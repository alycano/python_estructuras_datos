# 1. Definir ventas con 6 productos
ventas = [
    {"producto": "Laptop",    "unidades": 10, "precio": 800,  "categoria": "Tecnología"},
    {"producto": "Teclado",   "unidades": 50, "precio": 25,   "categoria": "Tecnología"},
    {"producto": "Mouse",     "unidades": 40, "precio": 15,   "categoria": "Tecnología"},
    {"producto": "Monitor",   "unidades": 12, "precio": 200,  "categoria": "Tecnología"},
    {"producto": "Silla",     "unidades": 5,  "precio": 150,  "categoria": "Muebles"},
    {"producto": "Escritorio","unidades": 3,  "precio": 300,  "categoria": "Muebles"}
]

print("=== PROCESAMIENTO DE VENTAS CON COMPREHENSIONS ===")

# 2. List comp: valor_total = unidades * precio por cada producto
valores_totales = [i["unidades"] * i["precio"] for i in ventas]
print(f"\nValores totales por venta: {valores_totales}")

# 3. List comp con filtro: productos_destacados (valor_total > 1000)
productos_destacados = [
    i["producto"] for i in ventas 
    if i["unidades"] * i["precio"] > 1000
]
print(f"Productos destacados (> $1000): {productos_destacados}")

# 4. Dict comp: producto_info mapping nombre -> {valor_total, unidades}
producto_info = {
    i["producto"]: {"valor": i["unidades"] * i["precio"], "unidades": i["unidades"]}
    for i in ventas
}
print(f"\nInformación por producto (Mapeo): {producto_info}")

# 5. Dict comp con filtro: ranking_premium (precio > 50) ordenado por valor descendente
ranking_premium_sin_ordenar = {
    i["producto"]: i["unidades"] * i["precio"]
    for i in ventas if i["precio"] > 50
}
# Ordenamos el diccionario resultante por su valor de mayor a menor
ranking_premium = {
    k: v for k, v in sorted(ranking_premium_sin_ordenar.items(), key=lambda x: x[1], reverse=True)
}
print(f"Ranking Premium (> $50 precio) descendente: {ranking_premium}")

# 6. Set comp: categorias_unicas
categorias_unicas = {i["categoria"] for i in ventas}
print(f"\nCategorías únicas (Set): {categorias_unicas}")

# 7. Set comp con filtro: productos_baratos (precio <= 50)
productos_baratos = {i["producto"] for i in ventas if i["precio"] <= 50}
print(f"Productos económicos (<= $50 precio): {productos_baratos}")

# 8. Combinar: resumen_formateado (dict comp con filtro) + gran_total con sum()
resumen_formateado = {
    i["producto"]: f"${i['unidades'] * i['precio']:,}" 
    for i in ventas if i["unidades"] > 5
}
gran_total = sum(valores_totales)

print("\n=== RESUMEN FINAL ===")
print(f"Productos con más de 5 unidades vendidas: {resumen_formateado}")
print(f"Gran total de ventas acumuladas: ${gran_total:,}")