class Lesefortschritt:
    def __init__(self, title, gesamtseiten):
        self.title = title
        self.gesamtseiten = gesamtseiten
   
    def fortschritt(self, gelesener_seiten):
        return f"{(gelesener_seiten / self.gesamtseiten) * 100:.2f}%"

    def weiterlesen(self, gelesener_seiten):
        print(f"Seite {gelesener_seiten} von {self.gesamtseiten} gelesen und Fortschritt zeigt: {self.fortschritt(gelesener_seiten)}")

mein_buch = Lesefortschritt("Python für Einsteiger", 300)
mein_buch.weiterlesen(75)
