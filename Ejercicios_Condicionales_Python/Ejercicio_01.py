##Ejercicio 1
#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
#Si es probable que el usuario se haya equivocado en el input, permitirle volver a ingresar la edad una vez más,
#antes de indicar si es o no mayor de edad. Pista: Reorganizar los condicionales.

edad_ingresada = int(input("Ingrese su edad: "))

if edad_ingresada < 0 or edad_ingresada > 125:
    edad_ingresada = int(input("ERROR, edad invalida, vulva a ingresarla: "))

if edad_ingresada >= 17:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")