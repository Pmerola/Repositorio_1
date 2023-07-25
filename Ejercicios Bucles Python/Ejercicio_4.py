#Ejercicio 4
#Escribir un programa que pida al usuario un número entero positivo 
#y muestre por pantalla la cuenta atrás desde ese número hasta cero 
 
valor = int(input("Ingrese un valor: "))

for i in range(valor, -1 ,-1):
    print(i)