def capturar_materias():
    materias = {}
    semestre = int(input("Ingrese el número de semestre (de 1 a 7): "))
    
    if semestre < 1 or semestre >= 8:
        print("Número de semestre no válido.")
        return
    
    while True:
        asignatura = input("Ingrese el nombre de la materia (o 'fin' para terminar): ")
        if asignatura.lower() == 'fin':
            break
        
        try:
            creditos = int(input(f"Ingrese los créditos de {asignatura}: "))
            if creditos < 0:
                print("Los créditos no pueden ser negativos.")
                continue
            
            materias[asignatura] = creditos
        except ValueError:
            print("Por favor, ingrese un número válido de créditos.")
    
    print("\nResumen del semestre:")
    total_creditos = sum(materias.values())
    for asignatura, creditos in materias.items():
        print(f"{asignatura} tiene {creditos} créditos.")
    
    print(f"Total de créditos del semestre: {total_creditos}")

capturar_materias()
