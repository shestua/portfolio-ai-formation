note = [("Alice", 15), ("Bob", 8), ("Charlie", 12), ("Diana", 19), ("Eve", 5)]

for nom, note in note:
    print (f"{nom} a eu {note} sur 20.")


    if note >= 16:
        print  ("« Excellent 🌟 »")

    elif 10 <= note <= 15:
        print ("« Passable 🙂 »")

    else:
        print ("« Insuffisant ❌ »")
