pin_correcto = 4321 

cant_intentos = 0
cant_maximo = 3

while cant_intentos < cant_maximo:
    entrada = input("ingresè clave de 4 digitos: ")
    salida = int (entrada)

    if  salida == pin_correcto:
      print("acceso cocedido")
      break

    else:

       print("pin incorrecto")
       cant_intentos += 1

if cant_intentos == cant_maximo:
    print("tarjeta bloqueada")