#Ejercicio 3.1
#Hacer el ejercicio 3 pero usando otra instrucción iterativa.
#Es decir, si en el 3 usaste un while, hacerlo con un for o al revés.

#Escribir un programa que pida al usuario un número entero positivo
#y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.


    
numero_ingresado = int(input("Ingrese un valor: "))

if numero_ingresado < 0:
    print("ERROR, numero invalido")
else:
    print("Numero Valido")
    
    contador = 1

    while contador < numero_ingresado:
        if contador % 2 == 0:
            print(contador)

        contador = contador + 1



