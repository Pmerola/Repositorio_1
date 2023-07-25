#Ejercicio 10
#Realizar un programa para ingresar desde el teclado un conjunto de números y mostrar por pantalla el mayor de ellos.
#Finalizar la lectura de datos con un valor -1.

#Ejemplo, le ingreso los valores 10, 50, 5, 20, -1
#Y debe mostrar que el mayor valor ingresado es 50.

valor_ingresado = 0

valor_mayor = 0

while valor_ingresado != -1:
   valor_ingresado = int(input("Ingrese un valor, para finalizar ingrese -1: "))
   if valor_ingresado != -1:
       if valor_ingresado > valor_mayor:
           valor_mayor = valor_ingresado
           
print("El valor mayor es: ", valor_mayor)
    