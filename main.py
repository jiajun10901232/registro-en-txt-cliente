import os

def ir_cliente():
    import cliente
    cliente.login()

def ir_admin():
    import admin
    admin.login()

def ir_registro():
    import registroCliente
    registroCliente.login()


#Menu de opciones para el usuario
while True:
    print("1. Cliente")
    print("2. Admin")
    print("3. Registro de Usuario")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        ir_cliente()
    elif opcion == "2":
        ir_admin()
    elif opcion == "3":
        ir_registro()
    elif opcion == "4":
        break
    else:
        print("Opción inválida.")
        os.system("clear")
    

input("Presione enter para continuar...")
