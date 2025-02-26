def manejo_info(**kwars):
    for llave, valor in kwars.items():
        print(f"{llave}: {valor}")
        
manejo_info(nombre="David", apellido="Perez", edad=22, ciudad="Alemania", profesion="Ingeniero")