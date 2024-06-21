#Ejercicio de prueba 

import csv, time, os

#Variables
bus = [["0" for x in range(4)] for y in range(7)]


#inicia aquí
print("Bienvenido a la empresa turística 'el busin del chulin'")
time.sleep(2)

while True:
    print("¿Que desea hacer?")
    print("1.- Ver una representación del bus")
    print("2.- Comprar asiento")
    print("3.- Mostrar ventas realizadas")
    print("4.- Salir")
    opc = int(input("Elegir opción: "))

    if opc==1:
        time.sleep(1)
        print("""        Esto muestra como se vería el bus
        para poder elegir su asiento
        (X: Asientos ocupados. 0: Asientos libres)""")
        print(" frente del bus")
        print(" _____________")
        print("|X X   P   0 0|")
        print("|0 X   A   0 0|")
        print("|0 0   S   0 0|")
        print("|0 X   I   0 0|")
        print("|0 0   L   X 0|")
        print("|0 0   L   0 0|")
        print("|0 0   O   0 0|")
        print("|_____________|")
        time.sleep(3)
    elif opc==2:
        print("Seleccione un asiento")
        for f in bus:
            print(f)
    elif opc==3:
        pass
    else:
        pass