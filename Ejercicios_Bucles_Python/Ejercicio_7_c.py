#Ejercicio 7
#Una determinada persona, clasifica los celulares según su precio, en diferentes categorías:

#Intervalo de valor
#Categoría
#Menos de 10.000$
#Barato
#Entre 10.000$ y 100.000$
#Caro
#Entre 100.000$ y 250.000$
#Muy Caro
#Más de 250.000$
#Impagable


#Escribir un programa que pregunte al usuario el valor del celular y muestre por pantalla
#la categoría a la que pertenece.

valor_usuario = int(input("Ingrese el valor que esta dispuesto a pagar por el producto: "))

if valor_usuario < 10000:
    print("El producto es cosiderado Barato")

if valor_usuario > 10000 and valor_usuario < 100000:
    print("El producto que esta disouesto a pagar es Caro")

if valor_usuario > 100000 and valor_usuario < 250000:
    print("El producto que esta dispuesto a pagar es considerado Muy Caro")

if valor_usuario > 250000:
    print("El producto que esta dispuesto a pagar es cosiderado Impagable")
    