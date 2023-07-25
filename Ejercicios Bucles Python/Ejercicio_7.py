#Ejercicio 7
#El ejercicio 3 de Repaso Condicionales decía:
#"Escribir un programa que pida al usuario dos números y muestre por pantalla su división.
#Si el divisor es cero el programa debe mostrar un error.". Para resolver este ejercicio, agregarle al código anterior,
#que vuelva a pedirle al usuario un divisor, hasta que ingrese uno válido.


numero_ingresado = int(input("Ingrese un valor: "))
divisor = int(input("Ingrese el numero divisor: "))

while divisor == 0:
    divisor = int(input("ERROR, el divisor ingresado no puede ser 0, por favor vuelva a ingresarlo: "))
print("Divisor valido")

resultado = numero_ingresado / divisor
print("El resultado de su division es:",resultado)






