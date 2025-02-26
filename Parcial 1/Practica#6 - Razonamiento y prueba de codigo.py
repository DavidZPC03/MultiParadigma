numeros = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez", "once", "doce", "trece", "catorce", "quince", "dieciseis", "diecisiete", "dieciocho", "diecinueve", "veinte"]
numUsuario = int(input("Introduce un número del 0 al 20: "))
print(numeros[numUsuario] if 0 <= numUsuario <= 20 else "Número fuera de rango")