# -*- coding: utf-8 -*-
"""

Simulador de credito 

- Monto del prestamo del carro
- Ingresa tu cuota inicial
- Ingresos mensuales
- Numero de meses del prestamo
- Datos personales 

----------------------------------------

Ingresos mensuales
- 908.526 - 1.000.000 >>>>>>>>>>>>>> 20.000.000
- 1.000.000 - 2.000.000 >>>>>>>>>> 25.000.000
- 2.000.000 - 2.500.000 >>>>>>>>>> 30.000.000
- 2.500.000 - 3.000.000 >>>>>>>>>> 40.000.000
- 3.000.000 - 4.500.000 >>>>>>>>>> 60.000.000
- 4.500.000 o mas >>>>>>>>>>>>>>>> 120.000.000


12 Meses - 1.772.488
	20.000.000 ->>> 100
	21.269.586 ->>> 106.3% /// equivale a un 6.3% de interes total 

	1.269.856
	105.798 de interès cada mes

24 Meses - 936.993
	20.000.000 ->>> 100
	22.487.832 ->>> 112.4% /// equivale a un 12.4% de interes total

	2.500.000 
	104.659 de interes cada mes

36 meses - 659.710

	20.000.000 ->>> 100
	23.749.560 ->>> 118.7% /// equivale a un 18.7% de interes total


48 meses - 521.976

	20.000.000 ->>> 100
	25.054.848 ->>> 125,2% /// equivale a un 25.2% de interes total

60 meses - 440.053

	20.000.000 ->>> 100
	25.054.848 ->>> 132% /// equivale a un 32% de interes total

72 meses - 386.030

	20.000.000 ->>> 100
	27.794.160 ->>> 138.9% /// equivale a un 38.9% de interes total



"""
import sys

print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print("|||||||||||||BIENVENIDO AL SIMULADOR DE CREDITO DE VEHICULO|||||||||||||")
print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print("||||||||||||||||||compra el vehiculo de tus sueños||||||||||||||||||||||")
print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

dp_nombre = str(input("Por favor digita tu nombre y apellido: "))
dp_edad = int(input("Por favor digita tu edad: "))


if dp_edad < 18:
    sys.exit("El credito es solo para mayores de edad")

if dp_edad >= 70:
    sys.exit("El credito es solo para personas entre los 18 y 69 años")

if dp_edad > 18 and dp_edad <= 70:
    dp_salario = int(input("por favor digita tu salario: "))

if dp_salario < 908526:
     sys.exit("Monto no valido, valor minimo de prestamo 1SMLV")

# 908.526 - 1.000.000 >>>>>>>>>>>>>> 20.000.000

if dp_salario > 908526 and dp_salario <= 1000000:
    print("El prestamo podra ser desde 1.000.000 hasta 20.000.000 cop")

# 1.000.000 - 2.000.000 >>>>>>>>>> 25.000.000
if dp_salario > 1000000 and dp_salario <= 2000000:
    print("El prestamo podra ser desde 1.000.000 hasta 25.000.000 cop")

# 2.000.000 - 2.500.000 >>>>>>>>>> 30.000.000

if dp_salario > 2000000 and dp_salario <= 2500000:
    print("El prestamo podra ser desde 1.000.000 hasta 30.000.000 cop")

# 2.500.000 - 3.000.000 >>>>>>>>>> 40.000.000

if dp_salario > 2500000 and dp_salario <= 3000000:
    print("El prestamo podra ser desde 1.000.000 hasta 40.000.000 cop")

# 3.000.000 - 4.500.000 >>>>>>>>>> 60.000.000

if dp_salario > 3000000 and dp_salario <= 4500000:
    print("El prestamo podra ser desde 1.000.000 hasta 60.000.000 cop")

# 4.500.000 o mas >>>>>>>>>>>>>>>> 120.000.000

if dp_salario > 4500000:
    print("El prestamo podra ser desde 1.000.000 hasta 120.000.000 cop")


#####################################################

if dp_salario > 908526:
    credito1 = int(input("Ingrese el valor del vehiculo: "))

while credito1 < 1000000:
    print("El valor no es valido, inserte un valor desde 1'000.000")
    credito1 = int(input("Ingrese el valor del vehiculo: "))


while dp_salario > 908526 and dp_salario <= 1000000 and credito1 > 20000000 or credito1 < 1000000:
    print("Monto no valido - El prestamo podra ser desde 1.000.000 hasta 20.000.000 cop")
    credito1 = int(input("Ingrese el valor del vehiculo: "))
    
while dp_salario > 1000000 and dp_salario <= 2000000 and credito1 > 25000000 or credito1 < 1000000:
    print("Monto no valido - El prestamo podra ser desde 1.000.000 hasta 25.000.000 cop")
    credito1 = int(input("Ingrese el valor del vehiculo: "))


while dp_salario > 2000000 and dp_salario <= 2500000 and credito1 > 30000000 or credito1 < 1000000:
    print("Monto no valido - El prestamo podra ser desde 1.000.000 hasta 30.000.000 cop")
    credito1 = int(input("Ingrese el valor del vehiculo: "))


while dp_salario > 2500000 and dp_salario <= 3000000 and credito1 > 40000000 or credito1 < 1000000:
    print("Monto no valido - El prestamo podra ser desde 1.000.000 hasta 40.000.000 cop")
    credito1 = int(input("Ingrese el valor del vehiculo: "))


while dp_salario > 3000000 and dp_salario <= 4500000 and credito1 > 60000000 or credito1 < 1000000:
    print("Monto no valido - El prestamo podra ser desde 1.000.000 hasta 60.000.000 cop")
    credito1 = int(input("Ingrese el valor del vehiculo: "))

while dp_salario > 4500000 and credito1 > 120000000 or credito1 < 1000000:
    print("Monto no valido - El prestamo podra ser desde 1.000.000 hasta 120.000.000 cop")
    credito1 = int(input("Ingrese el valor del vehiculo: "))

if credito1 > 1000000:
    cuota_inicial = int(input("Ingrese el valor de su cuota inicial: "))

    dinero_a_financiar = credito1 - cuota_inicial

    print("El dinero a financiar sera: ", dinero_a_financiar)

if credito1 > 1000000 and dinero_a_financiar > 1:
    cuotas = int(input("Ingrese el numero de cutas a financiar (12) (24) (36) (48) (60) (72): "))

while credito1 > 1000000 and dinero_a_financiar > 1 and cuotas != 12 and cuotas != 24 and cuotas != 36 and cuotas != 48 and cuotas != 60 and cuotas != 72:
    print("Numero de cuotas no valido")
    cuotas = int(input("Ingrese el numero de cutas a financiar (12) (24) (36) (48) (60) (72): "))

print("Señor(a): ",dp_nombre)

if credito1 > 1000000 and dinero_a_financiar > 1 and cuotas == 12:
    interes12 = (dinero_a_financiar * 106.3)/100
    print("El valor final aproximado a pagar es: ", round(interes12))
    cuota_mensual12 = interes12/12
    print("La cuota mensual aproximada es de: ", round(cuota_mensual12))

if credito1 > 1000000 and dinero_a_financiar > 1 and cuotas == 24:
    interes24 = (dinero_a_financiar * 112.4)/100
    print("El valor final a pagar es: ", round(interes24))
    cuota_mensual24 = interes24/24
    print("La cuota mensual es de: ", round(cuota_mensual24))

if credito1 > 1000000 and dinero_a_financiar > 1 and cuotas == 36:
    interes36 = (dinero_a_financiar * 118.7)/100
    print("El valor final aproximado a pagar es: ", round(interes36))
    cuota_mensual36 = interes36/36
    print("La cuota mensual aproximada es de: ", round(cuota_mensual36))

if credito1 > 1000000 and dinero_a_financiar > 1 and cuotas == 48:
    interes48 = (dinero_a_financiar * 125.2)/100
    print("El valor final aproximado a pagar es: ", round(interes48))
    cuota_mensual48 = interes48/48
    print("La cuota mensual aproximada es de: ", round(cuota_mensual48))

if credito1 > 1000000 and dinero_a_financiar > 1 and cuotas == 60:
    interes60 = (dinero_a_financiar * 132)/100
    print("El valor final aproximado a pagar es: ", round(interes60))
    cuota_mensual60 = interes60/60
    print("La cuota mensual aproximada es de: ", round(cuota_mensual60))
    
if credito1 > 1000000 and dinero_a_financiar > 1 and cuotas == 72:
    interes72 = (dinero_a_financiar * 138.9)/100
    print("El valor final aproximado a pagar es: ", round(interes72))
    cuota_mensual72 = interes72/72
    print("La cuota mensual aproximada es de: ", round(cuota_mensual72))

print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print("||||||||||GRACIAS POR USAR SIMULADOR DE CREDITO DE VEHICULO|||||||||||||")
print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print("||||||||||||||||||compra el vehiculo de tus sueños|||||||||||||||||||||||")
print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")




"""
Fuentes:
https://www.delftstack.com/es/howto/python/how-to-round-to-two-decimals-in-python/
https://www.delftstack.com/es/howto/python/python-exit-program/
https://www.bancodeoccidente.com.co/occiauto/autogestionado

"""