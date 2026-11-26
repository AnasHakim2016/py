import numpy as np

# Stündliche Außentemperatur in Grad Celsius, Stunde 0 bis 23
temperaturen = np.array([
    11.2, 10.8, 10.3,  9.9,  9.5,  9.8,
    10.6, 12.4, 14.7, 16.9, 18.8, 20.1,
    21.4, 22.3, 22.8, 22.5, 21.7, 20.3,
    18.6, 16.9, 15.4, 14.1, 13.0, 12.1,
])

# Dein Code ab hier
# print(temperaturen[14])
# print(temperaturen[6:12])
# print(temperaturen[21:23])
# maske=temperaturen>20
print(maske)
print(temperaturen[maske])
print(temperaturen[(temperaturen>18) & (temperaturen<22)])