#Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
#pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario
#coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
#La variable debe ser String, sin usar 'elif'
#Permitirle al usuario ingresar la contraseña inicial.

contrasenia_usuario = input("Ingrese la contrasenia que desee: ")
contrasenia_ingresada = input("Ingrese la contrasenia recientemente creada: ")

if contrasenia_ingresada != contrasenia_usuario:
    print("Contrasenia incorrecta")
else:
    print("Contrsenia correcta")