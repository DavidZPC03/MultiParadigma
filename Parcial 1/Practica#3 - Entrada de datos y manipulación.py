def main():
    nombre = input("Ingrese su nombre completo: ")
    print("Nombre en orden inverso:")
    for letra in reversed(nombre):
        print(letra)

if __name__ == "__main__":
    main()
