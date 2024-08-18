class Tarea:
    def __init__(self, titulo, descripcion, estado):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado

def mostrar_menu():
    print("\n Gestion de tareas\n 1.Agregar nueva tarea\n 2.Mostrar todas las tareas\n 3.Buscar tarea por titulo\n 4.Actualizar estado a completado \n 5.Eliminar el tarea \n 6.Salir \n" )

Lista_Tarea = []

while True:
    mostrar_menu()
    opcion = int(input("Elije una opcion: "))

    if opcion == 6:
        print("Saliendo del programa.")
        break

    if opcion == 1:
            titulo = input("Ingrese el titulo de la tarea: ")
            descripcion = input("Ingresa la descripcion de la tarea: ")
            estado = "pendiente"
            tarea = Tarea(titulo, descripcion, estado)
            Lista_Tarea.append(tarea)
            print("Tarea agregada")
    elif opcion == 2:
        if len(Lista_Tarea) !=0:
             for c in Lista_Tarea:
                print(f'Titulo: {c.titulo}, Descripcion {c.descripcion}, Estado {c.estado}')
        else:
             print("Ninguna tarea encontrada")            
    elif opcion == 3:
        if len(Lista_Tarea) !=0:
            titulo = input("Ingrese el titulo a buscar ")
            encontrado = False
            for c in Lista_Tarea:
                if c.titulo == titulo:
                    print(f'Titulo: {c.titulo}, Descripcion {c.descripcion}, Estado {c.estado}')
                    encontrado = True
                break
            if not encontrado:
                print("Tarea no encontrado.")
        else:
            print("No hay tareas para buscar en la lista")        
    elif opcion == 4:
        if len(Lista_Tarea) !=0:
            titulo = input("Ingrese el titulo de la tarea a actualizar el estado ")
            encontrado = False
            for c in Lista_Tarea:
                if c.titulo == titulo:
                    c.estado = "completado"
                encontrado = True
                break
            if not encontrado:
                print("Tarea no encontrado.")
        else:
            print("No hay tareas en la lista")                
    elif opcion == 5:
        if len(Lista_Tarea) !=0:
            titulo = input("Ingrese el titulo a eliminar ")
            encontrado = False
            for c in Lista_Tarea:
                if c.titulo == titulo:
                    Lista_Tarea.remove(c)
                    encontrado = True
                    break
            if not encontrado:
                print("Tarea no encontrado.")
        else:
            print("No hay tareas en la lista")
    else:
        print("Opcion no valida")