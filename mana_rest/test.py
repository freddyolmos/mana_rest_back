with open('datos.json', 'rb') as f:
    content = f.read()

# Remove BOM if it exists
if content.startswith(b'\xef\xbb\xbf'):
    content = content[3:]

with open('datos.json', 'wb') as f:
    f.write(content)
