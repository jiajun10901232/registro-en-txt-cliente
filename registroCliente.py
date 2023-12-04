import os

class Usuario:
    def __init__(self, password, username):
        self.__password = password
        self.__username = username

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    def get_username(self):
        return self.__username

    def set_username(self, username):
        self.__username = username

def registrar_usuario():
    username = input("Ingrese el nombre de usuario: ")
    password = input("Ingrese la contraseña: ")

    usuario = Usuario(password, username)

    with open("usuarios.txt", "a") as f:
        f.write(f"{usuario.get_username()},{usuario.get_password()}\n")

    print("Usuario registrado con éxito.")

def ir_main():
    import main
    main.iniciar()  

while True:
    print("Bienvenido al programa de gestión.")
    print("1. Registrar usuario")
    print("2. ir main")    
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        registrar_usuario()
    elif opcion == "2":
        ir_main()        
    elif opcion == "3":
        break
    else:
        print("Opción inválida.")

    input("Presione enter para continuar...")
    os.system("clear")
