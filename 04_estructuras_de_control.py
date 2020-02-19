# -*- coding: utf-8 -*-

#%%
# CONDICIONES
# Se usan para ejecutar lineas de código en caso de que se cumpla una condicion
# es decir, que una expresión se evalue como True

vocales = ["a", "e", "i", "o", "u"]
letra = "a"
if letra in vocales:
    print(f"'{letra}' es una vocal")

#%%
# Por ejemplo, este no se cumplirá:
if letra not in vocales:
    print(f"'{letra}' es una consonante")

#%%
# Los 4 espacios de tabulación son fundamentales. Sin ellos, Python no sabe 
# cual es la condición. Esto dará un fallo

if letra not in vocales:
print(f"'{letra}' es una consonante")

#%% Pueden ponerse todas las lineas que se quieran, y las condiciones se
# pueden anidar:
vocales = ["a", "e", "i", "o", "u"]
letra = "a"
if letra in vocales:
    print(f"'{letra}' es una vocal")
    if letra.islower():
        print(f"Además está en minúsculas")

#%% Aunque se prefiere con mucho usar la palabra reservada and para no crear
# anidaciones demasiado complejas

if letra in vocales and letra.islower():
    print(f"'{letra}' es una vocal en minúsculas")

#%%
# Tamién existe la palabra reservada or:
caracter = "2"
if caracter in vocales or caracter.isnumeric():
    print(f"'{caracter}' es una vocal o un número")

#%%
# Si las cosas se vuelven complicadas, usad siempre paréntesis. 
if (caracter in vocales and caracter.islower()) or caracter.isnumeric():
    print(f"'{caracter}' es, o una vocal en minúsculas, o un número")

#%% Si no, os encontraréis rápidamente con código muy difícil de seguir:
# No tiene por que estár mal, pero tendréis que pararos a leerlo

caracter = "3"
lista1 = ["a", "b"]
lista2 = ["b", "c", "d"]
lista3 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
if caracter in lista1 and caracter in lista2 or caracter in lista3:
    print(f"'{caracter}' es, o una vocal en minúsculas, o un número")

# Martin Fowlwer: “Any fool can write code that a computer can understand. 
# Good programmers write code that humans can understand.”


#%%
# Podemos preparar acciones en caso de que la principal no se cumpla:
caracter = "b"
if caracter in vocales:
    print(f"'{caracter}' es una vocal")
else:
    print(f"'{caracter}' es una consonante")

#%%
# También podemos poner, entre medias, más posibilidades:
caracter = "12"
if caracter.isnumeric():
    print(f"'{caracter}' es un numero")
elif caracter in vocales:
    print(f"'{caracter}' es una vocal")
else:
    print(f"'{caracter}' es una consonante")

#%%
# Todas las que queramos:
caracter = "+"
if not caracter.isalnum():
    print(f"'{caracter}' no es alfanumerico")
elif caracter.isnumeric():
    print(f"'{caracter}' es un numero")
elif caracter in vocales:
    print(f"'{caracter}' es una vocal")
else:
    print(f"'{caracter}' es una consonante")

#%%
# ¿Se puede anidar? 
# Se puede anidar

caracter = "+"
if caracter.isalnum():
    if caracter.isnumeric():
        print(f"'{caracter}' es un numero")
    else:
        if caracter in vocales:
            print(f"'{caracter}' es una vocal")
        else:
            print(f"'{caracter}' es una consonante")
else:
    print(f"'{caracter}' no es alfanumerico")

# Pero como veis la legibilidad se pierde.
#%%
# En caso de duda, acudid al zen del python.
import this
# El zen de python es una de esas cosas que hacen del lenguaje algo
# particularmente bien cuidado, un lugar especial

#%%
# Pasado este momento espiritual, sigamos con los bucles
# BUCLES: se usan para navegar por los datos.
for numero in range(10):
    print(numero)

#%%
# Se usan las mismas reglas de anidación
for numero in range(10):
    print(f"{numero} hola")
print("adios")

#%%
# Su utilidad más evidente es en las listas y las tuplas:
lista = ['uno','dos','tres','cuatro','cinco','seis','siete','ocho','nueve','diez']
for elemento in lista:
    print(elemento)

#%% 
# Puedes combinar la potencia de los condicionales con los bucles, 
# por ejemplo, eso te puede permitir filtrar valores:
lista = ['uno','dos','3','cuatro','5','seis','siete','ocho','nueve','10']
numeros = []
for elemento in lista:
    if elemento.isnumeric():
        numeros.append(elemento)
print(numeros)

#%%
# flat is better than nested:
numeros = [elemento for elemento in lista if elemento.isnumeric()]
print(numeros)

#%%
# ¿Por qué esta sintaxis? Por que puedes transformar el elemento 
palabras = [elemento.upper() for elemento in lista if not elemento.isnumeric()]
print(palabras)

#%%
# Esto sería el equivalente:
palabras = []
for elemento in lista:
    if not elemento.isnumeric():
        palabras.append(elemento.upper())
print(palabras)

#%% ¿Cómo haríamos para recorrer un diccionario?
diccionario = {
        "uno": 1,
        "dos": 2,
        "tres": 3
}
for clave in diccionario.keys():
    print(diccionario[clave])

#%% Por ejemplo, podríamos obtener el totol:
total = 0
for clave in diccionario.keys():
    total = total + diccionario[clave]
print(total)

#%% El operador += se usa esactamente para esto:
total = 0
for clave in diccionario.keys():
    total += diccionario[clave]
print(total)

#%% 
# readability counts
total = 0
for valor in diccionario.values():
    total += valor
print(total)

#%% ¿Hay una manera más fácil de hacerlo?
# En python, siempre:
total = sum(diccionario.values())
print(total)

#%%
# ¿Cómo puedo recorrer estructuras más complejas?
# Saquemos una lista de los días soleados en este parte meterologico:
enero = [{'dia': '01/01/2020', 'tiempo': 'soleado'},
 {'dia': '02/01/2020', 'tiempo': 'soleado'},
 {'dia': '03/01/2020', 'tiempo': 'lloviznas'},
 {'dia': '04/01/2020', 'tiempo': 'lluvioso'},
 {'dia': '05/01/2020', 'tiempo': 'soleado'},
 {'dia': '06/01/2020', 'tiempo': 'soleado'},
 {'dia': '07/01/2020', 'tiempo': 'lloviznas'},
 {'dia': '08/01/2020', 'tiempo': 'lloviznas'},
 {'dia': '09/01/2020', 'tiempo': 'soleado'},
 {'dia': '10/01/2020', 'tiempo': 'lluvioso'},
 {'dia': '11/01/2020', 'tiempo': 'nuboso'},
 {'dia': '12/01/2020', 'tiempo': 'lluvioso'},
 {'dia': '13/01/2020', 'tiempo': 'lluvioso'},
 {'dia': '14/01/2020', 'tiempo': 'soleado'},
 {'dia': '15/01/2020', 'tiempo': 'soleado'},
 {'dia': '16/01/2020', 'tiempo': 'lloviznas'},
 {'dia': '17/01/2020', 'tiempo': 'lluvioso'},
 {'dia': '18/01/2020', 'tiempo': 'soleado'},
 {'dia': '19/01/2020', 'tiempo': 'soleado'},
 {'dia': '20/01/2020', 'tiempo': 'soleado'},
 {'dia': '21/01/2020', 'tiempo': 'lloviznas'},
 {'dia': '22/01/2020', 'tiempo': 'lluvioso'},
 {'dia': '23/01/2020', 'tiempo': 'nuboso'},
 {'dia': '24/01/2020', 'tiempo': 'soleado'},
 {'dia': '25/01/2020', 'tiempo': 'lluvioso'},
 {'dia': '26/01/2020', 'tiempo': 'soleado'},
 {'dia': '27/01/2020', 'tiempo': 'lluvioso'},
 {'dia': '28/01/2020', 'tiempo': 'lluvioso'},
 {'dia': '29/01/2020', 'tiempo': 'soleado'},
 {'dia': '30/01/2020', 'tiempo': 'lluvioso'}]

dias_soleados = []
for dia in enero:
    if dia['tiempo'] == 'soleado':
        dias_soleados.append(dia['dia'])
print(dias_soleados)