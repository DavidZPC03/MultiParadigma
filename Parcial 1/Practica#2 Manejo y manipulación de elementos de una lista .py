# Problema 2: Manipulación de una lista
import string  # Módulo que contiene el abecedario en inglés

# Crear una lista con el abecedario
afabet = list(string.ascii_lowercase)  # Genera ['a', 'b', 'c', ..., 'z']

# Eliminar las letras en posiciones múltiplos de 3 (considerando índice base 1)
resultado = [letra for i, letra in enumerate(afabet, start=1) if i % 3 != 0]

# Mostrar la lista resultante
print("Lista después de eliminar posiciones múltiplos de 3:", resultado)