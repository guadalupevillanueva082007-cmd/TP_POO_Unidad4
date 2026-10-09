class Cancion:
    def __init__(self, titulo: str, artista: str, duracion_segundos: int):
        self.titulo = titulo
        self.artista = artista
        self.duracion_segundos = duracion_segundos

    def obtener_duracion_formateada(self) -> str:
        minutos = self.duracion_segundos // 60
        segundos = self.duracion_segundos % 60
        return f"{minutos}:{segundos:02d}"

    def __str__(self) -> str:
        return f"'{self.titulo}' - {self.artista} ({self.obtener_duracion_formateada()})"


class ListaReproduccion:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.canciones: list[Cancion] = []

    def agregar_cancion(self, cancion: Cancion):
        self.canciones.append(cancion)

    def calcular_duracion_total(self) -> int:
        return sum(c.duracion_segundos for c in self.canciones)

    def __str__(self) -> str:
        lineas = [f"LISTA DE REPRODUCCIÓN: {self.nombre}", "=" * 40]
        for idx, c in enumerate(self.canciones, 1):
            lineas.append(f"{idx}. {c}")
        
        total_seg = self.calcular_duracion_total()
        minutos = total_seg // 60
        segundos = total_seg % 60
        lineas.append("=" * 40)
        lineas.append(f"Duración Total: {minutos} min {segundos} seg")
        return "\n".join(lineas)


if __name__ == "__main__":
    mi_lista = ListaReproduccion("Éxitos en Español")
    mi_lista.agregar_cancion(Cancion("De Música Ligera", "Soda Stereo", 212))
    mi_lista.agregar_cancion(Cancion("Lamento Boliviano", "Los Enanitos Verdes", 223))
    mi_lista.agregar_cancion(Cancion("Rayando el Sol", "Maná", 254))

    print(mi_lista)