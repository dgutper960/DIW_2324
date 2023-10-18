# UT04. Actividad X. Trabajando con BEM

Como hemos visto en la teoría, BEM (Block__Element--Modifier) es un sistema de nomenclatura de clases CSS.

Un **Bloque** es un componente de interfaz de usuario independiente. Un bloque puede estar compuesto por varios elementos HTML.

Un **Elemento** es un componente de un bloque. Un elemento sirve para un propósito particular.

Un **Modificador** es una clase CSS que cambia la presentación de un bloque o un elemento.

A la hora de nombrar las clases en **BEM** tenemos que definir 3 cosas:

- El bloque: Definimos una clase para el bloque.
    - *.nombreClaseBloque*
- El elemento: Definimos una clase para el elemento del bloque.
    - *.nombreClaseBloque__nombreElementoHijo*
- El modificador: Definimos una clase para el modificador del elemento
    - *.nombreClaseBloque_nombreElementoHijo--modificador*

>Como dijo AbDul-Jabah Al-Hattari: *No me pises que llevo chanclas*

#### Enunciado

Haciendo uso de la **metodología BEM** corrige el proyecto contenido en la carpeta *ProyectoSinBEM* para que siga los estándares y recomendaciones de dicha metodología.