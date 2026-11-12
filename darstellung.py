from auswertung import gesamtkilometer, durchschnitt, aktivste

def formatiere_zeile(mitglied):
    name = mitglied["name"]
    gesamt = gesamtkilometer(mitglied)
    schnitt = durchschnitt(mitglied)
    return f"{name:<8} {gesamt:>6.1f} km gesamt   {schnitt:>5.1f} km im Schnitt"

def formatiere_bericht(mitglieder):
    zeilen = [formatiere_zeile(m) for m in mitglieder]
    spitze = aktivste(mitglieder)
    zeilen.append("")
    zeilen.append(f"Aktivstes Mitglied: {spitze['name']} ({gesamtkilometer(spitze):.1f} km)")
    return "\n".join(zeilen)