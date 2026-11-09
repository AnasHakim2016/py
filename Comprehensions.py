temperaturen_celsius = [3.4, -1.2, 18.7, 25.1, 0.0, 12.5, 28.3, -4.0, 21.9, 30.2, 7.8, 24.6]

temperaturen_fahrenheit = [wert * 9/5 + 32 for wert in temperaturen_celsius]


hitzetage= [wert for wert in temperaturen_celsius if wert > 30.0]


messwerte = [3.4, -1.2, 18.7, 25.1, 0.0, 12.5, 28.3, -4.0, 21.9, 30.2, 7.8, 24.6]

windgeschwindigkeiten = [round(flautewerte,1)  for flautewerte in messwerte if flautewerte < 5.0]

print("Temperaturen in Fahrenheit:", temperaturen_fahrenheit)
print("Hitzetage:", hitzetage)
print ("Windgeschwindigkeiten:", windgeschwindigkeiten)