class ProductoStock:
    def __init__(self, nombre: str, precio: float, stock_inicial: int, stock_minimo: int):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock_inicial
        self.stock_minimo = stock_minimo

    def reponer_stock(self, cantidad: int):
        if cantidad > 0:
            self.stock += cantidad
            print(f" Se repusieron {cantidad} unidades. Stock actual: {self.stock}")
            self._verificar_alerta()

    def vender(self, cantidad: int) -> bool:
        if cantidad <= 0:
            print(" La cantidad a vender debe ser mayor a 0.")
            return False
        
        if cantidad > self.stock:
            print(f" VENTA CANCELADA: Stock insuficiente ({self.stock} disponibles, intentó vender {cantidad}).")
            return False

        self.stock -= cantidad
        print(f" Venta realizada: {cantidad} unidad(es). Stock restante: {self.stock}")
        self._verificar_alerta()
        return True

    def _verificar_alerta(self):
        if self.stock < self.stock_minimo:
            print(f" ALERTA: El stock de '{self.nombre}' ({self.stock}) está por debajo del mínimo ({self.stock_minimo}). ¡Reponer pronto!")

    def __str__(self) -> str:
        return f"Producto: {self.nombre} | Stock: {self.stock} | Stock Mínimo: {self.stock_minimo}"


if __name__ == "__main__":
    prod = ProductoStock("Leche Entera 1L", 7000, stock_inicial=10, stock_minimo=5)
    print(prod)

    print("\n--- Operaciones de Stock ---")
    prod.vender(4)
    prod.vender(3)  # Salta alerta por debajo de 5
    prod.vender(5)  # Cancela por falta de stock
    prod.reponer_stock(10)