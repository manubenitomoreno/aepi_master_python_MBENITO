#Crear nueva lista restando 99 a cada elemento
#filtrar la nueva lista con todos los impares
numeros = [647,912,123,902,498,156,123,148,786,888,1000]
a = list(map(lambda x: x-99,numeros))
print(a)
b = list(filter(lambda x: x % 2 !=0, a))
print(b)