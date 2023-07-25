#Ejercicio 2.1
#Hacer el ejercicio 2 pero usando otra instrucción iterativa.
#Es decir, si en el 2 usaste un while, hacerlo con un for o al revés.

#Escribir un programa que pregunte al usuario su edad
#y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

edad = int(input("Ingrese su edad: "))

contador = 1

while contador < edad:
    print(contador)
    contador +=1

