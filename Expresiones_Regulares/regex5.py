import re

# Cadena de texto de ejemplo para un sitio web
texto = "Este es un eejemplo de pagina web: https://www.example.com y tambien podemos visualizar"

# Patron para validificar si la cadena es real
patron = r"https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Buscamos la pagina web
resultado = re.findall(patron,texto)

# Mostramos en pantalla el resultado
print(resultado)