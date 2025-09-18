etudiants = [("Alice", 18), ("Bob", 12), ("Charlie", 8), ("Diana", 15), ("Eve", 20)]
def classer_note(note):
    if note >= 16:
        return "« Excellent 🌟 »"
    elif 10 <= note <= 15:
        return "« Passable 🙂 »"
    else:
        return "« Insuffisant ❌ »"

for nom, note in etudiants:
    print(f"{nom} a eu {note} sur 20 : {classer_note(note)}")
