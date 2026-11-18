with open("notiz.txt", "r") as datei:
    inhalt = datei.read()

print(inhalt)

with open("notiz.txt", "r") as datei:
    for zeile in datei:
        print(zeile.rstrip())