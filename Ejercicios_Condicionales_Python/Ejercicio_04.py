##Ejercicio 4
#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
#Pista: Operador módulo. Resto de la división entera. %

numero_ingresado = int(input("Ingrese un numero: "))

if numero_ingresado % 2 == 0:
    print("El numero ingresado es Par")
else:
    print("El numero ingresado es Inpar")