
class Record():
    def __init__(self, nombre, puntos):
        self.nombre_player = nombre
        self.score = puntos

    def __str__(self):
        return f"{self.nombre_player} y {self.score}"

