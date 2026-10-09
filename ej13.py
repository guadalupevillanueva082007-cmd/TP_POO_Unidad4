class Habitacion:
    def __init__(self, numero: int, tipo: str, tarifa_por_noche: float):
        self.numero = numero
        self.tipo = tipo
        self.tarifa_por_noche = tarifa_por_noche
        self.ocupada = False

    def ocupar(self) -> bool:
        if self.ocupada:
            print(f" CANCELADO: La habitación {self.numero} ya se encuentra ocupada.")
            return False
        self.ocupada = True
        print(f" Habitación {self.numero} ocupada exitosamente.")
        return True

    def liberar(self) -> bool:
        if not self.ocupada:
            print(f" CANCELADO: La habitación {self.numero} ya está libre.")
            return False
        self.ocupada = False
        print(f" Habitación {self.numero} liberada exitosamente.")
        return True

    def calcular_costo_estadia(self, noches: int) -> float:
        return self.tarifa_por_noche * noches

    def __str__(self) -> str:
        estado = "Ocupada" if self.ocupada else "Libre"
        return f"Habitación {self.numero} [{self.tipo}] - Tarifa: {self.tarifa_por_noche:,.0f} Gs./noche | Estado: [{estado}]"


if __name__ == "__main__":
    hab = Habitacion(numero=302, tipo="Suite Matrimonial", tarifa_por_noche=350000)
    print(hab)

    print("\n--- Simulación de Estadía ---")
    hab.ocupar()
    hab.ocupar()  # Intento de re-ocupar

    noches = 3
    costo = hab.calcular_costo_estadia(noches)
    print(f" Costo por {noches} noches: {costo:,.0f} Gs.")

    hab.liberar()
    print(hab)