
class Libro:
    def __init__(self, titulo: str, autor: str, anio_publicacion: int, numero_paginas: int):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.numero_paginas = numero_paginas
    
    def mostrar_informacion(self):
        return print(f"El libro {self.titulo} fue escrito por {self.autor} en el año {self.anio_publicacion} y tiene {self.numero_paginas} páginas.")
    
metamorfosis = Libro("La Metamorfosis", "Franz Kafka", 1915, 128)
metamorfosis.mostrar_informacion()
