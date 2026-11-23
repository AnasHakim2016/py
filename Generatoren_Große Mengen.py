#Schritt 1
def werte_einzeln(liste):
    for wert in liste:
        yield wert


gen = werte_einzeln(["A", "B", "C", 42])
for element in gen:
    print(element)

#Schritt 2
import sys

def laufende_summe(folge):
    summe = 0
    for wert in folge:
        summe += wert
        yield summe


def laufende_summe_liste(folge):
    summe = 0
    ergebnis = []
    for wert in folge:
        summe += wert
        ergebnis.append(summe)
    return ergebnis


# Kurzer Funktionstest
print("Beispiel [10, 12, 11]:", list(laufende_summe([10, 12, 11])))
print("Liste    [10, 12, 11]:", laufende_summe_liste([10, 12, 11]))

# Speichervergleich für 1.000.000 Elemente
gen_obj = laufende_summe(range(1_000_000))
liste_obj = laufende_summe_liste(range(1_000_000))

print(f"Größe Generatorobjekt: {sys.getsizeof(gen_obj):,} Bytes")
print(f"Größe fertige Liste:   {sys.getsizeof(liste_obj):,} Bytes")

#Schritt 3
import random
def endlose_werte():
    while True:
        yield round(random.uniform(15, 25), 1)


for index, wert in enumerate(endlose_werte(), start=1):
    print(f"Wert {index}: {wert}")
    if index >= 10:
        break


#Schritt 4
import random

def endlose_werte():
    while True:
        yield round(random.uniform(15, 25), 1)


def filtern_ueber_schwelle(quelle, schwelle):
    for wert in quelle:
        if wert > schwelle:
            yield wert


def als_warnung(quelle):
    for wert in quelle:
        yield f"Warnung: {wert}"


pipeline = als_warnung(filtern_ueber_schwelle(endlose_werte(), schwelle=22.0))

for i, meldung in enumerate(pipeline, start=1):
    print(meldung)
    if i >= 5:
        break