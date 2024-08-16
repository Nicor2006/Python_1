class contacto:
    def __init__(self,nombre,telefono):
        self.nombre = nombre
        self.telefono=telefono


def mostrar_menu():
    print("Gestion de contactos\n 1.Agregar contacto\n 2.Mostrar contacto\n 3.Buscar contacto\n 4.Eliminat contacto \n 5. Salir" )


contactos = []

while True:
    mostrar_menu()
    opcion = int(input("Elije una opcion: "))

    if opcion == 5:
        print("Saliendo del programa.")
        break

    if opcion == 1:
        nombre = input("Ingrese el nombre: ")
        telefono = input("Ingresa el telefono: ")
        contacto1 = contacto(nombre, telefono)
        contactos.append(contacto1)
        print("Contacto agregado")
    elif opcion == 2:
         for c in contactos:
            print(f'Nombre: {c.nombre}, Telefono {c.telefono}')
    elif opcion == 3:
        nombre = input("Ingrese el nombre a buscar ")
        encontrado = False
        for c in contactos:
            if c.nombre == nombre:
                print(f'Nombre: {c.nombre}, Telefono {c.telefono}')
                encontrado = True
                break
            if not encontrado:
                print("Contacto no encontrado.")
    elif opcion == 4:
        nombre = input("Ingrese el nombre a eliminar ")
        encontrado = False
        for c in contactos:
            if c.nombre == nombre:
                contactos.remove(c)
                encontrado = True
                break
            if not encontrado:
                print("Contacto no encontrado.")
    else:
        print("Opcion no valida")