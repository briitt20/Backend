from fastapi  import APIRouter, HTTPException, status
from ..services.estudiante_service import EstudianteServicio
from ..schemas.estudiante import Estudiante, EstudianteActualizar

rutasEstudiante = APIRouter(prefix='/estudiantes', tags=['Estudiantes'])

estudianteServicio= EstudianteServicio()

@rutasEstudiante.post('/')
def guardarEstudiante(estudianteNuevo: Estudiante):
    try:
        return estudianteServicio.guardarEstudiante(estudianteNuevo)
    except Exception as e:
         raise HTTPException(status_code=status.HTTP_500_INTERNACIONAL_SERVER_ERROR, detail=str(e))   

@rutasEstudiante.get('/')
def mostrarEstudiantes():
        return estudianteServicio.mostrarEstudiante()

@rutasEstudiante.put('/{id}')
def actualizarEstudiantes(id: int, estudianteActualizar: EstudianteActualizar):
    try:
        return estudianteServicio.actualizarEstudiantes(id,estudianteActualizar)
    except Exception as e:
         raise HTTPException(status_code=status.HTTP_500_INTERNACIONAL_SERVER_ERROR, detail=str(e))
    
        
@rutasEstudiante.delete('/{id}')
def eliminarEstudiante(id: int):
    try:
        return estudianteServicio.eliminarEstudiante(id)
    except Exception as e:
         raise HTTPException(status_code=status.HTTP_500_INTERNACIONAL_SERVER_ERROR, detail=str(e))