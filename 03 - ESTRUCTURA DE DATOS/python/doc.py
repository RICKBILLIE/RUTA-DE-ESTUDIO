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

"""
DICCIONARIO
"""
my_dict: dict = {
    "name": "Brais",
    "surname": "Moure",
    "alias": "@mouredev",
    "age": "36"
}

#AGREGAR
my_dict["email"] = "mouredev@gmail.com"  # Inserción
print(my_dict)

# Eliminación
del my_dict["surname"]  
print(my_dict)

# Acceso
print(my_dict["name"])  

# Actualización
my_dict["age"] = "37"  
print(my_dict)

# Ordenación
my_dict = dict(sorted(my_dict.items()))  

#Devuelve pares clave-valor como tuplas
print(my_dict)
print(type(my_dict))