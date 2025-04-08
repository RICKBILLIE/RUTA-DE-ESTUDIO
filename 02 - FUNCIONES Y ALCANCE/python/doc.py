def greet ():
    print("Hola, Python!")

greet()

def return_greet ():
    return "Hola, Python"

print(return_greet())

#con argumento

def arg_greet (greet, name):

    print(f"{greet}, {name}")

arg_greet("Hi","andy")

#con arg predetermindado

def def_arg_greet ( name="cliente" ):
                                               
    print(f"hola, {name}")

def_arg_greet()

#con arg y return 

def def_return_arg_greet ( greet , name ):
                                               
    return (f"{greet}, {name}")

print (def_return_arg_greet("hi","brais"))

#con retorno de varios valores

def multiple_return_greet():
    return "hola", "python"

greet, name = multiple_return_greet()
print(greet)
print(name)

#numero de variavbles e argumentos

def var_arg_greet(*names):
    for name in names:
        print(f"hola, {name}!")

var_arg_greet("andy", "ANDU")

#CON UN NUMERO VARIABLE DE ARGUMENTOS CON PALABRA CLAVE

def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"{value} ({key})!")


variable_key_arg_greet(
    language="Python",
    name="Brais",
    alias="MoureDev",
    age=36
)


#Funciones dentro de funciones



def outer_function():
    def inner_function():
        print("Función interna: Hola, Python !")
    inner_function()


outer_function()

#Funciones del lenguaje

print(len("MoureDev"))
print(type(36))
print("MoureDev".upper())

#variables locales y globales

global_var = "Python"


def hello_python():
    local_var = "Hola"
    print(f"{local_var}, {global_var}!")

print(global_var)
# print(local_var) No se puede acceder desde fuera de la función

hello_python()