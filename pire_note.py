etudiants = [
    {"nom": "Alice", "note": 15},
    {"nom": "Bob", "note": 8},
    {"nom": "Charlie", "note": 12},
    {"nom": "Diana", "note": 19},
    {"nom": "Eve", "note": 5}
]

pire_note  = float("inf")
pire_etudiant = ""
meilleure_note = float("-inf")
meilleur_etudiant = ""


for etu in etudiants:
    if etu['note'] < pire_note:
        pire_note = etu['note']
        pire_etudiant = etu['nom']

    if etu['note'] > meilleure_note:
        meilleure_note = etu['note']
        meilleur_etudiant = etu['nom']

print(f"La meilleure note est {meilleure_note}, obtenue par {meilleur_etudiant}.")
print(f"La pire note est {pire_note}, obtenue par {pire_etudiant}.")
