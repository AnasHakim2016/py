from pathlib import Path

ordner = Path(".")

for eintrag in ordner.iterdir():
    print(eintrag)

print("\n#######################################:")

from pathlib import Path

ordner = Path("workshop")

for eintrag in ordner.rglob("*"):
    print(eintrag)