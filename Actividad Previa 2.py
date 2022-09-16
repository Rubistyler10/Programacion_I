###########################################################################
#Este es el código escrito para los ejercicios de la Actividad Previa 2
#No todos los Ejercicios requieren código per se
###########################################################################
#EJERCICIO 38
print('Ejercicio 38')
from math import sqrt

lado_A = int(input('Introduce el primer lado del triángulo: '))
lado_B = int(input('Introduce el segundo lado: '))
lado_C = int(input('Introduce el tercer lado: '))

perimetro = lado_A + lado_B + lado_C

semi_perimetro = perimetro/2
area = sqrt(semi_perimetro*(semi_perimetro-lado_A)*(semi_perimetro-lado_B)*(semi_perimetro-lado_C))

print(('El perímetro del triángulo es {0} y el área es {1}').format(perimetro, area))
print('''Fin del ejercicio 38
########################################################################################''')

#EJERCICIO 41
print('Ejercicio 41')

nombre = input('Introduce un nombre: ')
print((nombre + ' ')*1000)
print('''Fin del ejercicio 41
#########################################################################################''')
