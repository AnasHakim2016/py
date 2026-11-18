messwerte = [
    ("Montag", 12.4),
    ("Dienstag", 14.1),
    ("Mittwoch", 15.8),
    ("Donnerstag", 13.2),
    ("Freitag", 17.3),
    ("Samstag", 16.0),
    ("Sonntag", 14.9),
]

temp_Durchschnitt = 0
with open("wochenbericht.txt", "w") as datei:
    for tag, temperatur in messwerte:
        datei.write(f"{tag}: {temperatur} °C\n")
        temp_Durchschnitt += temperatur



with open("wochenbericht.txt", "r") as datei:
    inhalt = datei.read()
    print(inhalt)  

print((f"Durchschnitt: {round(temp_Durchschnitt/7, 2)} °C\n"))

