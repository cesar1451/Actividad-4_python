import os

while True:
    print("Signo Zodiacal dependiendo del día y mes de nacimiento.\n")
    
    dia = int(input("Ingresa el dia (1-31): "))
    while(dia<0 or dia>31):
        print("Día incorrecto, debe de estar entre 1-31.")
        dia = int(input("Ingresa el dia: "))
    mes = int(input("Ingresar el mes (1-12): "))
    while(mes<0 or mes>12):
        print("Mes incorrecto, debe de estar entre 1-12.")
        mes = int(input("Ingresar el mes (1-12): "))
    
    if ((dia>=20 and mes==1) or (dia<=18 and mes==2)):
        print("\nTu signo zodiacal es Acuario.")
    elif ((dia>=19 and mes==2) or (dia<=20 and mes==3)):
        print("\nTu signo zodiacal es Piscis.")
    elif((dia>=21 and mes==3) or (dia<=19 and mes==4)):
        print("\nTu signo zodiacal es Aries.")
    elif((dia>=20 and mes==4) or (dia<=20 and mes==5)):
        print("\nTu signo zodiacal es Tauro.")
    elif((dia>=21 and mes==5) or (dia<=20 and mes==6)):
        print("\nTu signo zodiacal es Géminis.")
    elif((dia>=21 and mes==6) or (dia<=22 and mes==7)):
        print("\nTu signo zodiacal es Cáncer.")
    elif((dia>=23 and mes==7) or (dia<=22 and mes==8)):
        print("\nTu signo zodiacal es Leo.")
    elif((dia>=23 and mes==8) or (dia<=22 and mes==9)):
        print("\nTu signo zodiacal es Virgo.")
    elif((dia>=23 and mes==9) or (dia<=22 and mes==10)):
        print("\nTu signo zodiacal es Libra.")
    elif((dia>=23 and mes==10) or (dia<=21 and mes==11)):
        print("\nTu signo zodiacal es Escorpio.")
    elif((dia>=22 and mes==11) or (dia<=21 and mes==12)):
        print("\nTu signo zodiacal es Sagitario.")
    else:
        print("\nTu signo zodiacal es Capricornio.")
        
    opc=input("\nDeseas saber otro (1-Sí): ")
    os.system("pause") 
    os.system("cls")
    
    if(opc != "1"):
        break