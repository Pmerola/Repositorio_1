#Ejercicio 5
#El ejercicio 1 de Repaso Condicionales decía algo similar a:
#"Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
#Si la edad del usuario es negativa, o mayor a 125, es una edad inválida.".
#Para resolver este ejercicio, agregarle al código anterior,
#que vuelva a pedirle la edad hasta que ingrese una que sea válida.

edad_ingresada = int(input("Ingrese su edad: "))

while edad_ingresada < 0 or edad_ingresada > 125:
    edad_ingresada = int(input("ERROR, edad invalida, porfavor vuelva a ingresarla: "))
print("Edad valida")

while edad_ingresada > 18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")


        