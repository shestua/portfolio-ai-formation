notes = {
    "Alice": 15,
    "Bob": 8,
    "Charlie": 12,
    "Diana": 19,
    "Eve": 5
}


for nom, note in notes.items():
    if note >= 16:
        print(f"{nom} a eu {note} sur 20." "« Excellent 🌟 »")
    elif 10 <= note <= 15:
        print(f"{nom} a eu {note} sur 20." "« Passable 🙂 »")
    else:
        print(f"{nom} a eu {note} sur 20." "« Insuffisant ❌ »")
