#Ejercicio 6
#El ejercicio 2 de Repaso Condicionales decía:
#"Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
#pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario
#coincide con la guardada en la variable.
#". Para resolver este ejercicio, agregarle al código anterior,
#que vuelva a pedirle al usuario la contraseña hasta que ingrese la correcta.

contrasenia = "pablo123"

contrasenia_ingresada = input("Ingrese la contrasenia: ")

while contrasenia_ingresada != contrasenia:
    contrasenia_ingresada = input("ERROR, contrasenia incorrecta, vuelva a ingresarla: ")
print("Contrasenia correcta")

        



         
    
    
        