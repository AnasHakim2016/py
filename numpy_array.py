import numpy as np

# Erzeugung in kWh, Woche 1 und Woche 2
erzeugt_w1 = np.array([2.1, 3.4, 1.8, 2.9, 3.7, 0.9, 2.5])
erzeugt_w2 = np.array([3.1, 2.7, 1.2, 3.9, 2.2, 3.5, 1.6])

# Verbrauch in kWh, Woche 1 und Woche 2
verbraucht_w1 = np.array([1.5, 3.9, 2.0, 2.4, 2.1, 1.8, 3.0])
verbraucht_w2 = np.array([2.8, 2.0, 2.6, 1.7, 3.4, 2.9, 2.2])

# Vergütung pro eingespeister kWh in Euro
einspeiseverguetung = 0.08

erzeugt = np.concatenate([erzeugt_w1,erzeugt_w2])
verbraucht = np.concatenate([verbraucht_w1,verbraucht_w2])
print(erzeugt)
ueberschuss=(erzeugt-verbraucht)
print (ueberschuss)
verguetung=ueberschuss[ueberschuss > 0]
print([verguetung])
einspeiseverguetung = 0.08


einspeisung = ueberschuss.copy()
einspeisung[einspeisung < 0] = 0
verguetung = einspeisung * einspeiseverguetung

tabelle = np.column_stack([erzeugt, verbraucht, ueberschuss])

print("Überschuss (kWh):", ueberschuss)
print("Vergütung pro Tag (€):", verguetung)
print("Form der Tabelle:", tabelle.shape)