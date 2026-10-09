from ej02 import Producto


class ItemCarrito:
    def __init__(self, producto: Producto, cantidad: int):
        self.producto = producto
        self.cantidad = cantidad

    def calcular_subtotal(self) -> float:
        return self.producto.precio_unitario * self.cantidad

    def __str__(self) -> str:
        return (
            f"{self.producto.nombre} x{self.cantidad} "
            f"@ {self.producto.precio_unitario:,.0f} Gs. = {self.calcular_subtotal():,.0f} Gs."
        )


class CarritoCompras:
    def __init__(self):
        self.items: list[ItemCarrito] = []

    def agregar_item(self, producto: Producto, cantidad: int):
        self.items.append(ItemCarrito(producto, cantidad))

    def calcular_total(self) -> float:
        return sum(item.calcular_subtotal() for item in self.items)

    def mostrar_detalle(self):
        print(" DETALLE DEL CARRITO DE COMPRAS")
        print("=" * 45)
        for item in self.items:
            print(f" • {item}")
        print("=" * 45)
        print(f" TOTAL A PAGAR: {self.calcular_total():,.0f} Gs.")


if __name__ == "__main__":
    prod1 = Producto("Teclado Mecánico", 250000, 10)
    prod2 = Producto("Mouse Gamer", 120000, 15)

    carrito = CarritoCompras()
    carrito.agregar_item(prod1, 2)
    carrito.agregar_item(prod2, 1)

    carrito.mostrar_detalle()