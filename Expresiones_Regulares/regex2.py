import re

# La cadena en la que se buscarán los patrones
texto = "La fecha es 24/06/2021 y el telefono es +1-555-555-5533"

# El patron a buscar
pattern = r"\d{2}/\d{2}/\d{4}"

# Cadena de texto que se usara para remplazar el patron
remplace = "Fecha oculta"

# Remplazar todas las apariciones del patron en la cadena de texto
new_text = re.sub(pattern,remplace,texto)

# Imprimir el resultado
print("Texto modificado: ",new_text)