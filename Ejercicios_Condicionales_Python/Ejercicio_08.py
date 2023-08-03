##Ejercicio 8
#Una editorial determina el precio de un libro según la cantidad de páginas que contiene.
#El costo básico del libro es de $500, más $3,20 por página con encuadernación rústica.
#Si el número de páginas supera las 300 la encuadernación debe ser en tela, lo que incrementa el costo en $200.
#Además, si el número de páginas sobrepasa las 600 se hace necesario un procedimiento especial de encuadernación 
#que incrementa el costo en otros $336.
#Desarrollar un programa que calcule el costo de un libro dado el número de páginas.

#Ingreso de cantidad de paginas del cliente
cantidad_paginas = int(input("Ingrese la cantidad de paginas de su producto: "))

#Costo basico
costo_basico = 500 + 3.20 

precio_basico = costo_basico + cantidad_paginas

if cantidad_paginas <= 300:
    print("El costo de su libro es de $",precio_basico)

#Costo de mas de 300 paginas
if cantidad_paginas > 300 :
    mas_de_300_pag = costo_basico + 200
    print("El costo de su libro es de $",mas_de_300_pag)

#Costo de mas de 600 
if cantidad_paginas > 600:
    mas_de_600_pag = mas_de_300_pag + 336
    print("El valor  de su libro es de $",mas_de_600_pag)



