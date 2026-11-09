messwerte = [3.4, -1.2, 18.7, 25.1, 0.0, 12.5, 28.3, -4.0, 21.9, 30.2, 7.8, 24.6]
alle_werte = []
for wert in messwerte:
    alle_werte.append(wert)



frostfreie_tage = []
for wert in messwerte:
    if wert >= 0:
        frostfreie_tage.append(wert)



sommertage_text=[]
for wert in frostfreie_tage:
        if wert > 25.0:
            sommertage_text.append(f"{wert} °C")

print("Alle Werte:", alle_werte)
print("Frostfreie Tage:", frostfreie_tage)  
print(frostfreie_tage)