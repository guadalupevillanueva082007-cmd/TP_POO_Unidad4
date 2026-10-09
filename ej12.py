class LineaTelefono:
    def __init__(self, numero: str, gigas_plan: float):
        self.numero = numero
        self.gigas_plan = gigas_plan
        self.gigas_consumidos = 0.0

    def consumir_datos(self, gigas: float):
        if self.gigas_consumidos >= self.gigas_plan:
            print(f" AVISO ({self.numero}): Tu paquete de datos ya está AGOTADO.")
            return

        self.gigas_consumidos += gigas
        print(f" Consumidos {gigas:.2f} GB en la línea {self.numero}.")

        if self.gigas_consumidos >= self.gigas_plan:
            print(f" ALERTA: Has alcanzado o superado el límite de tu plan ({self.gigas_plan} GB). Paquete agotado.")

    def obtener_gigas_disponibles(self) -> float:
        disponible = self.gigas_plan - self.gigas_consumidos
        return max(0.0, disponible)

    def __str__(self) -> str:
        return (
            f"Línea: {self.numero}\n"
            f"  Plan Contratado : {self.gigas_plan} GB\n"
            f"  Consumido       : {self.gigas_consumidos:.2f} GB\n"
            f"  Disponible      : {self.obtener_gigas_disponibles():.2f} GB"
        )


if __name__ == "__main__":
    linea = LineaTelefono("0981-999888", gigas_plan=10.0)
    print(linea)

    print("\n--- Consumos ---")
    linea.consumir_datos(4.5)
    linea.consumir_datos(6.0)  # Agota el paquete
    linea.consumir_datos(2.0)  # Aviso de paquete agotado

    print("\n--- Estado Final ---")
    print(linea)