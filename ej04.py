class Libro:
    def __init__(self, titulo: str, autor: str, disponible: bool = True):
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

    def __str__(self) -> str:
        estado = "Disponible" if self.disponible else "Prestado"
        return f"Libro: '{self.titulo}' | Autor: {self.autor} | Estado: [{estado}]"


if __name__ == "__main__":
    libro1 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", disponible=True)
    libro2 = Libro("Cien Años de Soledad", "Gabriel García Márquez", disponible=False)

    print(libro1)
    print(libro2)