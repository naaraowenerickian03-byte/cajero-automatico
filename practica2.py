pin_correcto = 9876 

cant_intentos = 0
cant_maximo = 3

while cant_intentos < cant_maximo:
    entrada = input("ingrese pin correcto: ")
    salida = int (entrada)

    if  salida == pin_correcto:
      print("caja furte abierta")
      break

    else:

       print("clave incorrecta")
       cant_intentos += 1

if cant_intentos == cant_maximo:
    print("la caja fuerte quedò bloqueada")