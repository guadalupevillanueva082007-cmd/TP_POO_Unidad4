class Empleado:
    def __init__(self, nombre: str, cargo: str, salario_mensual: float):
        self.nombre = nombre
        self.cargo = cargo
        self.salario_mensual = salario_mensual

    def calcular_salario_anual(self, incluye_aguinaldo: bool = True) -> float:
        meses = 13 if incluye_aguinaldo else 12
        return self.salario_mensual * meses

    def __str__(self) -> str:
        anual_con_aguinaldo = self.calcular_salario_anual(incluye_aguinaldo=True)
        return (
            f"Empleado: {self.nombre}\n"
            f"  Cargo          : {self.cargo}\n"
            f"  Salario Mensual: {self.salario_mensual:,.0f} Gs.\n"
            f"  Salario Anual (+ Aguinaldo): {anual_con_aguinaldo:,.0f} Gs."
        )


if __name__ == "__main__":
    emp1 = Empleado("Ana Martínez", "Desarrolladora Python", 6500000)
    emp2 = Empleado("Luis Vera", "Analista de Soporte", 3500000)

    print(emp1)
    print("-" * 30)
    print(emp2)