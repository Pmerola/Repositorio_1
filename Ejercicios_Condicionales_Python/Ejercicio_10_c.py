#Ejercicio 10
#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
#El grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior
#a la N y el grupo B por el resto.
#Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla 
#el grupo que le corresponde.

#Ingreso de datos (Nombre y Sexo)
nombre_alumno = input("Ingrese su nombre: ") [0]
sexo_alumno = input("Ingrese su sexo") 

#Seleccion de grupo Mujeres
if sexo_alumno == "Mujer":
    if nombre_alumno > "a" and nombre_alumno < "m":
        print("Usted pertenece al grupo A")
    else:
        print("Usted pertenece al gurpo B")

#Seleccion de grupo Varones
if sexo_alumno == "Varon":
    if nombre_alumno > "n" and nombre_alumno <= "z":
        print("Usted pertenece al grupo A")
    else:
        print("Usted pertenece al grupo B")