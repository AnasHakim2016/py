import asyncio
import time


async def lade(name, dauer):
    print(f"{name}: warte {dauer} s")
    await asyncio.sleep(dauer)
    with open("tempasync.txt", "a", encoding="utf-8") as f:
        for i in range(1000):
            f.write(f"{name} liefert Ergebnis {i + 1}\n")
    return f"{name} liefert Ergebnis"


async def main():
    start = time.perf_counter()
    ergebnisse = await asyncio.gather(
        lade("Quelle 1", 2),
        lade("Quelle 2", 1),
        lade("Quelle 3", 3),
    )

    for ergebnis in ergebnisse:
        print(ergebnis)

    for xxx in range(50):
        print(f"zweite prozess {xxx + 1}")
   
    ende = time.perf_counter()
    print(f"Gesamtdauer: {ende - start:.3f} s")


asyncio.run(main())