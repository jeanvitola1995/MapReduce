
from collections import Counter

""" 
https://www.learnpython.org/en/Map%2C_Filter%2C_Reduce
https://github.com/alkemyTech/OT281-python/blob/main/bigdata/src/F_top10_fechas_menor_post.py

https://github.com/alkemyTech/OT281-python/blob/main/bigdata/src/F_tiempo_rta_promedio.py <-- Tiempo de respuesta promedio
Map,filter and reduce functions

--> Son paradismas de la programación funcional. permiten escribir un código mas simple y corto
sin necesidad de preocuparse por complejidades como bucles y bifurcaciones 


Map
the Map() 

map(func, *iter )

func, es la función donde se aplicará cada elemento
iterm significa que puede haber tanto iterables como sea posible 

--> en python2 map() devolvia una lista, En python3, sin embargo de la
la función devuelve un "map object" generador. Para obtener el resultado como una lista,
"list()", por lo cual se tiene que llamar la función integrada en el objeto map 

--> list(map(func, *iter))
--> El numero de argumentos a "func" debe ser igual de "iterables" enumerados

Digamos que tengo una lista ( iterable) de los nombres de mis mascotas favoritas, todos en minúsculas
y los necesito en mayúsculas. Tradicionalmente, en pythoning normal, haría algo como esto:


Que luego daría salida['ALFRED', 'TABITHA', 'WILLIAM', 'ARLA']
Con map()funciones, no solo es más fácil,
 sino que también es mucho más flexible. Simplemente hago esto:
"""


my_pets = ['alfred', 'tabitha', 'william', 'arla']
uppered_pets = []

for pet in my_pets:
    pet_ = pet.upper()
    uppered_pets.append(pet_)

print(uppered_pets)

# Python 3
my_pets = ['alfred', 'tabitha', 'william', 'arla']

uppered_pets = list(map(str.lower, my_pets))

print(uppered_pets)

""" 
para consolidad nuestro conocimiento en la función map(), la usaremos para implementar nuestra
propia función Zip() personalizada. La función Zip() es una función que toma una cantidad de iterables y luego
crea una tupla que contiene cada uno de los elementos en los iterables. Al igual que map()  , en Python 3
devuleve un objeto generador, que se puede convertir facilmente en una lista llamando la función lista
integrada en él.
"""
# Python 3

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]

results = list(zip(my_strings, my_numbers))

print(results)


""" 
REDUCE Functions 

 reduce aplica una función "de dos argumentos" acumulativamente a los elementos de un iterable,
 comenzando opcionalmente con un argumento inicial.
 
 reduce(func, *iter[, initial])

Donde func es la función en la que *iter se aplica de forma acumulativa a cada elementos del iterable
y "initial" es el valor que se coloca antes de los elementos del iterable en el cálculo, y sirve como
valor predeterminado cuando el iterable está vacío.Debe tenerse en cuenta lo siguiente sobre reduce() : 

-> 1. la func requiere dos argumentos, el primero es el elemento iterable
->
->
->

"""
# Python 3
from functools import reduce

numbers =[({ '2010-10-14': 11}), Counter({'2010-10-15': 50}), Counter({'2010-10-16': 34, '2010-10-15': 16}), Counter({'2010-10-16': 32, '2010-10-17': 18}), Counter({'2010-10-17': 26, '2010-10-18': 24}), Counter({'2010-10-18': 44, '2010-10-19': 6}), Counter({'2010-10-19': 50}), Counter({'2010-10-20': 28, '2010-10-19': 22}), Counter({'2010-10-20': 50}), Counter({'2010-10-21': 40, '2010-10-20': 10}), Counter({'2010-10-21': 28, '2010-10-22': 22}), Counter({'2010-10-22': 50}), Counter({'2010-10-23': 49, '2010-10-22': 1}), Counter({'2010-10-24': 50}), Counter({'2010-10-25': 45, '2010-10-24': 5}), Counter({'2010-10-25': 48, '2010-10-26': 2}), Counter({'2010-10-26': 50}), Counter({'2010-10-26': 33, '2010-10-27': 17}), Counter({'2010-10-27': 50}), Counter({'2010-10-27': 40, '2010-10-28': 10}), Counter({'2010-10-28': 50}), Counter({'2010-10-28': 27, '2010-10-29': 23}), Counter({'2010-10-29': 38, '2010-10-30': 12}), Counter({'2010-10-30': 46, '2010-10-31': 4}), Counter({'2010-10-31': 45, '2009-01-03': 4, '2010-10-30': 1}), Counter({'2010-10-31': 24})]

def date_adder(data1, data2):
    data1.update(data2)
    return data1
reduced = reduce(date_adder, numbers)
print(reduced)

"""
reduce() toma el primer y segundo elemento  de la lista "numbers" y los pasa a "custom_sum", este calcula
su suma y le devuelve a reduce, luego este toma ese resultado y lo aplica como el primer elemento a "custom_sum"
y toma el tercer elemento number como el segundo elemento para "custom_sum". Hace esto hasta que  number se agote la lista

"""


"""
chunckify() es una función que fragmenta un archivo en partes iguales teniendo en cuenta el nivel de procesamiento del sistema.
La función devuelve un objeto el cual podemos iterar sobre el,
"""