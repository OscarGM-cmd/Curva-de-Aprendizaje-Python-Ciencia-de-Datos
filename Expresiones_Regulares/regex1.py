import re

# Cadena de texto de ejemplo
text = "The quick brown fox jumps over lazy dog"

# Busca un elemento que tenga al incio un The, busca todo menos los saltos de linea, y si hay dog al ultimo proporcionalo
x = re.search("^The.*dog$",text)

if x:
    print("Si")
else:
    print("No")
