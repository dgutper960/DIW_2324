## Diccionarios en Python
###### Obtenido de [*El Libro de Python*](https://ellibrodepython.com/)

Los diccionarios en Python son una estructura de datos que permite almacenar su contenido en forma de llave y valor.

#### Crear Diccionarios Python

Un diccionario en Python es una colección de elementos, donde cada uno tiene una llave ```key``` y un valor ```value```. Los diccionarios se pueden crear con llaves ```{}``` separando con una coma cada par ```key: value```. En el siguiente ejemplo tenemos tres keys que son el nombre, la edad y el documento.

```Python:
d1 = {
  "Nombre": "Sara",
  "Edad": 27,
  "Documento": 1003882
}
print(d1)
#{'Nombre': 'Sara', 'Edad': 27, 'Documento': 1003882}
```

Algunas propiedades de los diccionario en Python son las siguientes:

- Son ***dinámicos***, pueden crecer o decrecer, se pueden añadir o eliminar elementos.
- Son ***indexados***, los elementos del diccionario son accesibles a través del ```key```.
- Son ***anidados***, un diccionario puede contener a otro diccionario en su campo ```value```.
- Las ```key``` son únicas, es decir, no pueden repetirse en un mismo diccionario, y pueden ser de cualquier tipo de datos inmutable.

#### Acceder y modificar Diccionarios

Se puede acceder a sus elementos con ```[]``` o también con la función ```get()```. Lo que se indica dentro de los corchetes es la ```key``` del ```value``` al que queremos acceder.

- Si se intenta acceder a una ```key``` haciendo uso de ```[]``` y dicha clave no existe, se lanzará un ERROR.
- Si se intenta acceder a una ```key``` haciendo uso de ```get()``` y dicha clave no existe, el método devolverá *None*.

```Python:
print(d1['Nombre'])         #Sara
print(d1.get('Nombre'))     #Sara

print(d1['Apellidos'])      #!Error
print(d1.get('Apellidos'))  #None
```

***Ayuda***
Haciendo uso del método *.get()* de los diccionarios podemos saber si dicha clave existe dentro del diccionario o no. Para ello, simplemente hacemos una comprobación con una estructura if, donde comparamos el resultado de acceder a una ```key``` con None. Si el resultado es True, significa que dicha clave no existe en el diccionario.

```Python:
if d1.get('Apellidos') == None:
    print('El elemento no existe')
else:
    print(d1.get('Apellidos'))
```

Como podemos ver en el ejemplo anterior, indicamos la ```key``` *Nombre* para poder acceder a su ```value``` *Sara*

Para modificar un elemento basta con usar ```[]``` con el nombre del ```key``` y asignar el valor que queremos.

```Python:
d1['Nombre'] = "Laura"
print(d1)
#{'Nombre': Laura', 'Edad': 27, 'Documento': 1003882}
```

Si el ```key``` al que accedemos no existe, se añade automáticamente.

```Python:
d1['Direccion'] = "Calle 123"
print(d1)
#{'Nombre': 'Laura', 'Edad': 27, 'Documento': 1003882, 'Direccion': 'Calle 123'}
```

#### Iterar Diccionarios

Los diccionarios se pueden iterar de manera muy similar a las listas u otras estructuras de datos. Para imprimir los key.

```Python:
# Imprime los key del diccionario
for x in d1:
    print(x)
#Nombre
#Edad
#Documento
#Direccion
```

Se puede imprimir también solo el value.

```Python:
# Impre los value del diccionario
for x in d1:
    print(d1[x])
#Laura
#27
#1003882
#Calle 123
```

O si queremos imprimir el key y el value a la vez.

```Python:
# Imprime los key y value del diccionario
for x, y in d1.items():
    print(x, y)
#Nombre Laura
#Edad 27
#Documento 1003882
#Direccion Calle 123
```

#### Métodos Diccionarios

Existen varios métodos asociados a los diccionarios en Python:

- len(d): Devuelve el número de elementos del diccionario d
- d.clear() : Elimina todo el contenido del diccionario
- d.get(\<key>): Nos permite consultar el value para un key determinado.
- d.items(): Devuelve una lista con los keys y values del dicionario. Si se convierte en list se puede tratar como una lista normal.
- d.keys(): Devuelve una lista con todas las keys del diccionario
- d.values(): devuelve una lista con todos los values del diccionario
- d.pop(\<key>): Busca y elimina la key que se le pase por parámetro. Daría un error si se intenta eliminar una key que no existe.
- d.popitem(): Elimina de manera aleatoria un elemento del diccionario.
- d.update(): se llama sobre un diccionario y tiene como entrada otro diccionario. Los value son actualizados y si alguna key del nuevo diccionario no esta, es añadida.

##### clear()
```Python:
d = {'a': 1, 'b': 2}
d.clear()
print(d) #{}
```
##### get(\<key>)
```Python:
d = {'a': 1, 'b': 2}
print(d.get('a')) #1
print(d.get('z', 'No encontrado')) #No encontrado
```
##### items()
```Python:
d = {'a': 1, 'b': 2}
it = d.items()
print(it)             #dict_items([('a', 1), ('b', 2)])
print(list(it))       #[('a', 1), ('b', 2)]
print(list(it)[0][0]) #a
```
##### keys()
```Python:
d = {'a': 1, 'b': 2}
k = d.keys()
print(k)       #dict_keys(['a', 'b'])
print(list(k)) #['a', 'b']
```
##### values()
```Python:
d = {'a': 1, 'b': 2}
print(list(d.values())) #[1, 2]
```
##### pop(\<key>)
```Python:
d = {'a': 1, 'b': 2}
d.pop('a')
print(d) #{'b': 2}
```
##### popitem()
```Python:
d = {'a': 1, 'b': 2}
d.popitem()
print(d)
#{'a': 1}
```
##### update()
```Python:
d1 = {'a': 1, 'b': 2}
d2 = {'a': 0, 'd': 400}
d1.update(d2)
print(d1)
#{'a': 0, 'b': 2, 'd': 400}
```

Se puede imprimir también solo el value.

```Python:
# Impre los value del diccionario
for x in d1:
    print(d1[x])
#Laura
#27
#1003882
#Calle 123
```

O si queremos imprimir el key y el value a la vez.

```Python:
# Imprime los key y value del diccionario
for x, y in d1.items():
    print(x, y)
#Nombre Laura
#Edad 27
#Documento 1003882
#Direccion Calle 123
```