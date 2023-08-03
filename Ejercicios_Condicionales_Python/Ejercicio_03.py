#Escribir un programa que pida al usuario dos números y muestre por pantalla su división.
# Si el divisor es cero el programa debe mostrar un error.

numero = int(input("Ingrese un numero: "))
divisor = int(input("Ingrese el numero divisor: "))

if divisor == 0:
    print("ERROR, el divisor no puede ser 0")
else:
    resultado = numero / divisor
    print("El resultado de su division es:", resultado)