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

Reto 4 Tiendas y recomendaciones de películas

Para resolver este reto avanzado del módulo de conjuntos, dividí el desarrollo en dos secciones utilizando tanto los métodos de clase como los operadores matemáticos. En la primera parte, analicé el inventario de tres tiendas distintas mediante el uso de los métodos .union() y .intersection() para obtener el catálogo completo de la empresa y descubrir los productos comunes entre todas las sedes. Luego, utilicé .difference() en combinación con la unión de los otros inventarios para aislar los productos exclusivos de cada tienda, y verifiqué si había solapamientos entre la tienda Norte y Sur usando el método .isdisjoint().

En la segunda parte del ejercicio, gestioné las preferencias de géneros cinematográficos de tres usuarios aplicando los operadores matemáticos de conjuntos. Empleé el operador & para encontrar los géneros compartidos por todos, el operador | para consolidar el universo total de categorías, el operador - para identificar los gustos únicos del primer usuario, y el operador ^ para calcular la diferencia simétrica entre los dos primeros perfiles. Por último, utilicé el operador <= para comprobar si los gustos de un usuario eran un subconjunto de los de otro. Esta práctica me ayudó a dominar la diferencia entre aplicar métodos tradicionales y utilizar operadores matemáticos abreviados para realizar análisis de datos precisos en Python.

----------------------------------------------------------------------------------------------------------------

Reto 5 Analizador de ventas con las 3 comprehensions

Para resolver el quinto reto, utilicé las tres variantes de comprehensions para procesar un dataset de ventas de forma muy eficiente. Primero, mediante una comprensión de lista, calculé el valor total de cada venta multiplicando las unidades por el precio, y luego apliqué un filtro para extraer solo los nombres de los productos que superaron los mil dólares. Después, utilicé una comprensión de diccionario para crear un mapa estructurado de cada artículo junto con su información de ingresos y unidades; además, construí un ranking premium filtrando los artículos con precios mayores a cincuenta dólares y los ordené de mayor a menor.

Asimismo, aproveché las propiedades de las comprensiones de conjunto para extraer de forma automática y sin duplicados las categorías únicas del negocio, así como el listado de productos más económicos. Finalmente, combiné las tres técnicas para generar un reporte resumido y obtuve el gran total de las ventas usando la función sum(). Este ejercicio me ayudó a entender cómo las comprehensions de Python reducen el código de manera elegante y optimizan el rendimiento de lectura y transformación de datos en comparación con los ciclos tradicionales.

---------------------------------------------------------------------------------------------------------------

