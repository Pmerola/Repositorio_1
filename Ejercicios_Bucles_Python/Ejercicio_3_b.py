#Ejercicio 3
#Escribir un programa que pida al usuario un número entero positivo
#y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

numero_ingresado = int(input("Ingrese un numero entero positivo: "))

if numero_ingresado % 2 == 0:
    for i in range(1,numero_ingresado):
        print(i)
else:
    print("El numero ingresado es impar")
