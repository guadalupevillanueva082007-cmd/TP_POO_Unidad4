class Estudiante:
    def __init__(self, nombre: str, cedula: str):
        self.nombre = nombre
        self.cedula = cedula
        self.calificaciones: dict[str, float] = {}

    def registrar_nota(self, materia: str, nota: float):
        self.calificaciones[materia] = nota

    def calcular_promedio(self) -> float:
        if not self.calificaciones:
            return 0.0
        return sum(self.calificaciones.values()) / len(self.calificaciones)

    def esta_aprobado(self, nota_minima: float = 2.0) -> bool:
        return self.calcular_promedio() >= nota_minima

    def __str__(self) -> str:
        lineas = [f"BOLETÍN ACADÉMICO: {self.nombre} (C.I. {self.cedula})", "-" * 40]
        for materia, nota in self.calificaciones.items():
            lineas.append(f"  - {materia}: {nota}")
        
        prom = self.calcular_promedio()
        estado = "APROBADO" if self.esta_aprobado() else "REPROBADO"
        lineas.append("-" * 40)
        lineas.append(f" Promedio General: {prom:.2f}")
        lineas.append(f" Condición Final : [{estado}]")
        return "\n".join(lineas)


if __name__ == "__main__":
    estudiante = Estudiante("Beatriz Peña", "5.123.456")
    estudiante.registrar_nota("Python Lenguaje I", 5.0)
    estudiante.registrar_nota("Base de Datos", 4.0)
    estudiante.registrar_nota("Matemática Discreta", 3.0)

    print(estudiante)