#Ejercicio 13
#Realizar un programa para ingresar desde el teclado un conjunto de números
#y mostrar por pantalla la suma de ellos. Finalizar la lectura de datos con un valor -1.

numero_ingresado = 0
acumulador = 0

while numero_ingresado != -1:
    numero_ingresado = int(input("Ingrese un valor, para finalizar ingrese -1: "))
    if numero_ingresado != -1:
        acumulador = numero_ingresado + acumulador
print("La suma de los numeros ingresados es de:",acumulador)
    
        
        
    
    



        
    
        


