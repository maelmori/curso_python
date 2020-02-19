"""

Sois detectives de Central City. Han secuestrado al alcalde. Se sabe que el 2 de Junio de 2019 la mujer del alcalde,
llamada Ellen Dolan, recibió una llamada anónima advirtiendo que habían secuestrado a su marido y pidiendo un rescate
ridículamente alto. A lo largo del día habló con esa persona 3 veces. La voz del sospechoso estaba distorsionada. 
Según los expertos de la científica, esa distorsión solo puede realizarse con un programa de audio llamado "Spirit Audiowave".
Ella no sabe qué día secuestraron a su marido por que estaba de viaje desde hace una semana, pero revisando los videos 
de seguridad del ayuntamiento, puede verse a un hombre alto, con traje y enmascarado sacando al alcalde a punta de pistola por la puerta de 
servicio. Por un problema informático, no es posible tampoco saber qué día ocurrió, pero se ve en las 
imágenes que era un día lluvioso.

"""

nombre_a_buscar = "Ellen Dolan"

#%%
# Cual es el teléfono de Ellen Dollan?

file = open("/home/jose/proyectos/oldstuff/curso/data/abonados.txt", "r")
lista_abonados = file.read()
file.close()

print(lista_abonados)

#%%
# Interpolacion de cadenas
# Sintaxis de la palabra reservada in 

esta_ellen = nombre_a_buscar in lista_abonados
print(f"Tenemos el teléfono de Ellen? {esta_ellen}")

#%%
# Tenemos un texto enorme, pero queremos una lista de teléfonos.
# Así que hay que partirlo por los saltos de línea.
# Esto gernea una lista. ¿QUé es una lista?    
from pprint import pprint
lista_abonados = lista_abonados.split(";")
pprint(lista_abonados)


#%%
# ¿Cómo sacamos el número de teléfono de Ellen Dolan?
# Hay que recorrer la lista
# Y, si encontramos que el nombre está dentro del elemento de esa lista,
# lo imprimimos:

telefonos_ellen = [abonado.split(",")[1] for abonado in lista_abonados if nombre_a_buscar in abonado]

        
pprint(telefonos_ellen)
