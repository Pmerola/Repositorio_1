#Ejercicio 3.1
#Hacer el ejercicio 3 pero usando otra instrucción iterativa.
#Es decir, si en el 3 usaste un while, hacerlo con un for o al revés.

#Escribir un programa que pida al usuario un número entero positivo
#y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

numero_ingresado = int(input("Ingrese un numero entero positivo: "))

contador = 1

if numero_ingresado % 2 == 0:
    while contador < numero_ingresado:
        print(contador)
        contador += 1
else:
    print("El numero ingresado es impar")
    