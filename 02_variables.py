# -*- coding: utf-8 -*-

"""
VARIABLES DE TIPO TEXTO
"""

#%% Las cadenas de texto van entrecomilladas

cadena1 = "esto es una cadena de texto"
cadena2 = 'esto es otra cadena de texto'
cadena3 = """
esta es una cadena de texto
en la que meto saltos de línea
como si no hubiera un mañana

"""
#%%
# Es necesario poner comillas para declarar una cadeana de texto
cadena_invalida = no puedo poner un texto sin comillas

#%%
#incluso aunque sea una sola palabra
variable = valor

#%%
# Las comilllas pueden ser dobles o simples
# en Python da igual
variable_dobles = "valor"
variable_simple = 'valor'

#%%
# Pero tienes que ser consistente. Si empiezas por dobles
# acaba también con dobles (y con simples igual)
variable_mezclum = "esto se va a romper'


#%%
# Pero si qye puedes encerrar un tipo de comillas en otras
variable_encerrada = "esto 'no' se rompe"
print(variable_encerrada) 
#%%
variable_encerrada = 'esto "tampoco" se rompe'
print(variable_encerrada) 

#%%
# Formateo de cadenas

inicio_saludo = "Hola"
final_saludo = "Mundo"

print(inicio_saludo)
print(final_saludo)
#%%
# Formatos con PRINT
print(inicio_saludo + final_saludo)

#%%
# Concatenar con el símbolo más es un clásico
# aunque da muchos problemas
print("¡" + inicio_saludo + " " + final_saludo + "!")

#%%
# La aproximación del SXXI es usar interpolación de cadenas
print("¡{} {}!".format(inicio_saludo, final_saludo))

#%%
# Esto es algo más moderno, y solo podrás hacerlo en las últimas versiones
# de Python
print(f"¡{inicio_saludo} {final_saludo}!")


#%%
# EJERCICIO:
# Declara una variable con tu nombre y otra con tu apellido; 
# y haz que se imprima en la pantalla un saludo usando esas variables.

#%%
# Los métodos son acciones que pueden hacer las cadenas. Por ejemplo,
# se pueden pasar a mayúsculas
print(inicio_saludo.upper())

#%%
# Para usar un método, no tienes por que usar la cadena en una variable
print("hola".upper())

#%%
# Algunos métodos de las cademas

print("hola".upper())
print("HOLA".lower())
print("alejandro fernandez".capitalize())
print("alejandro fernandez".replace("o","i"))
print("alejandro fernandez".replace("alejandro","ramiro"))
print(" alejandro fernandez ".strip())
#%%
#Algunos métodos nos permiten saber qué hay dentro de la cadena
print("12".isnumeric())
print("HOLA".isupper())
print("HOLA".islower())
print("hola".isalnum())
print("hola!".isalnum())

#%% Los métodos se pueden encadenar:
print(" hola ".strip().capitalize().replace("la","lita"))


#%%
# EJERCICIO: 
# usando métodos de cadenas, y la variable "texto", haz que se imprima
# Buenos días "profesor" Falken.
# Truco: puedes reemplazar una cadena de texto por ... ¡nada en absoluto! 
texto = "BUENAS NOCHES ---PROFESOR FALKEN ."
print(texto)

#%%
"""
VARIABLES NUMÉRICAS: ENTEROS

"""
#%%
# Variables numéricas
uno = 1
dos = 2

print(uno + dos)

#%%
# Escrbir variables numéricas
print("1" + 2)
#%%
print(str(1) + "2")
#%%
print(1 + int("2"))
#%%
# ¿Por qué es necesario comvertir?
# Por que los números no tienen los métodos de las cadenas
uno = 1
uno.replace(1,3)
#%%
# ni las cadenas tienen las operaciones de los números
# La siguiente expresión ni siquiera tiene sentido
hola="Hola"
mundo="Mundo"
hola/mundo

#%%
# Saber el tipo de una variable.
print(type(uno))
print(type(inicio_saludo))
print(isinstance(inicio_saludo, str))

#%%
# Más sobre números:
a = 1
b = 2

print(a + b)
print(a - b)
print(a * b)
print(b ** b)
print(a / b)
print(a // b)
print(a % b)

#%% 
# Los decimales:
import math
print(math.pi)
print(type(math.pi))
print(isinstance(math.pi, float))

#%%
# Convirtiendo
c = "0,5"
d = 0.5
print(c + str(d))
#%%
# Esto dará error
print(float(c)+ d)

#%%
# Para corregirlo hay que usar un punto
c = "0.5"
print(float(c)+ d)

#%%
# Errores de precision y redondeo
a = 0.1
b = 0.2
print(a+b)
# Explicación
# http://effbot.org/pyfaq/why-are-floating-point-calculations-so-inaccurate.htm
#%%
# ¿Cómo lo solucionamos?
from decimal import Decimal
a = Decimal("0.1")
b = Decimal("0.2")
print(a + b)

#%%
# PROBLEMAS COMUNES CON EL FORMATO DE LOS DECIMALES
# Imprimir solo dos decimales
print("{0:.2f}".format(math.pi))

#%%
# Parsear e imprimir en formato español
# EL formato de estos números es el americao (sin separador de millar, y con punto como separador decunal)
numero_largo = 2345678.5
print(f"{numero_largo}")

#%%
# ¿Como hacermos para imprimirlo en formato español?
# La librería precargada babel nos ahorra trabajo:
from babel.numbers import format_decimal
print(format_decimal(numero_largo, locale='ES_es'))

#%%
# ¿Y para leerlo del formato español?
# Esto dará error por el formato
numero = Decimal("2.231.099,12")

#%%
# Python espera el formato americano
numero = Decimal("2231099.12")
print(numero)
#%%
# Muchas veces leyendo ficheros de excel tendremos el formato español
# así que es importante poder leerlo correctamente.
# La manera buena es usar babel
from babel.numbers import parse_decimal
numero = parse_decimal('2.231.099,12', locale='es_ES')
print(numero)

#%% EJERCICIO
# Calcula el 30% de la variable "numero",
# y muestra el resutado en formato español
numero="3.456.134,12"


#%% Variables de tipo BOOL
# SIEMPRE DAN VERDADERO (True) O FALSE (False)
es_de_dia = True
print(es_de_dia)

#%% Condiciones:
# Las condiciones son una expresión que devuelven verdadero o false
# Y como tal pueden almacenarse en una variable
variable = "valor"
condicion = (variable == "valor")
print(condicion)

#%% Sin los paréntesis es igual pero se lee peor
condicion = variable == "valor"
print(condicion)

#%% algunas condiciones básicas
# La palabra reservada "in" es muy util tambien
contiene_v = ("v" in "valor")
print(contiene_v)

#%%
# Sirve con cadenas más largas
es_alejandro = ("alejandro" in "alejandro fernandez")
print(es_alejandro)

#%%
# Recordad que estamos usando valores directamente, pero es lo mismo
# que si lo almacenásemos en una variable
nombre = "alejandro fernandez"
es_alejandro = ("alejandro" in nombre)
print(es_alejandro)

#%% 
# Otras condiciones posibles: 
igual_alejandro_fernandez = (nombre == "alejandro fernandez")
distinto_alejandro_fernandex = (nombre != "alejandro fernandez")
igual_arturo = (nombre == "arturo")

print(f"Es exactamente alejandro fernandez? {igual_alejandro_fernandez} ")
print(f"Es distinto de alejandro fernandez? {distinto_alejandro_fernandex}")
print(f"Es arturo? {igual_arturo}")

#%% 
# ¿Y las mayúsculas?
igual_alejandro_fernandez = (nombre == "ALEJANDRO FERNANDEZ")
print(f"Es ALEJANDRO FERNANDEZ? {igual_alejandro_fernandez} ")

#%% 
# Las condiciones también se pueden aplicar a los números, con otros operadores
diez = 10
cinco_menor_que_diez = (5 < 10)
print(f"cinco menor que diez {cinco_menor_que_diez}")

#%%
# Un truco: puedes meter expresiones simples entre las llaves del printf
print(f"cinco menor que diez {5 < 10}")

#%% 
#Sabiendo esto, aqui van unas cuantas condiciones con números:
diez = 10
print(f"{5 == diez}")
print(f"{5 != diez}")
print(f"{5 > diez}")
print(f"{10 >= diez}")
print(f"{10 <= diez}")

#%%
# Por supuesto puedes almacenar todas estas expresiones en variables
diez_mayor_igual_diez = (10 >= 10)
print(f"{diez_mayor_igual_diez}")

#%% 
# Una palabra sobre los varoles vacíos
vacio = None

esta_vacio = vacio is None
print(esta_vacio)

#%%
# No se pueden hacer muchas cosas con None
# Cualquier operacion de cadena o numerica con None dará error
None + 1
None.isnumeric()

