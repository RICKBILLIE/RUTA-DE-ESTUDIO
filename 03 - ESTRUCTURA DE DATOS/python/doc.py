#ESTRUCTURAS DE DATOS
"""
LISTAS
"""

milista:list =["platano","naranja","palta","pera"]
print (milista)

#AGREGAR

milista.append("fresa")
print (milista)

#ELIMINAR

milista.remove("fresa")
print(milista)

#ACTUALIZACIÓN

milista[1] = "manzana"
print (milista)

#ORDENAR

milista.sort()
print (milista)


"""
TUPLAS (SON INMUTABLES, PERO SE PUEDEN CONVERTIR A LISTAS)
"""

mitupla:tuple =("platano","naranja","palta","pera")

#ACCESO
print(mitupla[2])

#AGREGAR 

milist:list = list(mitupla)
milist.append("fresa")

mitupla:tuple = tuple(milist)
milist.clear

print(mitupla)

#ACTUALIZACIÓN
milist:list = list(mitupla)
milist[4]= "toronja"
mitupla:tuple = tuple(milist)
milist.clear

print(mitupla)

#Eliminar
milist:list = list(mitupla)
milist.remove("toronja")
mitupla:tuple = tuple(milist)
milist.clear

print(mitupla)

"""
CONJUNTOS (NO PERMITEN ELEMENTOS DUPLICADOS, SIN INDEXACIÓN)
"""

miset = {"platano","naranja","palta","pera"}

print(miset)

#AGREGAR

miset.add("fresa")
print(miset)
miset.add("fresa")

#ACTUALIZAR

milist:list = list(miset)
milist[4]= "toronja"
miset:set = set(milist)
milist.clear

#ELIMINAR

miset.remove("toronja") 
print(miset)

#ORDENAR

miset = set(sorted(miset)) 

print(miset)

print(type(miset))

