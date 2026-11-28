import pandas as pd

df = pd.DataFrame({
    "produkt":   ["Apfel", "Karotte", "Bauernbrot", "Banane", "Kartoffel",
                  "Mango", "Vollkornbrot", "Zwiebel", "Erdbeere", "Kürbis"],
    "kategorie": ["Obst", "Gemüse", "Backwaren", "Obst", "Gemüse",
                  "Obst", "Backwaren", "Gemüse", "Obst", "Gemüse"],
    "preis_eur": [2.40, 1.10, 3.80, 1.90, 0.95,
                  4.50, 3.20, 0.80, 5.60, 2.10],
    "vorrat_kg": [35.0, 60.0, 12.0, 25.0, 80.0,
                  8.0, 15.0, 50.0, 6.0, 40.0],
    "herkunft":  ["regional", "regional", "regional", "import", "regional",
                  "import", "regional", "regional", "regional", "regional"],
})

# Dein Code ab hier
guenstig = df[df["preis_eur"] < 3 ]
print(guenstig)
regional = df[df["herkunft"] == "regional" ]
print(regional)
#print(df[(df["preis"] < 4.0) & (df["ware"] == "Apfel")])
aushang=df[(df["preis_eur"] < 3)  & (["herkunft"] == "regional")]
summe_1 = df[df["preis_eur"] <= 1 ]["preis_eur"].sum()
print(summe_1)
summe_2 = df[df["preis_eur"] <= 100 ]["preis_eur"].sum()
print(summe_2)