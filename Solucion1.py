'''
Crear un programa que determine si una contraseña es segura o no. Se considera segura
si tiene al menos una mayúscula, una minúscula y un número. Se debe utilizar funciones.

'''
def valida_clave(clave):
    # Inicializamos los test en 0.
    cmp_mayuscula = 0
    cmp_minuscula = 0
    cmp_numero = 0

    # Recorremos caracter a caracter la clave ingresada por el usuario.
    for caracter in clave:
        # Analizamos, si posee una mayuscula, entonces cmp_mayuscula se ponen en 1.
        if caracter.isupper():
            cmp_mayuscula = 1        
        # Analizamos, si posee una minuscula, entonces cmp_minuscula se ponen en 1.
        if caracter.islower():
            cmp_minuscula = 1        
        # Analizamos, si posee una numero, entonces se ponen en 1.
        if caracter.isdigit():
            cmp_numero = 1

    # Cuando salimos del bucle for, validamos los test, si todos pasaron entonces la clave es segura.
    if cmp_mayuscula == 1 and cmp_minuscula == 1 and cmp_numero == 1:
        return 1
    else:
        return 0

# Solicitamos al usuario una clave, y la convertimos en una lista para su mejor manipulacion.
while True:
    # Validamos que el usuario ingrese una contraseña valida.
    clave = list(input("Ingrese clave a validar: "))
    if valida_clave(clave) == 1:
        print("La clave ingresada es segura.")
        break
    else:
        print("ERROR:\nLa clave ingresada es insegura.")



