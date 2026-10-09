class Cliente:
    def __init__(self, nombre: str, cedula: str, telefono: str):
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono

    def __str__(self) -> str:
        return (
            f"FICHA DE CLIENTE\n"
            f"  Nombre  : {self.nombre}\n"
            f"  Cédula  : {self.cedula}\n"
            f"  Teléfono: {self.telefono}"
        )


if __name__ == "__main__":
    cliente1 = Cliente("María González", "4.567.890", "0981-123456")
    cliente2 = Cliente("Carlos Benítez", "3.210.987", "0971-654321")

    print(cliente1)
    print("-" * 30)
    print(cliente2)