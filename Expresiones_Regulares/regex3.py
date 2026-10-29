import re
# Cadena de texto de ejemplo
texto = "remplazando todas las vocales por el asterisco"

# Remplaza la cadena de texto por cualquier vocal [aeiou], [*] todas las letras que coincidan seran remplazadas por * en texto
new_text = re.sub("[aiou]","*",texto)

# Impresion de resutlados
print(new_text)