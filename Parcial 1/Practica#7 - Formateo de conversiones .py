import datetime

print("Seleccione un formato para la fecha: ")
print("1. Imprimir en el formato YYYY-MM-DD")
print("2. Imprimir en el formato DD-MM-YYYY")

opcion = int(input("Ingrese la opcion: "))


diaActual = datetime.date.today()

if opcion == 1: print("Fecha en el formato YYYY-MM-DD: ", diaActual)
elif opcion == 2: print("Fecha en el formato DD-MM-YYYY: ", diaActual.strftime("%d-%m-%Y"))
else: print("Opcion invalida, porfavor selecciona 1 o 2")