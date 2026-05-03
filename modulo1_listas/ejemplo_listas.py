# --- REPLICA DE EJEMPLOS DEL MATERIAL ---

# 1. Creación y Acceso
frutas = ["manzana", "plátano", "cereza"]
print(f"Primera fruta: {frutas[0]}")
print(f"Última fruta: {frutas[-1]}")

# 2. Slicing
numeros = [10, 20, 30, 40, 50, 60, 70]
print(f"Sublista (1 al 3): {numeros[1:4]}")
print(f"Invertida: {numeros[::-1]}")

# 3. Métodos para añadir y eliminar
colores = ["rojo", "azul"]
colores.append("verde")      # Añade al final
colores.insert(1, "amarillo") # Inserta en índice 1
colores.pop(0)               # Elimina el índice 0 (rojo)
print(f"Lista de colores final: {colores}")

# 4. Ordenamiento
desordenados = [5, 2, 9, 1]
desordenados.sort()
print(f"Lista ordenada: {desordenados}")