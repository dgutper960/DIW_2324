# Atributo Display
### Conceptos principales sobre el atributo Display

*¿Qué valores puede tomar el atributo **display**?*

block | inline | inline-block | none | flex | grid

El atributo ***"display"*** en CSS se utiliza para controlar cómo se muestra un elemento en una página web. Hay varios valores que puedes usar para el atributo *"display"* pero los más comunes son:

- **block**: Los elementos con *"display: block"* ocupan todo el ancho disponible y se muestran en una línea separada en la página. Esto significa que comienzan en una nueva línea y abarcan todo el ancho de su contenedor.  
**IMPORTANTE**
    - **\<div>** es el principal ejemplo de elemento block

- **inline**: Los elementos con *"display: inline"* se muestran en la misma línea que el contenido circundante. No ocupan todo el ancho disponible y se ajustan al contenido que contienen.  
**IMPORTANTE**  
    - Su ancho (width) y alto (height) se ajustan A LO QUE CONTIENE EL ELEMENTO. De hecho, el ancho y el alto de un elemento *inline* **no se puede variar**.
    - **\<span>** es el principal ejemplo de elemento inline.


- **inline-block**: Los elementos con *"display: inline-block"* se comportan como elementos en línea (inline), pero permiten aplicar estilos de bloque (block), lo que significa que pueden tener un ancho y alto específicos, márgenes y relleno.  

- **none**: Los elementos con *"display: none"* no se muestran en la página en absoluto, están ocultos y se comportan como si no existieran. Es como si el elemento no existiera en el documento.

- **flex**: Los elementos con *"display: flex"* se utilizan para crear diseños flexibles y permiten un control más avanzado de la distribución de elementos en una fila o columna. El atributo *display: flex;* tiene muchas propiedades y conviene estudiarlo en detalle para saber cómo usarlo. Recomiendo [esta guía](https://css-tricks.com/snippets/css/a-guide-to-flexbox/) para poder entender y usar flex.

- **grid**: Los elementos con *"display: grid"* se utilizan para crear diseños de cuadrícula y permiten organizar elementos en filas y columnas, lo que es útil para diseñar páginas complejas. Al igual que con el atributo anterior, *display: flex;* merece ser estudiado en detalle para una buena comprensión. Recomiendo [esta guía](https://css-tricks.com/snippets/css/complete-guide-grid/) para poder entender y usar grid.