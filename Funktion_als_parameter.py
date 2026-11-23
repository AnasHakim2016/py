def mit_pfand(preis):
    return preis + 0.25


# Schritt 1
def wende_an(funktion, preis):
    return funktion(preis)


# Schritt 2
def erzeuge_aufschlag(prozent):
    def aufschlag(preis):
        return preis * (1 + prozent / 100)
    return aufschlag


# Testausgaben zu den Schritten
print(wende_an(mit_pfand, 1.50))        # -> 1.75

mit_mwst = erzeuge_aufschlag(19)
print(mit_mwst(100))                    # -> 119.0

wochenendzuschlag = erzeuge_aufschlag(10)
print(wochenendzuschlag(50))            # -> 55.0

# Schritt 3: Übergeben und Erzeugen verbinden
print(wende_an(erzeuge_aufschlag(10), 50))  # -> 55.0