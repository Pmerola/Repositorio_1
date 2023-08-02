#Ejercicio 4.1
#Escribir un programa que pida al usuario un número entero positivo 
#y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas
#Utilizar bucle while

numero_ingresado = int(input("Ingrese un numero entero positivo: "))

contador = numero_ingresado

while contador > 0:
    print(contador)
    contador = contador - 1