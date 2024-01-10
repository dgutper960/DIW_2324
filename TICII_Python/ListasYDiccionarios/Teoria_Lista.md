## Listas en Python
###### Obtenido de [*El Libro de Python*](https://ellibrodepython.com/)

Las listas en Python son un tipo de dato que permite almacenar datos de cualquier tipo. Son mutables y dinámicas, lo cual es la principal diferencia con los sets y las tuplas.

#### Crear listas Python

Las listas en Python son uno de los tipos o estructuras de datos más versátiles del lenguaje, ya que permiten almacenar un conjunto arbitrario de datos. Es decir, podemos guardar en ellas prácticamente lo que sea. Si vienes de otros lenguajes de programación, se podría decir que son similares a los arrays.

```Python:
lista = [1, 2, 3, 4]
```

También se puede crear usando ```list``` y pasando un objeto [iterable](https://ellibrodepython.com/iterator-python).

Una lista se crea con ```[]``` separando sus elementos con comas. Una gran ventaja es que pueden almacenar tipos de datos distintos.

```Python:
lista = [1, "Hola", 3.67, [1,2,3]]
```

Como puedes observar en el ejemplo anterior, se ha creado una lista que contiene datos numéricos enteros, cadenas de caracteres, datos numéricos reales, e incluso otra lista.

Algunas propiedades de las listas son:
- Son **ordenadas**, mantienen el orden en el que han sido definidas
- Pueden ser formadas por tipos **arbitrarios**
- Pueden ser indexadas con ``[i]``.
- Se pueden **anidar**, es decir, meter una dentro de la otra.
- Son **mutables**, ya que sus elementos pueden ser modificados.
- Son **dinámicas**, ya que se pueden añadir o eliminar elementos.

#### Acceder y modificar listas

Si tenemos una lista ``a`` con 3 elementos almacenados en ella, podemos acceder a los mismos usando corchetes y un índice, que va desde ``0`` a ``n-1`` siendo ``n`` el tamaño de la lista.`

```Python:
a = [90, "Python", 3.87]
print(a[0]) #90
print(a[1]) #Python
print(a[2]) #3.87
```

Se puede también acceder al último elemento usando el índice ``[-1]``.

```Python:
a = [90, "Python", 3.87]
print(a[-1]) #3.87
```

De la misma manera, al igual que ``[-1]`` es el último elemento, podemos acceder a ``[-2]`` que será el penúltimo.

```Python:
print(a[-2]) #Python
```

Y si queremos modificar un elemento de la lista, basta con asignar con el operador = el nuevo valor.

```Python:
a[2] = 1
print(a) #[90, 'Python', 1]
```

Un elemento puede ser eliminado con diferentes métodos como veremos a continuación, o con ``del`` y la lista con el índice a eliminar.

```Python:
l = [1, 2, 3, 4, 5]
del l[1]
print(l) #[1, 3, 4, 5]
```

También es posible crear sublistas más pequeñas de una más grande. Para ello debemos de usar : entre corchetes, indicando a la izquierda el valor de inicio, y a la izquierda el valor final que no está incluido. Por lo tanto ``[0:2]`` creará una lista con los elementos ``[0]`` y ``[1]`` de la original.

```Python:
l = [1, 2, 3, 4, 5, 6]
print(l[0:2]) #[1, 2]
print(l[2:6]) #[3, 4, 5, 6]
```

Hay ciertos operadores como el ``+`` que pueden ser usados sobre las listas.

```Python:
l = [1, 2, 3]
l += [4, 5]
print(l) #[1, 2, 3, 4, 5]
```

#### Iterar listas

En Python es muy fácil iterar una lista, mucho más que en otros lenguajes de programación.

```Python:
lista = [5, 9, 10]
for l in lista:
    print(l)
#5
#9
#10
```