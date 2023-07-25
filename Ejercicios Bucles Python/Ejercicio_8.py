#Ejercicio 8
#El ejercicio 5 de Repaso Condicionales decía:
#"Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o 
#superiores a 1000 € mensuales.
#Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y
#muestre por pantalla si el usuario tiene que tributar o no.".
#Para resolver este ejercicio, agregarle al código anterior:
#Validar que la edad ingresada por el usuario esté entre 1 y 125.
#Validar que los ingresos estén entre 0 y 10000.
#Pista: Decir "Validar" o decir, "Volverle a pedir hasta que ingrese un valor correcto" es lo mismo.

edad_ingresada = int(input("Ingrese su edad: "))

while edad_ingresada < 1 or edad_ingresada > 125:
    edad_ingresada = int(input("ERROR, edad invalida, porfavor vuelva a ingresar su edad: "))
print("Edad valida")

if edad_ingresada > 16:
    print("Usted es menor de edad, no puede tributar")
else:
    print("Usted cumple con la edad para tributar")

ingresos_mensuales = int(input("Ingrese sus ingresos mensuales: "))

while ingresos_mensuales < 0 or ingresos_mensuales > 10000:
    print("ERROR, los ingresos son invalidos, por favor vuelva a ingresarlos: ")
print("Ingresos validos")

if ingresos_mensuales >= 1000:
    print("Usted puede tributar")
else: 
    print("Usted no puede tributar, ya que sus ingresos mensuales no superan el monto establecido ")






    
    



    


