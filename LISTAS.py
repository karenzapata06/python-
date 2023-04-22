"""#se representan con [] las listas
lista = [] #lista vacia
listas = [1, 1.30, "Hola", True, False] #enteros, decimales, string, booleano, cada dato debe ser separado con (,)

#Mutables: modificar
#indexadas

#metodo len(): muestra la longitud de la lista
print(len(listas)) #cantidad de elementos que tiene la lista

#acceder a la lista
print(listas[2]) #se escribe el nombre de la lista y entre [] la posision del objeto que quiere ver
print(listas[-2]) #si se quiere acceder de forma inversa

#modificar elemento
listas[2]="Colecciones"
print(listas)

#recorrer una lista
for elemento in listas:
    print(elemento)
    
#indice (posicion)
for elem in range(len(listas)):
    print(f"{listas[elem]} esta en la posicion {elem}") #recorre rango desde 0
    
#Insertar elementos: insert(posicion, dato o elemento a ingresar),append(dato o elemento a ingresar) ingresa el elemento en la ultima posicion
Marcas_Autos = ["Renault", "Chevrolet", "Suzuki", "Audi", "Kia"]
Marcas_Autos.insert(3, "Mazda") #aca primero se pone la posicion en la que quiere el nuevo elemneto seguido del nombre que quiere agregar
Marcas_Autos.append("Toyota") # el append es para que el elemento agregado quede de ultima posicion
print(Marcas_Autos)

#eliminar elementos
#pop(indica la posicion del elemento que va a eliminar), remove(indica el elemento a eliminar)
Marcas_Autos.pop(4)
print(Marcas_Autos)

#conocer la posicion del elemento:index(elemento)
posicion = Marcas_Autos.index("suzuki")
print(posicion)

#ORGANIZAR LISTA: ascendente sort(),descendente sort(reverse=true)

Marcas_Autos.sort()
print(Marcas_Autos)
Marcas_Autos.sort(reverse=True)
print(Marcas_Autos)

#EXTENDER LA LISTA :extend(lista)
otras_marcas = ["BMW","Ferrari","Tesla","Mercesdes bena"]
Marcas_Autos.extend(otras_marcas)
print(Marcas_Autos) 

#recorrer 2 o mas listas al mismo tiempo 
Animales = ["Gato","Leon","Ballena","Pajaro","Serpiente"]
Tipo_A = ["Terrestre","Salvaje","Mamifero","Aereo","Reptil"]

for Animal,tipo in zip (Animales,Tipo_A):
    print(f"aca los animal {Animal} y el tipos {tipo}")
    
#contar elementos repetidos count(elemento)
numeros = [1,2,3,4,5,1,345,1,45,2,1,1,1,456]
Contar = numeros.count(1)
print(Contar)

#Ejercicio
#Crear 2 listas vacias una llamada tienda, otra llamada precio, el usuario debe ingresar el numero de articulos de la tienda y los elementos de cada lista, estos elementos deben ser agregados a la lista correspondiente. debe mostrar los elementos de la tienda con su respectivo precio. (for o while)"""


tienda = []
precio = []

numarticulos = int(input("Ingrese el número de artículos: "))

for i in range(numarticulos):
    nombrearticulo = input("Ingrese el nombre del artículo: ")
    precioarticulo = int(input("Ingrese el precio del artículo: "))
    tienda.append(nombrearticulo)
    precio.append(precioarticulo)

print("Elementos de la tienda con su respectivo precio:")
for i in range(numarticulos):
    print(tienda[i] + ": $" + str(precio[i]))
