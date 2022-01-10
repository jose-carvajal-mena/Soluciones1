'''
Escribir un programa que lea números ingresados y luego devuelva el total. Se debe
desarrollar usando recursión. No se pueden utilizar ciclos. Se ingresar números hasta que
el usuario ingrese un espacio. Si el primer input es un espacio, entonces imprime 0. 
'''
# Creamos dos listas una para almacenar los numeros y la otra para almacenar la sumatoria.
lista_numeros = []
sumatoria = [0]

# Creamos nuestra funcion recursiva.
def totalizar_numeros():
    numero = input("Ingrese Numero: ")

    # Validamos si el usuario ingreso el utlimo espacio y si la lista no esta vacia , entonces retornamos los resultados.
    if numero == " " and len(lista_numeros) != 0:
        return f"Numeros ingresasdos fueron: {lista_numeros} \nCantidad de numeros ingresados: {len(lista_numeros)} \nLa suma de los numeros es: {sumatoria[0]}"

    # Validamos si el usuario ingreso un espacio en el primer input y si la lista esta vacia, entonces almacenamos un 0.
    elif numero == " " and len(lista_numeros) == 0:
        numero = 0
        lista_numeros.append(numero)
        return totalizar_numeros()
    else:

        # Validamos que nuestra sumatoria no este vacia para ir agregando la suma de los numeros.
        if len(sumatoria) != 0:
            
            # Sumamos y agregamos la suma a nuestra lista.
            sumatoria[0] = sumatoria[0]+int(numero)
        lista_numeros.append(numero)
        return totalizar_numeros()


print(totalizar_numeros())
