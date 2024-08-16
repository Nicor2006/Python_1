class producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

def mostrar_menu():
    print("\n Sistema de inventario\n 1.Agregar nuevo producto\n 2.Mostrar todos los productos\n 3.Buscar producto por nombre\n 4.Actualizar cantidad \n 5.Eliminar el producto \n 6.Salir \n" )

Lista_Productos = []

while True:
    mostrar_menu()
    opcion = int(input("Elije una opcion: "))

    if opcion == 6:
        print("Saliendo del programa.")
        break

    if opcion == 1:
        try:
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingresa la cantidad: "))
            precio = int(input("Ingresa el precio: "))
            Producto = producto(nombre, cantidad, precio)
            Lista_Productos.append(Producto)
            print("Producto agregado")
        except:
            print("La cantidad o precio tienen que ser un numero")
    elif opcion == 2:
        if len(Lista_Productos) !=0:
             for c in Lista_Productos:
                print(f'Nombre: {c.nombre}, Cantidad {c.cantidad}, Precio {c.precio}')
        else:
             print("Ningun producto encontrado")            
    elif opcion == 3:
        if len(Lista_Productos) !=0:
            nombre = input("Ingrese el nombre a buscar ")
            encontrado = False
            for c in Lista_Productos:
                if c.nombre == nombre:
                    print(f'Nombre: {c.nombre}, Cantidad {c.cantidad}, Precio {c.precio}')
                    encontrado = True
                break
            if not encontrado:
                print("Producto no encontrado.")
        else:
            print("No hay productos para eliminar en la lista")        
    elif opcion == 4:
        if len(Lista_Productos) !=0:
            nombre = input("Ingrese el nombre del producto a cambiar la cantidad ")
            encontrado = False
            for c in Lista_Productos:
                if c.nombre == nombre:
                    try:
                        Cantidad_Nueva = int(input("Cual es la cantidad a cambiar "))
                        c.cantidad = Cantidad_Nueva
                        print ("Cantidad Actualizada")
                    except:
                        print("La cantidad del producto tiene que ser una cantidad valida")
                encontrado = True
                break
            if not encontrado:
                print("Producto no encontrado.")
        else:
            print("No hay productos para eliminar en la lista")                
    elif opcion == 5:
        if len(Lista_Productos) !=0:
            nombre = input("Ingrese el nombre a eliminar ")
            encontrado = False
            for c in Lista_Productos:
                if c.nombre == nombre:
                    Lista_Productos.remove(c)
                    encontrado = True
                    break
            if not encontrado:
                print("Producto no encontrado.")
        else:
            print("No hay productos para eliminar en la lista")
    else:
        print("Opcion no valida")
    
