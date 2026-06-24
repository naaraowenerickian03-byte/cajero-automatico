continuar = "si"


while continuar=="si":
    edad = int(input("ingrese su edad: "))
    invitacion = input("tiene invitacion: ").lower()
    if edad >= 18 and invitacion == "si": 
    
        print("acceso permitido ")
    else:
        print(" acceso denegado")

    continuar = input("quiere verificar otra persona: ")
print(" programa finalizado")



 
 