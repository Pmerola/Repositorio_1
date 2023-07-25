#Escribir un programa que pida al usuario un número entero positivo 
#y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas

numero_ingresado = int(input("Ingrese un valor: "))

while numero_ingresado < 0:
    numero_ingresado = int(input("ERROR,el numero ingresado no es valido, ya que no es positivo , vuelva a ingresar el valor: "))
print("Numero valido")

contador = numero_ingresado

while contador > -1 :
    print(contador)
    contador = contador -1