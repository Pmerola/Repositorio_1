#Ejercicio 3
#Escribir un programa que pida al usuario un número entero positivo
#y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

numero_ingresado = int(input("Ingrese un numero positivo: "))

if numero_ingresado < 0:
    print("ERROR, usted ingreso un numero negativo")
else:
    print("Numero ingresado valido")
    
    for i  in range(1,numero_ingresado):
        if i % 2 != 0:
            print(i)
    
    

