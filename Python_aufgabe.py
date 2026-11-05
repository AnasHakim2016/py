
artikel_1 = "Äpfel"
menge_1 = 12
preis_1 = 0.8

artikel_2 = "Bauernbrot"
menge_2 = 7
preis_2 = 3.5

artikel_3 = "Bergkäse"
menge_3 = 4
preis_3 = 6.25


print(f"Artikel: {artikel_1}, Menge: {menge_1}, Einzelpreis: {preis_1}")
print("\n")

umsatz_1 = menge_1 * preis_1

print(
    f"Artikel: {artikel_1}, Menge: {menge_1}, Einzelpreis: {preis_1:.2f} €, Umsatz: {umsatz_1:.2f} €"
)
print("\n")

umsatz_1 = menge_1 * preis_1
umsatz_2 = menge_2 * preis_2
umsatz_3 = menge_3 * preis_3

gesamtumsatz = umsatz_1 + umsatz_2 + umsatz_3

print(f"{'Artikel':<15}{'Menge':>8}{'Einzelpreis':>14}{'Umsatz':>10}")

print(
    f"{artikel_1:<15}{menge_1:>8}{preis_1:>14.2f}{umsatz_1:>10.2f}"
)
print(
    f"{artikel_2:<15}{menge_2:>8}{preis_2:>14.2f}{umsatz_2:>10.2f}"
)
print(
    f"{artikel_3:<15}{menge_3:>8}{preis_3:>14.2f}{umsatz_3:>10.2f}"
)

