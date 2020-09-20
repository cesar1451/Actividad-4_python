import math
import os

def areaCuadrado(lado):
    return lado*lado

def areaTriangulo(base, altura):
    return (base*altura)/2

def areaCirculo(radio):
    return (math.pi * (pow(radio, 2)))

while True:
    print("\tPrograma para calcular áreas de Figuras.\n")
    print("Ingrese la figura a calcular: ")
    print("1 - Cuadrado\n2 - Triángulo\n3 - Circulo\n4 - Salir\n")
    opc = input("Ingrese la opción: ")
    
    if opc == "1":
        lado = float(input("Ingrese el lado: "))
        print("El área del Cuadrado = {:.3f}".format(areaCuadrado(lado)))
    elif opc == "2":
        base = float(input("Ingresa la base: "))
        altura = float(input("Ingresa la altura: "))
        print("El área de Triángulo = {:.3f}".format(areaTriangulo(base, altura)))
    elif opc == "3":
        radio = float(input("Ingrese el radio: "))
        print("El área del Circulo = {:.3f}".format(areaCirculo(radio)))
    elif opc == "4":
        print("Gracias por utilizar el programa, hasta luego...\n")
        break
    else:
        print("Error. No se encuentra la opción elegida.\n")
        
    os.system("pause")
    os.system("cls")                