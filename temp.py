from __future__ import annotations

from collections.abc import Callable, Iterator
from dataclasses import dataclass
from functools import wraps
import json
from pathlib import Path
import time
from typing import Any


@dataclass(frozen=True)
class Transaktion:
    konto: str
    betrag: float
    kategorie: str

    def __post_init__(self) -> None:
        if not isinstance(self.konto, str) or not self.konto.strip():
            raise ValueError("Feld 'konto' fehlt oder ist leer.")
        if isinstance(self.betrag, bool) or not isinstance(self.betrag, (int, float)):
            raise ValueError("Feld 'betrag' muss numerisch sein.")
        betrag_float = float(self.betrag)
        if not isinstance(self.kategorie, str) or not self.kategorie.strip():
            raise ValueError("Feld 'kategorie' fehlt oder ist leer.")
        object.__setattr__(self, "betrag", betrag_float)

    def __str__(self) -> str:
        return f"Transaktion({self.konto}: {self.betrag:.2f} [{self.kategorie}])"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Transaktion):
            return NotImplemented
        return (
            self.konto == other.konto
            and self.betrag == other.betrag
            and self.kategorie == other.kategorie
        )

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Transaktion):
            return NotImplemented
        return self.betrag < other.betrag

    def to_dict(self) -> dict[str, Any]:
        return {
            "konto": self.konto,
            "betrag": self.betrag,
            "kategorie": self.kategorie,
        }


def zeilen_strom(pfad: Path, fehler_zaehler: list[int]) -> Iterator[Transaktion]:
    """Liest eine JSONL-Datei zeilenweise verzögert ein und liefert gültige Transaktionen."""
    with pfad.open("r", encoding="utf-8") as fh:
        for zeile in fh:
            roh = zeile.strip()
            if not roh:
                continue
            try:
                daten = json.loads(roh)
                if not isinstance(daten, dict):
                    raise TypeError("Zeile ist kein JSON-Objekt.")
                yield Transaktion(
                    konto=daten["konto"],
                    betrag=daten["betrag"],
                    kategorie=daten["kategorie"],
                )
            except (json.JSONDecodeError, KeyError, TypeError, ValueError):
                fehler_zaehler[0] += 1


def top_drei_aktualisieren(bestenliste: list[Transaktion], tx: Transaktion) -> list[Transaktion]:
    """Hält maximal die drei größten Transaktionen absteigend fest (auch bei Gleichstand)."""
    kandidaten = [*bestenliste, tx]
    kandidaten.sort(reverse=True)
    return kandidaten[:3]


def zeit_messen(func: Callable[..., dict[str, Any]]) -> Callable[..., dict[str, Any]]:
    """Misst die Laufzeit der Auswertung und ergänzt 'dauer_sekunden' im Bericht."""

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> dict[str, Any]:
        start = time.perf_counter()
        bericht = func(*args, **kwargs)
        bericht["dauer_sekunden"] = round(time.perf_counter() - start, 6)
        return bericht

    return wrapper


@zeit_messen
def auswerten(eingabe_pfad: Path) -> dict[str, Any]:
    """Durchläuft die Datei genau einmal und berechnet alle Kennzahlen."""
    fehler_zaehler = [0]
    summen_roh: dict[str, float] = {}
    konten_set: set[str] = set()
    bestenliste: list[Transaktion] = []

    for tx in zeilen_strom(eingabe_pfad, fehler_zaehler):
        summen_roh[tx.kategorie] = summen_roh.get(tx.kategorie, 0.0) + tx.betrag
        konten_set.add(tx.konto)
        bestenliste = top_drei_aktualisieren(bestenliste, tx)

    summe_je_kategorie = {
        kategorie: round(summen_roh[kategorie], 2)
        for kategorie in sorted(summen_roh)
    }

    return {
        "summe_je_kategorie": summe_je_kategorie,
        "konten": sorted(konten_set),
        "groesste": [tx.to_dict() for tx in bestenliste],
        "fehlerhafte_zeilen": fehler_zaehler[0],
    }


def main() -> None:
    eingabe = Path("transaktionen.jsonl")
    ausgabe = Path("bericht.json")

    bericht = auswerten(eingabe)
    ausgabe.write_text(
        json.dumps(bericht, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()