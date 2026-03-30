import re

file_path = "main.py"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace explicit corner_radiuses
content = re.sub(r'corner_radius=10\b', 'corner_radius=6', content)
content = re.sub(r'corner_radius=8\b', 'corner_radius=6', content)
content = re.sub(r'corner_radius=5\b', 'corner_radius=4', content)

# Add corner_radius=6 to CTkButton if not present
def add_radius_button(match):
    m = match.group(0)
    if 'corner_radius' not in m:
        # insert corner_radius before the closing parenthesis or just after CTkButton(
        return m.replace('ctk.CTkButton(', 'ctk.CTkButton(corner_radius=6, ')
    return m

content = re.sub(r'ctk\.CTkButton\([^)]*\)', add_radius_button, content)

# Add corner_radius=6 to CTkEntry if not present
def add_radius_entry(match):
    m = match.group(0)
    if 'corner_radius' not in m:
        return m.replace('ctk.CTkEntry(', 'ctk.CTkEntry(corner_radius=6, ')
    return m

content = re.sub(r'ctk\.CTkEntry\([^)]*\)', add_radius_entry, content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated corner_radiuses in main.py")
