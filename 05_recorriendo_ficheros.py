# -*- coding: utf-8 -*-

#%% 4 tipos de ficheros de datos
# CSV

#%% Json 

#%% 
import json

file = open("/home/jose/proyectos/oldstuff/curso/data/pharma_data.json", "r")
text_data = file.read()
pharma_data = json.load()
