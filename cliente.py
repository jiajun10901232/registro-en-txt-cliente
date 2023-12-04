import os

def login():
    username = input("Username: ")
    password = input("Password: ")

    with open("usuarios.txt", "r") as file:
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

def ver_todo_producto():
    with open("almacen.txt", "r") as f:
        for linea in f:
            campos = linea.strip().split(":")
            codigo = campos[0]
            nombre = campos[1]
            precio = campos[2]
            print(f"Código: {codigo}\nNombre: {nombre}\nPrecio: {precio}\n")


def comprar_producto():
    productos_comprados = []
    while True:
        codigo = input(
            "Ingrese el código del producto que desea comprar (o 'f' para finalizar): ")
        if codigo == 'f':
            break

        with open("almacen.txt", "r") as f:
            lineas = f.readlines()

        encontrado = False
        for linea in lineas:
            campos = linea.strip().split(":")
            if campos[0] == codigo:
                encontrado = True
                nombre = campos[1]
                precio = float(campos[2])
                print(f"Producto seleccionado: {nombre}")
                print(f"Precio: {precio}")
                cantidad = int(
                    input("Ingrese la cantidad que desea comprar: "))
                productos_comprados.append((nombre, precio, cantidad))
                break

        if not encontrado:
            print("Producto no encontrado.")

    # Guardar la lista de compra en el archivo "factura.txt"
    with open("factura.txt", "a") as f:
        f.write("Resumen de la compra:\n")
        total = 0.0
        for producto in productos_comprados:
            nombre, precio, cantidad = producto
            subtotal = precio * cantidad
            total += subtotal
            f.write(
                f"{nombre}: Precio: {precio:.2f}, Cantidad: {cantidad}, Subtotal: {subtotal:.2f}\n")
        f.write(f"Total a pagar: {total:.2f}\n")

    # Mostrar resumen de la compra
    if productos_comprados:
        print("Resumen de la compra:")
        for producto in productos_comprados:
            nombre, precio, cantidad = producto
            subtotal = precio * cantidad
            print(
                f"{nombre}: Precio: {precio}, Cantidad: {cantidad}, Subtotal: {subtotal}")
        print(f"Total a pagar: {total}")
        confirmar = input("¿Desea confirmar la compra? (s/n): ")
        if confirmar.upper() == "S":
            print("Compra realizada con éxito.")
        else:
            print("Compra cancelada.")
    else:
        print("No se realizaron compras.")


def Modificar_sus_datos():
    username = input("Ingrese el username: ")
    password = input("Ingrese el nuevo password: ")
    with open("usuarios.txt", "r") as f:
        lineas = f.readlines()
    encontrado = False
    with open("usuarios.txt", "w") as f:
        for linea in lineas:
            campos = linea.strip().split(",")
            if campos[0] == username:
                campos[1] = password
                linea = ",".join(campos) + "\n"
                encontrado = True
            f.write(linea)
    if encontrado:
        print("se ha cambiado correctamnente.")
    else:
        print("Usuario no encontrado.")


def ir_main():
    import main
    main()
    

if login():
    while True:
        print("Bienvenido al programa de gestión.")
        print("1. Ver productos")
        print("2. Ver todo productos")        
        print("3. comprar producto")
        print("4. Modificar sus datos")
        print("5. ir main")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            ver_producto()
        elif opcion == "2":
            ver_todo_producto() 
        elif opcion == "3":
            comprar_producto()
        elif opcion == "4":
            Modificar_sus_datos()
        elif opcion == "5":
            ir_main()      
        elif opcion == "6":
            break
        else:
            print("Opción inválida.")
        input("Presione enter para continuar...")
        os.system("clear")

else:
    print("Credenciales inválidas. No puede acceder al programa de gestión.")
