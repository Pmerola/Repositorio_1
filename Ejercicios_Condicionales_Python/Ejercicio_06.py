#Ejercicio 6
#Ingresar las notas de los dos parciales de un alumno e indicar si promocionó, aprobó o si debe recuperar.
#Informar un error si el valor de alguna nota no está entre 0 y 10.

#-Se promociona cuando las notas de ambos parciales son mayores o iguales a 7.
#-Se aprueba cuando las notas de ambos parciales son mayores o iguales a 4.
#-Se debe recuperar cuando al menos una de las dos notas es menor a 4.

nota_1 = int(input("Ingrese la nota del primer parcial: "))
nota_2 = int(input("Ingrese la nota de su segundo parcial: "))

if nota_1 < 0 or nota_1 > 10:
    print("La nota del primer parcial no es valida")
else:
    print("La nota del primer parcial es valida")

if nota_2 < 0 or nota_2 > 10:
    print("La nota del segundo parcial no es valida")
else:
    print("La nota de su segundo parcial es valida")

if nota_1 >= 7:
    if nota_2 >= 7:
        print("Felicidades, Usted promociona la materia")
else:
    print("Usted no promociona")

if nota_1 >= 4 and nota_1 < 7:
    if nota_2 >= 4 and nota_2 < 7:
        print("Usted aprueba los parciales, pero no promociona la materia, (usted debe rendir el final)")
else:
    print("Usted no aprueba, ya que una de sus notas es menor a 4")

if nota_1 < 4:
    print("Usted debe recueperar el primer parcial")
    if nota_2 < 4:
        print("Usted debe recuperar el sgundo parcial")
