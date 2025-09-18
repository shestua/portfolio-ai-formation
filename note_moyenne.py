etudiants = [
    {"nom": "Alice", "note": 15},
    {"nom": "Bob", "note": 8},
    {"nom": "Charlie", "note": 12},
    {"nom": "Diana", "note": 19},
    {"nom": "Eve", "note": 5}
]


valeurs = [etu['note'] for etu in etudiants]
moyenne = sum(valeurs) / len(valeurs)
moyenne_generale = sum(valeurs) / len(etudiants)
print(f"La moyenne générale de la classe est {moyenne_generale:.2f} sur 20.")
