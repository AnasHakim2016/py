def gesamtkilometer(mitglied):
    return sum(mitglied["laeufe"])

def durchschnitt(mitglied):
    laeufe = mitglied["laeufe"]
    if not laeufe:
        return 0.0
    return sum(laeufe) / len(laeufe)

def aktivste(mitglieder):
    return max(mitglieder, key=gesamtkilometer)