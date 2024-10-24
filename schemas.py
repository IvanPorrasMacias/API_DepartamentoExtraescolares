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

# Modelo Pydantic para la Actividad
class ActividadBase(BaseModel):
    nombre: str
    horario: str
    grupo: str

# Modelo para creación de una Actividad
class ActividadCreate(ActividadBase):
    pass

# Modelo para representar una Actividad
class Actividad(ActividadBase):
    id: int
    class Config:
        from_attributes = True

# Modelo para la actualización de la actividad
class ActividadUpdate(BaseModel):
    nombre: Optional[str] = None
    horario: Optional[str] = None
    grupo: Optional[str] = None

# Modelo base para ActividadesAlumno
class ActividadesAlumnoBase(BaseModel):
    alumno_id: int
    actividad_id: int

# Modelo para crear ActividadesAlumno
class ActividadesAlumnoCreate(ActividadesAlumnoBase):
    pass

# Modelo para representar ActividadesAlumno
class ActividadesAlumno(ActividadesAlumnoBase):
    id: int

    class Config:
        from_attributes = True
