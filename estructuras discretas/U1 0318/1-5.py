# programa de python de interseccion

s1 = set([4 , 6 , 9])

s2 = set([1 , 6 , 8])

#las 2 formas sirven
print(s1.intersection(s2))

#print(s1 & s2)

s1.intersection_update(s2)

print(s1)