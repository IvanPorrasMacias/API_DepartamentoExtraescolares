from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Alumno(Base):
    __tablename__ = 'alumno'

    numero_control = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    semestre = Column(Integer)
    carrera = Column(String)
    
    # Relación con la tabla Actividades_Alumno (Especificar las foreign_keys)
    actividades_alumno = relationship("Actividades_Alumno", foreign_keys="[Actividades_Alumno.numero_control]")

class Actividades(Base):
    __tablename__ = 'actividades'
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    horario = Column(String)
    grupo = Column(String)

    # Relación con Actividades_Alumno (si la clase se llama 'Actividades_Alumno')
    alumnos_actividad = relationship('Actividades_Alumno', back_populates='actividad')


class Actividades_Alumno(Base):
    __tablename__ = 'actividades_alumno'

    numero_control = Column(Integer, ForeignKey('alumno.numero_control'), primary_key=True)
    actividad_id = Column(Integer, ForeignKey('actividades.id'), primary_key=True)

    # Relaciones
    alumno = relationship("Alumno", back_populates="actividades_alumno", foreign_keys=[numero_control])
    actividad = relationship("Actividades", back_populates="alumnos_actividad", foreign_keys=[actividad_id])

