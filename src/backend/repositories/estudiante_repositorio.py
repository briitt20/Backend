from ..schemas.estudiante import Estudiante, EstudianteActualizar

class EstudianteRepositorio:
    def __init__(self):
        self.__listaEstudiantes:list[Estudiante] = []
    
    def guardarEstudiante(self, estudianteNuevo: Estudiante):
        self.__listaEstudiantes.append(estudianteNuevo)
        return estudianteNuevo
    
    def mostrarEstudiantes(self):
        return self.__listaEstudiantes

    def actualizarEstudiantes(self, id: int, estudianteActualizar:EstudianteActualizar):
        try:

            for _, valor in enumerate(self.__listaEstudiantes):
                if valor.id == id:
                    valor.nombre = estudianteActualizar.nombre
                    valor.edad = estudianteActualizar.edad
                    valor.correo= estudianteActualizar.correo
                    return valor
        except Exception as e:
            raise str(e)

    def eliminarEstudiante(self, id:int):
        try:
            for indice, valor in enumerate(self.__listaEstudiantes):
                if valor.id == id:
                    self.__listaEstudiantes.pop(indice)
                    return id
                return None
            
        except Exception as e:
            raise str(e)