#voumen de una esfera en python
import numpy as np

r=2
vol = lambda r : (4./3.)*np.pi*(r**3)
volumen = vol(r)
print(volumen)


#comprension de listas
e = [vol(r) for r in range(10)]
"""la funcion de arriba reemplaza el r en rango de 10,osea del 0 hasta el 9 y hace una lista 
con los resultados , (explicacion detallada con deepseek)"""

e_map = list(map(vol,range(10)))