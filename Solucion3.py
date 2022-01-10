'''
Crear una clase llamada “cuenta”. Al instanciar la clase se debe proveer el número de
cuenta, el nombre el titular, saldo inicial, tipo cuenta (ahorro, corriente, inversiones). Crear
tres métodos depositar, retirar, obtener balance. Si en la cuenta1 hay un saldo inicial de
10 y se hace un depósito de 20 y un retiro de 5, entonces al obtener el balance debe
mostrar un saldo de <5. Imprimir la información con todos los datos de usuarios y
balances.

'''
# Importamos estos modulos para manipular algunas cosas en nuestro script.
import os,time
from os import path


class Cuenta():
    # Variables de clase para almacenar los datos solicitados al usuario
    numero_cuenta = 0
    nombre_titular = ""

    # Creamos una pequeña lista para almacenar los tipos de cuentas.
    tipos_cuentas = ["Ahorro", "Corriente", "Inversiones"]

    # Para el manejo de los datos antiguos y nuevos.
    lista_antigua = []
    datos_nuevos = ""

    # Con estas variables manejamos las posiciones de nuetros datos (funcionan como id)
    posicion = 0
    posicion_editado = 0

    # Creamos  he instanciamos nuestras variables para el tratamiento del saldo.
    saldo_anterior = 0
    saldo_inicial = 0
    saldo_actual = 0

    # Creamos nuestro constructor de la clase.
    def __init__(self):
            
        # Verificamos mediante el modulo os con sus metodos, path y isfile y le pasamos como parametro nuestro archivo
        # si no existe lo creamos en modo estritura (write).
        
        if not os.path.isfile(os.path.dirname(os.path.realpath(__file__))+"/bd.txt"):
        
            base_clientes = open(os.path.dirname(os.path.realpath(__file__))+"/bd.txt", "w")
        self.menu_principal()

    # Metodo para depositar, al igual que el metodo retirar se le pasa el parametro de numero de cuenta.
    def depositar(self,ncuenta):

        conexion = open(os.path.dirname(os.path.realpath(__file__))+"/bd.txt","r+")
        cuentas = list(conexion.readlines(0))
        for i in range(0, len(cuentas)):
            datos = list(cuentas[i].split(","))
            if datos[0] == ncuenta:
                tipo = self.tipos_cuentas[int(datos[5])]
                print("Datos del Cliente\n")
                print(f"N° Cuenta:{datos[0]}\nNombre Cliente: {datos[1]}\nSaldo Anterior: ${datos[2]}\nSaldo Inicial: {datos[3]}\nSaldo Actual: {datos[4]}\nTipo Cuenta:{tipo}", end="")
                datos[2] = datos[4]
                nuevo_saldo = input("Monto a depositar: $")
                dinero = datos[2].replace("\n", "")
                datos[4] = int(dinero)+int(nuevo_saldo)
                cuentas[i] = datos[0]+","+datos[1]+","+str(datos[2])+","+str(datos[3])+","+str(datos[4])+","+str(datos[5])
                self.posicion_editado = i
                self.datos_nuevos = cuentas[i]
            else:
                posicion = i
                datos_antiguos = cuentas[i]
                self.lista_antigua.insert(posicion, datos_antiguos)


        self.lista_antigua.insert(self.posicion_editado, self.datos_nuevos)
        conexion.truncate(0)
        conexion.close()
        conexion = open(os.path.dirname(os.path.realpath(__file__))+"/bd.txt", "r+")

        for n in self.lista_antigua:
            conexion.writelines(n)

        conexion.close()

    # Metodo para retirar dinero, le pasamos el numero de cuenta para ser filtrado.
    def retirar(self,ncuenta):
    
        
        conexion = open(os.path.dirname(os.path.realpath(__file__))+"/bd.txt","r+")
        cuentas = list(conexion.readlines(0))
        for i in range(0, len(cuentas)):
            datos = list(cuentas[i].split(","))

            if datos[0] == ncuenta:
                tipo = self.tipos_cuentas[int(datos[5])]
                print("Datos del Cliente\n")
                print(f"N° Cuenta:{datos[0]}\nNombre Cliente: {datos[1]}\nSaldo Anterior: ${datos[2]}\nSaldo Inicial: {datos[3]}\nSaldo Actual: {datos[4]}\nTipo Cuenta:{tipo}", end="")
                datos[2] = datos[4]
                control_retiro = True
                while control_retiro:
                    monto_giro = input("Monto a retirar: $")
                    dinero = datos[2].replace("\n", "")
                    if monto_giro <= dinero:
                        datos[4] = int(dinero)-int(monto_giro)
                        cuentas[i] = datos[0]+","+datos[1]+","+str(datos[2])+","+str(datos[3])+","+str(datos[4])+","+str(datos[5])
                        self.posicion_editado = i
                        self.datos_nuevos = cuentas[i]
                        control_retiro = False
                    elif dinero == "0":
                        break
                    else:
                        print("ADVERTENCIA:\nEl monto solicitado exede el al saldo actual, \npor favor ingrese un nuevo saldo o ingrese 0 para salir.")
                        control_retiro = True
            else:
                posicion = i
                datos_antiguos = cuentas[i]
                self.lista_antigua.insert(posicion, datos_antiguos)


        self.lista_antigua.insert(self.posicion_editado, self.datos_nuevos)
        conexion.truncate(0)
        conexion.close()
        conexion = open(os.path.dirname(os.path.realpath(__file__))+"/bd.txt", "r+")

        for n in self.lista_antigua:
            conexion.writelines(n)

        conexion.close()

    # Metodo para obtener nuestro hitorial de balances.
    def obtener_balance(self,ncuenta):

        # Abrimos nuestro archivo en modo lectura y escritura.
        conexion = open(os.path.dirname(os.path.realpath(__file__))+"/bd.txt","r+")

        # Leemos los datos y lo almacenamos en la variable cuentas
        cuentas = list(conexion.readlines(0))

        # Recorremos nustros datos y le damos formato.
        for i in range(0, len(cuentas)):
            datos = list(cuentas[i].split(","))
            if datos[0] == ncuenta:
                tipo = self.tipos_cuentas[int(datos[5])]
                
                print("=========================================================================================================================")
                print("|                                                 HISTORIAL BALANCE                                                     |")
                print("=========================================================================================================================")
                print(f"|    N° Cuenta    |    Nombre Cliente    |    Saldo Anterior    |  Saldo Inicial |  Saldo Actual    |    Tipo Cuenta    |")
                print("=========================================================================================================================")
                print(f"|    {datos[0]}        |    {datos[1]}              |         {datos[2]}            |     {datos[3]}       |      {datos[4]}           |    {tipo}      |")
                print("=========================================================================================================================")
          
        conexion.close()

    def listar_clientes(self):

        # Abrimos nuestro archivo en modo lectura y escritura.
        conexion = open(os.path.dirname(os.path.realpath(__file__))+"/bd.txt","r+")

        # Leemos los datos y lo almacenamos en la variable cuentas
        cuentas = list(conexion.readlines(0))
        print("=========================================================================================================================")
        print("|                                                 LISTA DE CLIENTES                                                     |")
        print("=========================================================================================================================")
        print(f"|    N° Cuenta    |    Nombre Cliente    |    Saldo Anterior    |  Saldo Inicial |  Saldo Actual    |    Tipo Cuenta    |")
        print("=========================================================================================================================")
            
        # Recorremos nustros datos y le damos formato.
        for i in range(0, len(cuentas)):
            datos = list(cuentas[i].split(","))
            
            tipo = self.tipos_cuentas[int(datos[5])]
            
            print(f"|    {datos[0]}        |    {datos[1]}              |         {datos[2]}            |     {datos[3]}       |      {datos[4]}           |    {tipo}      |")
        print("=========================================================================================================================")
          
        conexion.close()


    # Metodo para agregar un nuevo cliente a nuestro archivo.
    def agrega_cliente(self, num_cuenta, nom_titular, sal_inicial, tip_cuenta):

        # Obtenemos todos los datos necesarios del cliente.
        self.numero_cuenta = num_cuenta
        self.nombre_titular = nom_titular
        self.saldo_inicial = sal_inicial
        self.tipo_cuenta = tip_cuenta
        self.saldo_actual = self.saldo_inicial
        
        # Formateamos los datos y se lopasamos la lista para ser guardados.
        daltos_cliente = str(self.numero_cuenta)+",", self.nombre_titular + ",",str(self.saldo_anterior)+",", str(self.saldo_inicial)+",",str(self.saldo_actual)+",", str(self.tipo_cuenta)+"\n"
        
        # Abrimos nuestro archivo en modo a(append) para ir agregando el nuevo cliente al final del archivo.
        base_clientes = open(os.path.dirname(os.path.realpath(__file__))+"/bd.txt", "a")

        # Escribimos nuestro archivo con los datos
        base_clientes.writelines(list(daltos_cliente))

        # Por ultimo cerramos nuestro archivo, y retornamos un mensaje indicando que se agrego.
        base_clientes.close()
        return f"Cuenta {daltos_cliente[0]} agregada con exito"

    def menu_principal(self):
        # Dibujamos el menu con sus opciones.
        print("\n=============================")
        print("| Bienvenido a Banco IPP    |")
        print("|============================")
        print("| [1] Nuevo Cliente         |\n| [2] Depositar             |\n| [3] Retirar               |\n| [4] Obtener Balanse       |\n| [5] Listar Clientes       |\n| [6] Salir                 |")
        print("=============================\n")
       

os.system("cls")
# Instancacion del objeto.
cuenta1 = Cuenta()

while True:
    # Input para solicitar una opcion del menu.
    try:
        opcion_menu = int(input("Ingrese una opcion por favor: "))

        # Validamos la opcion ingresada por el usuario.
        if opcion_menu == 1:
            os.system("cls")
            cuenta = input("N° Cuenta: ")
            cliente = input("Nombre Titular: ")
            saldo = input("Saldo Inicial: $")
            print("\n[Elija tipo de cuenta]\n[0]Ahorro\n[1]Corriente\n[2]Inversiones")
            tipo_cuenta = input("Tipo Cuenta: ")

            # Invocamos el metodo para agregar un nuevo cliente.
            cuenta1.agrega_cliente(cuenta, cliente,saldo,tipo_cuenta)
            cuenta1.menu_principal()
        elif opcion_menu == 2:
            os.system("cls")
            # Invocamos el metodo para depositar dinero, el cual se le pasa el numero de cuenta como argumento.
            valida_numero_cuenta = True
            while valida_numero_cuenta:
                try:
                    numero_cuenta = int(input("Ingrese N° cuenta:"))
                    cuenta1.depositar(str(numero_cuenta))
                    cuenta1.menu_principal()
                    valida_numero_cuenta = False
                    
                except ValueError:
                    print("Debe ingresar nuemro de cuenta valido")
                    valida_numero_cuenta = True    

        elif opcion_menu == 3:
            os.system("cls")
            # Invocamos el metodo para retirar dinero, el cual se le pasa el numero de cuenta como argumento.
            valida_numero_cuenta = True
            while valida_numero_cuenta:
                try:
                    numero_cuenta = int(input("Ingrese N° cuenta:"))
                    cuenta1.retirar(str(numero_cuenta))
                    cuenta1.menu_principal()
                    valida_numero_cuenta = False
                    
                except ValueError:
                    print("Debe ingresar nuemro de cuenta valido")
                    valida_numero_cuenta = True
            
            
        elif opcion_menu == 4:
            os.system("cls")
            # Invocamos el metodo para listar el historial del balance, el cual se le pasa el numero de cuenta como argumento.
            cuenta1.obtener_balance(input("Ingrese N° de Cuenta del titular:"))
            cuenta1.menu_principal()
        elif opcion_menu == 5:
            os.system("cls")
            cuenta1.listar_clientes()
            cuenta1.menu_principal()
        elif opcion_menu == 6:
            print("Abandonando el sistema...")
            time.sleep(3)
            os.system("cls")
            print("Gracias por preferirnos, que tenga buen dia.")
            exit()
        else:
            os.system("cls")
            cuenta1.menu_principal()
            print("ADVERTENCIA:\nLa opcion ingresada no esta en el menu, \npor favor ingrese una opcion valida y vuelva a intentarlo por favor.\n")
    except ValueError:
         os.system("cls")
         cuenta1.menu_principal()
         print("ERROR:\nSolo se aceptan valores numericos.\n")