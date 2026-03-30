with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace(" corner_radius=6)", ")")
content = content.replace(", corner_radius=6", "")
content = content.replace("corner_radius=6, ", "")
content = content.replace("corner_radius=6", "")
content = content.replace("(, ", "(")

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Stripped corner_radius=6")
