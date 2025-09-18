def classer_note(note):
    if note >= 16:
        return "« Excellent 🌟 »"
    elif 10 <= note <= 15:
        return "« Passable 🙂 »"
    else:
        return "« Insuffisant ❌ »"

print (classer_note(18))
print (classer_note(12))
print (classer_note(5))
