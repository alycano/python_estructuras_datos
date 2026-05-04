Reto 1 Gestión de inventario

Para resolver este reto, utilicé una lista de listas para guardar mis productos, ya que me permite juntar el nombre, la cantidad y el precio en un solo lugar. Primero, definí el inventario con los tres productos iniciales. Luego, utilicé la función de actualizar precios para modificar el valor del segundo producto ("Mouse") y usé la función de ventas para restar unidades del primer producto ("Laptop") tras simular una venta. También agregué un producto nuevo ("Monitor") a la lista usando la función de añadir producto con el método append(). Finalmente, ejecuté la función de mostrar inventario para verificar que todos los cambios se guardaron correctamente. Este ejercicio me sirvió mucho para entender que las listas en Python se pueden modificar directamente, lo que hace que el manejo de los datos sea muy rápido y práctico.

--------------------------------------------------------------------------------------------------------------

Reto 2 Sistema de peliculas

Para resolver el segundo reto, construí un catálogo de películas utilizando una tupla de tuplas, ya que esta estructura me garantiza que los datos de las películas no se puedan modificar por accidente gracias a su propiedad de inmutabilidad. Al recorrer el catálogo, utilicé el desempaquetado básico en un ciclo for para extraer directamente el título, director, año y puntuación de cada película sin necesidad de usar índices. También implementé el operador * para separar la primera película del resto del catálogo de forma muy sencilla.

En la búsqueda por director, creé una función que filtra las coincidencias comparando los nombres en minúsculas para evitar errores tipográficos, y convertí el resultado final de nuevo en una tupla para mantener la inmutabilidad de los datos retornados. Para las estadísticas, definí una función que extrae las puntuaciones y calcula el valor mínimo, máximo y el promedio, retornando estos tres datos en una sola tupla. Finalmente, desempaqueté este retorno en tres variables individuales para imprimirlas ordenadamente. Este ejercicio me ayudó a entender las ventajas de rendimiento y seguridad que ofrecen las tuplas cuando manejamos datos que deben permanecer fijos durante la ejecución del programa.

---------------------------------------------------------------------------------------------------------------

Reto 3 Análisis de ventas por región

Para resolver el tercer reto, utilicé un diccionario anidado para modelar las ventas trimestrales de cuatro regiones. Al trabajar con esta estructura, utilicé el método .items() para recorrer cada región y la función sum(values()) para calcular el total anual de cada una sin complicaciones. Para identificar cuál fue la región con mejor rendimiento, empleé la función max() combinada con una función lambda, lo que me permitió evaluar los valores del diccionario de totales de forma directa. Luego, utilicé una iteración anidada para recorrer los trimestres de cada región e ir acumulando las ventas globales de cada trimestre en un nuevo diccionario.

Finalmente, calculé el gran total sumando todos los ingresos regionales y utilicé una comprensión de diccionario para generar los porcentajes de participación de cada zona en una sola línea de código. Para cerrar el ejercicio, ordené los datos de mayor a menor ventas usando la función sorted() con una clave personalizada, mostrando el reporte final de manera clara y estructurada. Este reto me permitió comprender lo útiles que son los diccionarios para agrupar y analizar datos complejos mediante el uso de estructuras clave-valor.

---------------------------------------------------------------------------------------------------------------

