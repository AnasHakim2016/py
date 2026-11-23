# kasse.py

from collections.abc import Iterable


def mit_steuer(betrag: float, satz: float = 0.19) -> float:
    return betrag * (1 + satz)


def beleg_zeile(name: str, betrag: float) -> str:
    return f"{name}: {betrag:.2f} Euro"


def netto_summe(preise: Iterable[float]) -> float:
    return sum(preise)


def finde_preis(preisliste: dict[str, float], name: str) -> float | None:
    if name in preisliste:
        return preisliste[name]
    return None


if __name__ == "__main__":
    katalog: dict[str, float] = {"Apfel": 0.80, "Brot": 2.50, "Kaese": 4.20}

    warenkorb: list[float] = [katalog["Apfel"], katalog["Brot"], katalog["Brot"]]
    netto: float = netto_summe(warenkorb)

    print(beleg_zeile("Zwischensumme", netto))
    print(beleg_zeile("Mit Steuer", mit_steuer(netto)))

    gesucht: float | None = finde_preis(katalog, "Kaese")
    if gesucht is not None:
        print(beleg_zeile("Kaese", gesucht))

    fehlt: float | None = finde_preis(katalog, "Milch")
    print("Milch im Katalog:", fehlt is not None)