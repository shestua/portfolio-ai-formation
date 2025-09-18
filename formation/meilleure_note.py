etudiants = [
    {"nom": "Alice", "note": 15},
    {"nom": "Bob", "note": 8},
    {"nom": "Charlie", "note": 12},
    {"nom": "Diana", "note": 19},
    {"nom": "Eve", "note": 5}
]

# Initialisation
meilleure_note = float("-inf")
meilleur_etudiant = ""

# Parcours
for etu in etudiants:
    if etu['note'] > meilleure_note:
        meilleure_note = etu['note']
        meilleur_etudiant = etu['nom']

# Affichage
print(f"La meilleure note est {meilleure_note}, obtenue par {meilleur_etudiant}.")
