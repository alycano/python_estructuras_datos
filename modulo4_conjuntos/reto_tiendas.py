# 1. Definir tienda_centro, tienda_norte y tienda_sur como sets de productos
tienda_centro = {"Laptop", "Mouse", "Teclado", "Monitor", "Audífonos"}
tienda_norte  = {"Teclado", "Monitor", "Cámara Web", "Micrófono"}
tienda_sur    = {"Audífonos", "Mouse", "Impresora", "Escaner"}

print("=== PARTE 1: ANÁLISIS DE TIENDAS ===")

# 2. Calcular catalogo_completo con union() y productos_comunes con intersection()
catalogo_completo = tienda_centro.union(tienda_norte).union(tienda_sur)
productos_comunes = tienda_centro.intersection(tienda_norte).intersection(tienda_sur)

print(f"Catálogo completo de la cadena ({len(catalogo_completo)} productos): {catalogo_completo}")
print(f"Productos comunes en las tres tiendas: {productos_comunes if productos_comunes else 'Ninguno'}")

# 3. Usa difference() para exclusivos e isdisjoint() para solapamientos
exclusivos_centro = tienda_centro.difference(tienda_norte.union(tienda_sur))
exclusivos_norte  = tienda_norte.difference(tienda_centro.union(tienda_sur))
exclusivos_sur    = tienda_sur.difference(tienda_centro.union(tienda_norte))

print(f"\nProductos exclusivos de Tienda Centro: {exclusivos_centro}")
print(f"Productos exclusivos de Tienda Norte: {exclusivos_norte}")
print(f"Productos exclusivos de Tienda Sur: {exclusivos_sur}")

print(f"\n¿Tienda Norte y Tienda Sur no tienen ningún producto en común?: {tienda_norte.isdisjoint(tienda_sur)}")


print("\n=== PARTE 2: RECOMENDACIONES DE PELÍCULAS ===")

# 4. Definir usuario1, usuario2, usuario3 como sets de géneros cinematográficos
usuario1 = {"Acción", "Comedia", "Ciencia Ficción", "Aventura"}
usuario2 = {"Drama", "Comedia", "Romance", "Documental"}
usuario3 = {"Acción", "Aventura", "Fantasía", "Ciencia Ficción"}

# 5. Usa & | - ^ para comunes, universo, exclusivos y diferencias
generos_comunes = usuario1 & usuario2 & usuario3
universo_generos = usuario1 | usuario2 | usuario3
solo_usuario1 = usuario1 - (usuario2 | usuario3)
diferencia_simetrica_1_2 = usuario1 ^ usuario2

print(f"Géneros comunes entre los tres usuarios: {generos_comunes if generos_comunes else 'Ninguno'}")
print(f"Universo total de géneros de los tres usuarios: {universo_generos}")
print(f"Géneros exclusivos que solo le gustan al Usuario 1: {solo_usuario1}")
print(f"Géneros que le gustan al Usuario 1 o al Usuario 2, pero no a ambos: {diferencia_simetrica_1_2}")

# 6. Usa <= para verificar subconjunto e imprime el resumen final integrado
es_subconjunto_u3_u1 = usuario3 <= usuario1
print(f"\n¿Todos los géneros del Usuario 3 le gustan también al Usuario 1?: {es_subconjunto_u3_u1}")