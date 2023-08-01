#Ejercicio 4
#Escribir un programa que pida al usuario un número entero positivo 
#y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas

numero_ingresado = int(input("Ingrese un numero entero postivo: "))

for i in range(numero_ingresado,0,-1):
    print(i)