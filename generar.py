#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 21:46:59 2020

@author: jose
"""
from random import choice, randint
from pprint import pprint
import os

file = open("/home/jose/proyectos/oldstuff/curso/data/abonados.txt", "r")
lista_abonados = file.read()
file.close()
lista_abonados = lista_abonados.split(";")
lista_abonados = lista_abonados[0:int(len(lista_abonados) / 2)]
abonados = [a for a in map(lambda x: x.split(","), lista_abonados)]
cabecera="receptor,emisor,fecha"
fechas = []
for i in range(1,31):
    fechas.append(f'{i:02}/06/2019')
pprint(fechas)
llamadas = [cabecera]
for fecha in fechas:

    for i in range(1,randint(800,1000)):
        nombre1, telefono1 = choice(abonados)
        nombre2, telefono2= choice(abonados)
        llamadas.append(telefono1+","+telefono2+","+fecha)
pprint(llamadas)

file = open("/home/jose/proyectos/oldstuff/curso/data/registro_llamadas.txt", "w+")
texto = "\n".join(llamadas)
file.write(texto) 
file.close()