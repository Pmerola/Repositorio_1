#Ejercicio 5
#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos
#iguales o superiores a 1000 € mensuales.
#Escribir un programa que pregunte al usuario
#su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

edad_ingresada = int(input("Ingrese su edad: "))

if edad_ingresada > 16:
    print("Usted es mayor de 16 años, puede tributar")

    ingresos_mensuales = int(input("Ingrese el valor de sus ingresos mensuales: "))

    if ingresos_mensuales >= 1000:
        print("Usted debe tributar")
    else:
        print("Usted no puede tributar, ya que sus ingrsos mensuales no son suficientes")
else:
    print("Usted es menor de edad, no tiene derecho a tributar")
