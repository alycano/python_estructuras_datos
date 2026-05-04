# 1. Definir ventas_por_region como dict anidado
ventas_por_region = {
    "Norte": {"Q1": 15758, "Q2": 19632, "Q3": 16552, "Q4": 21441},
    "Sur":   {"Q1": 12117, "Q2": 11547, "Q3": 13114, "Q4": 14522},
    "Este":  {"Q1": 21022, "Q2": 22774, "Q3": 21159, "Q4": 24654},
    "Oeste": {"Q1": 10114, "Q2": 12802, "Q3": 11810, "Q4": 13123}
}

# 2. Calcular ventas totales con items() y sum(values())
totales_por_region = {}
for region, ventas in ventas_por_region.items():
    totales_por_region[region] = sum(ventas.values())

print("--- VENTAS TOTALES ANUALES POR REGIÓN ---")
for region, total in totales_por_region.items():
    print(f"Región {region}: ${total:,}")

# 3. Encontrar región con mayores ventas usando max() con key=lambda
mejor_region = max(totales_por_region, key=lambda k: totales_por_region[k])
print(f"\nLa región con mayores ventas fue: {mejor_region} (${totales_por_region[mejor_region]:,})")

# 4. Acumular ventas por trimestre con iteración anidada
totales_por_trimestre = {"Q1": 0, "Q2": 0, "Q3": 0, "Q4": 0}
for region, ventas in ventas_por_region.items():
    for trimestre, monto in ventas.items():
        totales_por_trimestre[trimestre] += monto

print("\n--- VENTAS TOTALES POR TRIMESTRE (TODAS LAS REGIONES) ---")
for trim, monto in totales_por_trimestre.items():
    print(f"{trim}: ${monto:,}")

# 5. Calcular gran total y porcentajes con dict comprehension
gran_total = sum(totales_por_region.values())
porcentajes_por_region = {
    region: round((total / gran_total) * 100, 2)
    for region, total in totales_por_region.items()
}

# 6. Imprimir reporte ordenado de mayor a menor con sorted() + items()
reporte_ordenado = sorted(
    totales_por_region.items(),
    key=lambda x: x[1],
    reverse=True
)

print(f"\n--- REPORTE FINAL ORDENADO (Gran Total: ${gran_total:,}) ---")
for region, total in reporte_ordenado:
    pct = porcentajes_por_region[region]
    print(f"Región {region:<6} | Total: ${total:<8,} | Porcentaje: {pct}%")