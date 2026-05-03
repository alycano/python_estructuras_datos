# --- RETO: GESTIÓN DE INVENTARIO ---

# 1. Inventario inicial [nombre, cantidad, precio]
inventario = [
    ["Laptop", 10, 1500.0],
    ["Mouse", 50, 25.0],
    ["Teclado", 30, 45.0]
]

def mostrar_inventario():
    print("\n--- INVENTARIO ACTUAL ---")
    for p in inventario:
        print(f"Producto: {p[0]} | Stock: {p[1]} | Precio: ${p[2]}")

def actualizar_precio(nombre, nuevo_precio):
    for p in inventario:
        if p[0].lower() == nombre.lower():
            p[2] = nuevo_precio
            print(f"\n> Precio de {nombre} actualizado.")

def registrar_venta(nombre, cantidad):
    for p in inventario:
        if p[0].lower() == nombre.lower():
            if p[1] >= cantidad:
                p[1] -= cantidad
                print(f"\n> Venta: {cantidad} {nombre}(s) vendidos.")
            else:
                print(f"\n> Error: No hay suficiente stock de {nombre}.")

def añadir_producto(nombre, cantidad, precio):
    for p in inventario:
        if p[0].lower() == nombre.lower():
            p[1] += cantidad
            print(f"\n> Stock de {nombre} incrementado.")
            return
    inventario.append([nombre, cantidad, precio])
    print(f"\n> Nuevo producto {nombre} añadido.")

# Ejecución de prueba
if __name__ == "__main__":
    mostrar_inventario()
    actualizar_precio("Laptop", 1300.0)
    registrar_venta("Mouse", 5)
    añadir_producto("Monitor", 10, 250.0)
    mostrar_inventario()