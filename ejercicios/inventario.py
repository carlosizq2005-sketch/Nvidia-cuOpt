"""Gestor de inventario de ejemplo, usado en los ejercicios del tutorial de Git."""

import pandas as pd
from rich import print
from rich.table import Table


def crear_inventario():
    return [
        {"nombre": "Teclado", "categoria": "Periféricos", "precio": 45.0, "cantidad": 10},
        {"nombre": "Ratón", "categoria": "Periféricos", "precio": 20.0, "cantidad": 25},
        {"nombre": "Monitor", "categoria": "Pantallas", "precio": 150.0, "cantidad": 5},
    ]


def anadir_producto(inventario, nombre, categoria, precio, cantidad):
    inventario.append(
        {"nombre": nombre, "categoria": categoria, "precio": precio, "cantidad": cantidad}
    )


def calcular_total(inventario):
    return sum(producto["precio"] * producto["cantidad"] for producto in inventario)


def aplicar_descuento(inventario, porcentaje):
    for producto in inventario:
        producto["precio"] = round(producto["precio"] * (1 - porcentaje / 100), 2)


def mostrar_inventario(inventario):
    tabla = Table(title="Inventario")
    tabla.add_column("Producto")
    tabla.add_column("Categoría")
    tabla.add_column("Precio (€)", justify="right")
    tabla.add_column("Cantidad", justify="right")
    for producto in inventario:
        tabla.add_row(
            producto["nombre"],
            producto["categoria"],
            f"{producto['precio']:.2f}",
            str(producto["cantidad"]),
        )
    print(tabla)


def resumen_por_categoria(inventario):
    """Devuelve, con pandas, el valor total del inventario agrupado por categoría."""
    df = pd.DataFrame(inventario)
    df["valor_total"] = df["precio"] * df["cantidad"]
    return df.groupby("categoria")["valor_total"].sum()


if __name__ == "__main__":
    inventario = crear_inventario()
    mostrar_inventario(inventario)
    print(f"\nValor total del inventario: {calcular_total(inventario):.2f} €")

    print("\nValor total por categoría:")
    print(resumen_por_categoria(inventario))