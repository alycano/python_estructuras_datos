# 1. En esta parte defino el catalogo como tupla de subtuplas (titulo, director, año, puntuación)
catalogo = (
    ("Forrest Gump", "Robert Zemeckis", 1994, 8.8),
    ("Titanic", "James Cameron", 1997, 7.8),
    ("Pulp Fiction", "Quentin Tarantino", 1994, 8.9),
    ("The Matrix", "Lana y Lilly Wachowski", 1999, 8.7)
)

# 2. Recorrer catalogo con for desempaquetando los cuatro campos
print("--- CATÁLOGO DE PELÍCULAS ---")
for titulo, director, anio, puntuacion in catalogo:
    print(f"Título: {titulo} | Director: {director} | Año: {anio} | Puntuación: {puntuacion}")

# 3. Usar operador * para separar primera película del resto
primera_pelicula, *resto_peliculas = catalogo
print("\n--- SEPARACIÓN CON OPERADOR * ---")
print(f"Primera película guardada: {primera_pelicula[0]} ({primera_pelicula[2]})")
print(f"Número de películas restantes: {len(resto_peliculas)}")

# 4. Definir buscar_por_director(director)
def buscar_por_director(director_buscado):
    """Busca y retorna una tupla con las películas de un director específico."""
    coincidencias = []
    for pelicula in catalogo:
        # pelicula[1] es el director
        if pelicula[1].lower() == director_buscado.lower():
            coincidencias.append(pelicula)
    return tuple(coincidencias)

# 5. Definir obtener_estadisticas(peliculas)
def obtener_estadisticas():
    """Calcula la puntuación mínima, máxima y el promedio de las películas."""
    puntuaciones = [pelicula[3] for pelicula in catalogo]
    minima = min(puntuaciones)
    maxima = max(puntuaciones)
    promedio = sum(puntuaciones) / len(puntuaciones)
    return minima, maxima, promedio

# --- EJECUCIÓN DE PRUEBAS ---

# 6. Llamar a buscar_por_director e imprimir coincidencias
print("\n--- BÚSQUEDA POR DIRECTOR ---")
director = "Robert Zemeckis"
peliculas_nolan = buscar_por_director(director)
print(f"Películas encontradas de '{director}':")
for titulo, _, anio, puntuacion in peliculas_nolan:
    print(f"- {titulo} ({anio}) - Calificación: {puntuacion}")

# 7 y 8. Desempaquetar retorno de obtener_estadisticas e imprimir los tres valores
print("\n--- ESTADÍSTICAS DEL CATÁLOGO ---")
peor_nota, mejor_nota, promedio_nota = obtener_estadisticas()
print(f"Puntuación más baja: {peor_nota}")
print(f"Puntuación más alta: {mejor_nota}")
print(f"Promedio de calificación: {promedio_nota:.2f}")