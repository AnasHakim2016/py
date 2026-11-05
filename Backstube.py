
name = input("Name eingeben: ")
bestellwert_eingabe = input("Bestellwert eingeben: ")
gutschein_eingabe = input("Gutscheinwert eingeben (0 wenn kein Code): ")

ausgabetext = ""


if name:
    ausgabetext = "Hallo " + name
else:
    ausgabetext = "Hallo zusammen" 

if bestellwert_eingabe:
    bestellwert = bestellwert_eingabe
    
    if gutschein_eingabe and gutschein_eingabe:
        gutschein = gutschein_eingabe
        endbetrag = float(bestellwert) - float(gutschein)
        ausgabetext = ausgabetext + " Bestellwert = " + str(endbetrag)
    else:
        ausgabetext = ausgabetext + ": " + bestellwert
else:
    ausgabetext = ausgabetext + ": Warenkorb leer"

print(ausgabetext)
 

          
