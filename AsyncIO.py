import asyncio
import time
from pathlib import Path


def lies_und_zaehle(pfad):
    """Liest eine Logdatei und zählt die ERROR-Zeilen.
    Das time.sleep imitiert eine langsame Platte und blockiert dabei."""
    print(f"{pfad.name}: lese ...")
    text = pfad.read_text(encoding="utf-8")
    time.sleep(1)  # simulierte I/O-Latenz
    fehler = sum(1 for zeile in text.splitlines() if " ERROR " in zeile)
    print(f"{pfad.name}: {fehler} Fehler")
    return pfad.name, fehler


async def main():
    start = time.perf_counter()
    dateien = sorted(Path("logs").glob("*.log"))

    tasks = [asyncio.to_thread(lies_und_zaehle, pfad) for pfad in dateien]
    ergebnisse = await asyncio.gather(*tasks)

    gesamt = sum(f for _, f in ergebnisse)
    print(f"Gesamtfehler: {gesamt}")
    print(f"Gesamtdauer: {time.perf_counter() - start:.1f} s")


if __name__ == "__main__":
    asyncio.run(main())



# import os
# import random
# from pathlib import Path

# random.seed(7)
# logs_dir = Path("logs")
# logs_dir.mkdir(exist_ok=True)

# levels = ["INFO"] * 7 + ["WARNING"] * 2 + ["ERROR"]

# for name in ["auth", "payment", "search", "mailer"]:
#     log_path = logs_dir / f"{name}.log"
#     with log_path.open("w", encoding="utf-8") as f:
#         for i in range(random.randint(40, 120)):
#             f.write(
#                 f"2026-06-28 09:{i % 60:02d}:00 {random.choice(levels)} {name} Nachricht {i}\n"
#             )