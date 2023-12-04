import os

def login():
    username = input("Username: ")
    password = input("Password: ")

    with open("userAdmin.txt", "r") as file:
        for line in file:
            line = line.strip().split(",")
            if line[0] == username and line[1] == password:
                return True

    return False

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

class Producto:
    def __init__(self, codigo, nombre, precio):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio


def insertar_producto():
    codigo = input("Ingrese el código del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))

    producto = Producto(codigo, nombre, precio)

    with open("almacen.txt", "a") as f:
        f.write(
            f"{producto.get_codigo()}:{producto.get_nombre()}:{producto.get_precio()}\n")

    print("Producto insertado con éxito.")


def ver_producto():
    codigo = input("Ingrese el código del producto: ")
    with open("almacen.txt", "r") as f:
        for linea in f:
            campos = linea.strip().split(":")
            if campos[0] == codigo:
                print(
                    f"Código: {campos[0]}\nNombre: {campos[1]}\nPrecio: {campos[2]}")
                return
        print("Producto no encontrado.")


def modificar_producto():
    codigo = input("Ingrese el código del producto: ")
    precio = float(input("Ingrese el nuevo precio del producto: "))
    with open("almacen.txt", "r") as f:
        lineas = f.readlines()
    encontrado = False
    with open("almacen.txt", "w") as f:
        for linea in lineas:
            campos = linea.strip().split(":")
            if campos[0] == codigo:
                campos[2] = str(precio)
                f.write(f"{campos[0]}:{campos[1]}:{campos[2]}\n")
                encontrado = True
            else:
                f.write(linea)
    if encontrado:
        print("Producto modificado con éxito.")
    else:
        print("Producto no encontrado.")


def eliminar_usuario():
    username = input("Ingrese el nombre de usuario del usuario a eliminar: ")
    with open("usuarios.txt", "r") as f:
        lineas = f.readlines()
    encontrado = False
    with open("usuarios.txt", "w") as f:
        for linea in lineas:
            campos = linea.strip().split(":")
            if campos[3] == username:
                encontrado = True
            else:
                f.write(linea)
    if encontrado:
        print("Usuario eliminado con éxito.")
    else:
        print("Usuario no encontrado.")


def facturacion_total():
    total = 0.0

    with open("factura.txt", "r") as f:
        lineas = f.readlines()

    print("Facturación total:")
    for linea in lineas:
        if "Subtotal" in linea:
            subtotal = float(linea.split(":")[-1])
            total += subtotal
            print(linea.strip())

    print(f"Total a pagar: {total:.2f}")

def registrar_usuario():
    username = input("Ingrese el nombre de usuario: ")
    password = input("Ingrese la contraseña: ")

    usuario = Usuario(password, username)

    with open("userAdmin.txt", "a") as f:
        f.write(f"{usuario.get_username()},{usuario.get_password()}\n")

    print("Usuario registrado con éxito.")


def ir_main():
    import main
    main() 




if login():
    while True:
        print("Bienvenido al programa de gestión.")
        print("1. Crear producto")
        print("2. Ver producto")
        print("3. Modificar producto")
        print("4. Eliminar usuario")
        print("5. Facturación total")
        print("6. Registrar usuario")        
        print("7. ir main")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            insertar_producto()
        elif opcion == "2":
            ver_producto()
        elif opcion == "3":
            modificar_producto()
        elif opcion == "4":
            eliminar_usuario()
        elif opcion == "5":
            facturacion_total()
        elif opcion == "6":
            registrar_usuario()        
        elif opcion == "7":
            ir_main()       
        elif opcion == "8":
            break
        else:
            print("Opción inválida.")
        input("Presione enter para continuar...")   
        os.system("clear")

else:
    print("Credenciales inválidas. No puede acceder al programa de gestión.")
