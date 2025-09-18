courses = [(10, 55), (5, 25), (21.1, 100)]
# On définit une liste appelée "courses".
# Chaque élément est un tuple (distance, temps) → distance en km, temps en minutes.
# Ex : (10, 55) = une course de 10 km en 55 minutes.

for dist, time in courses:
    # La boucle "for" va parcourir chaque tuple de la liste.
    # "dist" reçoit la distance du tuple, "time" reçoit le temps.
    # Ex : première boucle → dist=10, time=55.

    pace_min_per_km = time / dist
    # On calcule l'allure en minutes par km.
    # Exemple : 55 min ÷ 10 km = 5.5 (soit 5 minutes 30 secondes au km).

    minutes = int(pace_min_per_km)
    # On prend seulement la partie entière → ça donne les minutes de l’allure.
    # int(5.5) = 5 minutes.

    secondes = int(round((pace_min_per_km - minutes) * 60))
    # On enlève la partie entière pour garder la partie décimale.
    # (5.5 - 5) = 0.5 → *60 = 30 secondes.
    # round(...) pour éviter les erreurs d’arrondi (ex : 29.999 → 30).
    # int(...) pour obtenir un entier.

    if secondes == 60:
        minutes += 1
        secondes = 0
    # Cas particulier : si le calcul donne 60 secondes (ex : 59.999 arrondi à 60).
    # On corrige : +1 minute et secondes = 0.

    vitesse_moyenne = (dist / time) * 60
    # Calcul de la vitesse moyenne en km/h.
    # On divise la distance (km) par le temps (min) → dist/time = km/min.
    # On multiplie par 60 pour convertir en km/h.
    # Ex : 10 / 55 = 0.1818 km/min → *60 = 10.91 km/h.

    print(f"Pour {dist} km en {time} min :")
    # Affichage d'une phrase introductive avec la distance et le temps de la course.
    # f-string permet d'insérer directement les variables {dist} et {time}.

    print(f"  Pace : {minutes:02d}:{secondes:02d} min/km")
    # Affichage de l’allure formatée : MM:SS.
    # {minutes:02d} → entier sur 2 chiffres (05 au lieu de 5).
    # {secondes:02d} → idem pour les secondes.

    print(f"  Vitesse moyenne : {vitesse_moyenne:.2f} km/h")
    # Affichage de la vitesse avec 2 décimales.
    # {vitesse_moyenne:.2f} → format flottant avec 2 chiffres après la virgule.

    if pace_min_per_km > 6:
        print("  « Endurance fondamentale 🐢 »")
    elif pace_min_per_km >= 5:
        print("  « Tempo / Confort ⚡ »")
    elif pace_min_per_km >= 4:
        print("  « Seuil / Course rapide 🔥 »")
    else:
        print("  « Vitesse / Compétition 🚀 »")
    # Conditions pour classer l’allure en zone.
    # - si allure > 6 min/km → Endurance
    # - si entre 5 et 6 → Tempo
    # - si entre 4 et 5 → Seuil
    # - si < 4 → Vitesse/Compétition
    # "elif" = "else if" en Python (équivalent de "elsif" en Ruby).
    # Pas de "end", c’est l’indentation qui fait la structure.

    print("-" * 28)
    # Affiche une ligne de séparation pour plus de lisibilité.
    # "-" * 28 → répète le caractère "-" 28 fois.
