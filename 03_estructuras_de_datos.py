#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 17:45:48 2020

@author: jose
"""

"""
TUPLAS
"""
# Una tupla es una colección de variables de cualquier tipo
tupla = (1, "dos", True)

#%%
# Aunque lo normal es que todos los objetos dentro de la colección sean del 
# mismo tipo, como en este caso, que son variables de tipo texto
tupla = ('uno','dos','tres','cuatro','cinco','seis','siete','ocho','nueve','diez')
#%%
# Puedes acceder los elementos de la tupla por su índice
# EL primer elemento de la tupla está en el índice 0
print(tupla[0])
#%%
# Contando desde cero, accedemos a cualquier elemento
print(tupla[3])
#%%
# Podemos acceder a un rango de elementos
print(tupla[0:3])
print(tupla[2:4])
print(tupla[3:])
#%%
# SI no ponemos nada, cuenta como el elemento 0
print(tupla[:3])
#%% 
# Si es en el segudo índice, es el final
print(tupla[6:])

#%%
# Hay algún truquillo para llegar al final de la tupla
print(tupla[-1])

#%%
# Podemos saber cuanto mide esta tupla
len(tupla)

#%%
# Y también podemos preguntar si hay o no un elemento dentro:
print("diez" in tupla)
print("once" in tupla)

#%%
"""
LISTAS
"""

#%%
# Las tuplas están bien, pero no permiten añadir ni borrar elementos. 
# ¡Se usan a veces! pero con mucha más frecuencia, usarás una lista. 
# Se distingue por que en vez de paréntesis, se usa un corchete cuadraro

lista = ['uno','dos','tres','cuatro','cinco','seis','siete','ocho','nueve','diez']

#%% Y funciona exactamente igual
print(lista[0])
print(lista[3])
print(lista[0:3])
print(lista[2:4])
print(lista[3:])
print(lista[:3])
print(lista[6:])
print(lista[-1])
len(lista)
print("diez" in lista)
print("once" in lista)

#%% con la diferencia de que puedes añadir elementos
print(lista)
lista.append("once")
print(lista)
#%% y eliminarlo!

lista.remove("once")
print("once" in lista)

#%% Si tratas de eliminar un elemento que no existe, python lanzará un error
lista.remove("once")

#%% Puedes eliminar elementos por su índice: 
lista.pop(0)
print("uno" in lista)

#%%
# Puedo obtener una lista de una variable de tipo texto

palabras = "tenedor cuchillo cuchara peine"
print(palabras)
print(palabras.split())

#%%
# Podemos encadenar métodos de string para hacer cosas
# Como eliminar los espacios del principio y del final
palabras = " tenedor cuchillo cuchara peine "
print(palabras.split(" "))
print(palabras.strip().split(" "))

#%%
# Podeis hacer split por casi cualquier caracter
palabras_con_comas = "hola,tengo,varias,palabras"
print(palabras_con_comas.split(","))

#%% 
# Incluso por salto de linea, con el método splitlines
# lo que nos resultará muy util para leer algunos ficheros
cadena = """Hola
tengo
varias
lineas"""
print(cadena.splitlines())

#%% Strip también funcionará con saltos de línea
cadena = """

Hola
tengo
varias
lineas

"""
print(cadena.splitlines())

#%%

print(cadena.strip().splitlines())

#%% 
# Las propias cadenas de texto funcionan como si fueran listas:
# por ejemplo, puedo acceder a sus índices
cadena = "Hola mundo!"
print(cadena[0])
print(cadena[-1])
print(cadena[2:6])

#%% 
# Podemos ordenar las listas:
lista = ["z","g","a","d"]
lista.sort()
print(lista)

#%%
# También numéricamente
lista = [9,4,1,0,100,23]
lista.sort()
print(lista)


#%% 
#Y darle la vuelta
lista.reverse()
print(lista)
#%%
""" 
DICCIONARIOS
"""

#%%
# Los diccionarios asocian una palabra a un valor:

diccionario = {
            "uno": 1,
            "dos": 2,
            "tres": 3
        }
print(diccionario)

#%% 
# En vez de acceder por el índice, accedemos por la palabra
print(diccionario["uno"])

#%%
# Si queremos saber las claves que contiene, debemos usar la palabra keys()
print(diccionario.keys())

#%% Podemos convertir esto en una lista, para acceder a ellos como si fuerann
# los elementos de una lista
claves = list(diccionario.keys())
print(claves[0])

#%% 
# La palabra reservada "in" aquí funciona de manera algo distinta:
# Responde a la pregunta ¿está la palabra en el diccionario?
print("uno" in diccionario)
print(1 in diccionario)

#%% Si queremos saber si un valor está dentro del diccionario, al igual
# que tenemos keys, tenemos values
print(diccionario.values())
#%%
# Igualmente puedes convertirlo en una lista
valores = list(diccionario.values())
print(valores[0])

#%%
# Y así es como puede comprobarse si un valor está dentro de un diccionario
print(1 in diccionario.values())

#%%
"""
ANIDACIÓN DE ESTRUCTURAS
"""

#%% Algo que no solo es común, si no que vosotras mismas querréis hacer
# es anidar estructuras de datos. 
# Por ejemplo:

personas = [
        {"nombre": "Juan", "apellido": "Espadas"},
        {"nombre": "Fernando", "apellido": "Jimenez"}
        ]
print(personas)

#%% Para estos casos el comando print nos puede mostrar cosas muy confusas
# Es mucho mejor pprint, que nos coloca saltos de línea
from pprint import pprint
pprint(personas)

#%%
# COmo veis, hemos creado una lista, y cada elemento de la lista es a su vez un
# diccionario. ¿Como accedo a cada elemento? Pues como si pelase una cebolla
# desde las capas superiores a las inferiores. Empiezo por la lista. 
# personas[0]`deberia darme el primer elemento

print(personas[0])

#%%
# Dentro de ese primer elemento, puedo acceder al diccionario
print(personas[0]["nombre"])

#%% Podríamos querer acceder al segundo elemento:
print(personas[1]["nombre"])

#%%
# Tenemos total libertad de anidación de estos objetos. Por ejemplo, podríamos 
# completar nuestro ejemplo:

personas = [{
     "nombre":"Juan",
     "apellidos":"Espadas",
     "direccion":{
         "fiscal": {
             "calle":"Calle del álamo 12",
             "localidad":"Madrid",
             "provincina":"Madrid",
             "codigoPostal":"28005"
         },
        "postal" : {
             "calle":"Calle del cerezo 15",
             "localidad":"Madrid",
             "provincina":"Madrid",
             "codigoPostal":"28008"
        }
     },
     "telefonos":[
         "212 555-1234",
         "646 555-4567"
     ]
    }, {
     "nombre":"Fernando",
     "apellidos":"Jimenez",
     "direccion":{
         "fiscal": {
             "calle":"Calle del cierzo 110",
             "localidad":"Madrid",
             "provincina":"Madrid",
             "codigoPostal":"28012"
         },
        "postal" : {
             "calle":"Plaza del céfiro 1",
             "localidad":"Madrid",
             "provincina":"Madrid",
             "codigoPostal":"28001"
        }
     },
     "telefonos":[
         "567 555-8765",
         "666 555-5432"
     ]
 }]

#%%
# Fijaos en la diferencia entre pprint y print
print(personas) 
#%%
pprint(personas)    

#%% 
#Solo tenemos que ser conscientes de que cuanto más liemos las cosas, 
# más dificil seránn de leer, y que debemos de buscar estructuras lo más 
# intuitivas posibles:
# Aqui está la dirección de la primera persona

print(personas[0]["direccion"]["postal"]["calle"])
