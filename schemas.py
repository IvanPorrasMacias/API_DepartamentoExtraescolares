from pydantic import BaseModel
from typing import Optional

# Modelo Pydantic para el Alumno
class AlumnoBase(BaseModel):
    nombre: str
    numero_control: int
    semestre: int
    carrera: str

# Modelo para representar un Alumno (incluyendo el ID)
class Alumno(AlumnoBase):
    class Config:
        from_attributes = True

# Modelo para creación de un Alumno
class AlumnoCreate(AlumnoBase):
    pass

# Modelo para la actualización del alumno 
class AlumnoUpdate(BaseModel):
    nombre: Optional[str] = None 
    numero_control: Optional[int] = None
    semestre: Optional[int] = None
    carrera: Optional[str] = None