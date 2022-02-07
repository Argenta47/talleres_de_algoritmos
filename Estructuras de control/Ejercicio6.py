"""
Datos de entrada
número de hombres-->n_hombres-->int
número de mujeres-->n_mujeres-->int
Datos de salida
total-->t-->int
porcentaje de hombres-->ph-->float
porcentaje de mujeres-->pm-->float
"""
#Entradas
n_hombres=int(input("Digite el número de hombres: "))
n_mujeres=int(input("Digite el número de mujeres: "))
#Caja negra
t=n_hombres+n_mujeres
ph=(n_hombres*100)/t
pm=(n_mujeres*100)/t
#Salidas
print(f"El porcentaje de hombres es: {ph}")
print(f"El porcentaje de mujeres es: {pm}")
