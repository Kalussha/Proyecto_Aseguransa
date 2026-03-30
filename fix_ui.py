import re

file_path = "main.py"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Remove the incorrectly placed keyword argument at the beginning
content = content.replace('ctk.CTkButton(corner_radius=6, \n', 'ctk.CTkButton(\n')
content = content.replace('ctk.CTkEntry(corner_radius=6, \n', 'ctk.CTkEntry(\n')

content = content.replace('ctk.CTkButton(corner_radius=6,\n', 'ctk.CTkButton(\n')
content = content.replace('ctk.CTkEntry(corner_radius=6,\n', 'ctk.CTkEntry(\n')

content = content.replace('ctk.CTkButton(corner_radius=6, ', 'ctk.CTkButton(')
content = content.replace('ctk.CTkEntry(corner_radius=6, ', 'ctk.CTkEntry(')

# 2. Append smartly correctly
def append_kwarg(match):
    m = match.group(0)
    # If corner_radius is somehow already there in the multiline block, do nothing
    if 'corner_radius=' in m:
        return m
    
    # Append safely before closing parens. But watch out for trailing commas
    # m ends with ')'
    inner = m[:-1].rstrip()
    if inner.endswith(','):
        return inner + ' corner_radius=6)'
    else:
        return inner + ', corner_radius=6)'

# Fix buttons
content = re.sub(r'ctk\.CTkButton\([^)]*\)', append_kwarg, content)
# Fix entries
content = re.sub(r'ctk\.CTkEntry\([^)]*\)', append_kwarg, content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Fixed syntax issues")
