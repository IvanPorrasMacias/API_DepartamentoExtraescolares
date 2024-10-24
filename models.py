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
    
    actividades_alumno = relationship("ActividadesAlumno", back_populates="alumno")


class Actividades(Base):
    __tablename__ = 'actividades'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    horario = Column(String)
    grupo = Column(String)

    alumnos = relationship("ActividadesAlumno", back_populates="actividad")



class ActividadesAlumno(Base):
    __tablename__ = 'actividades_alumno'
    id = Column(Integer, primary_key=True, index=True)
    
    alumno_id = Column(Integer, ForeignKey('alumno.numero_control'), nullable=False)
    actividad_id = Column(Integer, ForeignKey('actividades.id'), nullable=False)

    alumno = relationship("Alumno", back_populates="actividades_alumno")
    actividad = relationship("Actividades", back_populates="alumnos")


