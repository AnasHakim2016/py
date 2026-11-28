import numpy as np

# Täglich verkaufte Brote, vier Wochen (Zeilen) zu je sieben Tagen (Spalten)
verkauf = np.array([
    [42, 55, 48, 51, 60, 88, 30],
    [40, 52, 50, 47, 63, 91, 28],
    [45, 58, 53, 49, 66, 95, 33],
    [38, 50, 46, 52, 61, 84, 27],
])

gesamtsumme = np.sum(verkauf)

tagesdurchschnitt = np.mean(verkauf)

bester_tag = np.max(verkauf)
schwaechster_tag = np.min(verkauf)

streuung = np.std(verkauf)

wochendurchschnitt = np.mean(verkauf, axis=1)


print(f"Gesamtsumme verkaufter Brote (4 Wochen): {gesamtsumme}")
print(f"Durchschnitt pro Tag: {tagesdurchschnitt:.1f}")
print(f"Bester Tag (Maximum): {bester_tag} | Schwächster Tag (Minimum): {schwaechster_tag}")
print(f"Standardabweichung (Streuung): {streuung:.1f}")
print(f"Durchschnitt je Woche (Woche 1–4): {np.round(wochendurchschnitt, 1)}")