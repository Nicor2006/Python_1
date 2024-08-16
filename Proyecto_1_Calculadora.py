def Suma(a, b):
    return a + b
def Resta(a, b):
    return a - b
def Multiplicacion(a, b):
    return a * b
def Division(a, b):
    if b!=0 :
        return a / b
    else :
        return print("Operacion no valida, intentando dividir por 0")



print("Te doy la bienvenida a la calculadora basica")
Num1 = float(input("Ingrese el numero 1 "))
Num2 = float(input("Ingrese el numero 2 "))

print("Ahora que operacion quieres hacer \n 1: Suma \n 2: Resta \n 3: Multiplicacion \n 4: Division \n 5: Salir")

while True:
    opcion = int(input("Elije una opcion "))
    if opcion == 5:
        print("Saliendo del programa, gracias por usarlo")
        break
    
    if opcion == 1:
        print("El resultado de la suma es " + str(Suma(Num1,Num2)))
    elif  opcion == 2:
        print("El resultado de la resta es " + str(Resta(Num1,Num2)))
    elif  opcion == 3:
        print("El resultado de la multiplicacion es " + str(Multiplicacion(Num1,Num2)))
    elif  opcion == 4:
        print("El resultado de la division es " + str(Division(Num1,Num2)))
    else:
        print("Opcion no existente, intente \n 1: Suma \n 2: Resta \n 3: Multiplicacion \n 4: Division \n 5: Salir")
        