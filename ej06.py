class CuentaCorriente:
    def __init__(self, cliente: str, saldo_inicial: float = 0.0):
        self.cliente = cliente
        self.saldo = saldo_inicial

    def acreditar(self, monto: float):
        if monto > 0:
            self.saldo += monto
            print(f" Acreditado: {monto:,.0f} Gs. Nuevo saldo: {self.saldo:,.0f} Gs.")
        else:
            print(" El monto a acreditar debe ser mayor a 0.")

    def registrar_consumo(self, monto: float) -> bool:
        if monto <= 0:
            print(" El monto de compra debe ser mayor a 0.")
            return False
        
        if monto > self.saldo:
            print(f" RECHAZADO: Fondos insuficientes para gastar {monto:,.0f} Gs. (Saldo actual: {self.saldo:,.0f} Gs.)")
            return False

        self.saldo -= monto
        print(f" Consumo registrado: {monto:,.0f} Gs. Saldo restante: {self.saldo:,.0f} Gs.")
        return True

    def __str__(self) -> str:
        return f"Cuenta de {self.cliente} | Saldo: {self.saldo:,.0f} Gs."


if __name__ == "__main__":
    cuenta = CuentaCorriente("Juan Pérez", 50000)
    print(cuenta)

    print("\n--- Secuencia de operaciones ---")
    cuenta.acreditar(100000)
    cuenta.registrar_consumo(80000)
    cuenta.registrar_consumo(100000)  # Operación rechazada
    cuenta.acreditar(50000)
    cuenta.registrar_consumo(100000)  # Operación aprobada

    print("\n--- Estado final ---")
    print(cuenta)