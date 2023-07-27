##Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
#pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida
#por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

contrasenia = "Regatas7"
contrasenia_ingresada = input("Ingrese la contrasenia: ")

if contrasenia_ingresada != contrasenia:
    print("Contrasenia incorrecta")
else:
    print("Contrsenia correcta")