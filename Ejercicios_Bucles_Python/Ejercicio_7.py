#Ejercicio 7
#El ejercicio 3 de Repaso Condicionales decía:
#"Escribir un programa que pida al usuario dos números y muestre por pantalla su división.
#Si el divisor es cero el programa debe mostrar un error.". Para resolver este ejercicio,
#agregarle al código anterior,
#que vuelva a pedirle al usuario un divisor, hasta que ingrese uno válido.

numero_ingresado = int(input("Ingrese el numero que desee dividir: "))
divisor_ingresado = int(input("Ingrese el numero divisor que desee: "))

while divisor_ingresado == 0:
    divisor_ingresado = int(input("ERROR, el divisor ingresado no es valido, ya que no puede ser 0, por favor vuelva a ingresar el divisor: "))
print("Divisor valido")

resultado = numero_ingresado / divisor_ingresado
print ("El resultado de su division es: ", resultado)