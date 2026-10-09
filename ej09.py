class Turno:
    def __init__(self, paciente: str, hora: str):
        self.paciente = paciente
        self.hora = hora
        self.atendido = False

    def marcar_como_atendido(self):
        self.atendido = True

    def __str__(self) -> str:
        estado = "Atendido" if self.atendido else "Pendiente"
        return f"[{self.hora}] Paciente: {self.paciente} | Estado: {estado}"


class Agenda:
    def __init__(self, fecha: str):
        self.fecha = fecha
        self.turnos: list[Turno] = []

    def agendar_turno(self, paciente: str, hora: str):
        nuevo_turno = Turno(paciente, hora)
        self.turnos.append(nuevo_turno)

    def listar_pendientes(self):
        print(f"\n Turnos Pendientes ({self.fecha}):")
        pendientes = [t for t in self.turnos if not t.atendido]
        if not pendientes:
            print("  No hay turnos pendientes.")
        else:
            for t in pendientes:
                print(f"  - {t}")


if __name__ == "__main__":
    agenda = Agenda("07/10/2026")
    agenda.agendar_turno("Roberto Gómez", "08:30")
    agenda.agendar_turno("Lucía Méndez", "09:15")
    agenda.agendar_turno("Mario Abdo", "10:00")

    agenda.listar_pendientes()

    # Se atiende al primer paciente
    print("\n--- Atendiendo a Roberto Gómez ---")
    agenda.turnos[0].marcar_como_atendido()

    agenda.listar_pendientes()