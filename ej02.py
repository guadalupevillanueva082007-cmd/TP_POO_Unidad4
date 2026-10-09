class Producto:
    def __init__(self, nombre: str, precio_unitario: float, stock: int):
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.stock = stock

    def calcular_valor_total_stock(self) -> float:
        return self.precio_unitario * self.stock

    def __str__(self) -> str:
        valor_total = self.calcular_valor_total_stock()
        return (
            f"Producto: {self.nombre}\n"
            f"  Precio Unitario: {self.precio_unitario:,.0f} Gs.\n"
            f"  Stock Actual   : {self.stock} unidades\n"
            f"  Valor Total    : {valor_total:,.0f} Gs."
        )


if __name__ == "__main__":
    p1 = Producto("Yerba Mate 1kg", 18000, 25)
    p2 = Producto("Aceite de Girasol 900ml", 14500, 12)

    print(p1)
    print("-" * 30)
    print(p2)