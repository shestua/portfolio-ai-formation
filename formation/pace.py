distance_km = float(input("Distance (en km) : "))
temps_min = float(input("Temps total (en minutes) : "))

pace_min_per_km = temps_min / distance_km
minutes = int(pace_min_per_km)
secondes = int(round((pace_min_per_km - minutes) * 60))


if secondes == 60:
    minutes += 1
    secondes = 0

vitesse_moyenne = (distance_km / temps_min) * 60

print(f"Pace : {minutes:02d}:{secondes:02d} min/km")
print(f"Vitesse moyenne : {vitesse_moyenne:.2f} km/h")


if pace_min_per_km > 6: print ("« Endurance fondamentale 🐢 »")
elif pace_min_per_km >= 5: print ("« Tempo / Confort ⚡ »")
elif pace_min_per_km >= 4: print ("« Seuil / Course rapide 🔥 »")
else: print ("« Vitesse / Compétition 🚀 »")



