# Problema 1: Función con n parámetros para calcular el producto total

def producto_total(*numeros):
    """
    Recibe un número variable de parámetros y calcula su producto total.
    """
    producto = 1  # Inicializamos el producto en 1
    for num in numeros:
        producto *= num  # Multiplicamos cada número
    return producto

# Ejemplo de uso
resultado = producto_total(2, 3, 4)
print("El producto total es:", resultado)