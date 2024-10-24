from sqlalchemy.orm import Session
import models
import schemas

# Crear un nuevo Alumno en la base de datos
def create_alumno(db: Session, alumno: schemas.AlumnoCreate):
    db_alumno = models.Alumno(**alumno.model_dump())
    db.add(db_alumno)
    db.commit()
    db.refresh(db_alumno)
    return db_alumno

# Obtener un Alumno por número de control
def read_alumno(db: Session, numero_control: int):
    return db.query(models.Alumno).filter(models.Alumno.numero_control == numero_control).first()

# Actualizar un alumno por su número de control
def update_alumno(db: Session, numero_control: int, alumno_update: schemas.AlumnoUpdate):
    alumno = read_alumno(db, numero_control)
    if alumno:
        for key, value in alumno_update.model_dump(exclude_unset=True).items():
            setattr(alumno, key, value)
        db.commit()
        db.refresh(alumno)
    return alumno

# Borrar un alumno en la base de datos
def delete_alumno(db: Session, numero_control: int):
    alumno = read_alumno(db, numero_control)
    if alumno:
        db.delete(alumno)
        db.commit()
    return alumno

# Crear una nueva Actividad en la base de datos
def create_actividad(db: Session, actividad: schemas.ActividadCreate):
    db_actividad = models.Actividades(**actividad.model_dump())
    db.add(db_actividad)
    db.commit()
    db.refresh(db_actividad)
    return db_actividad

# Leer un actividad por su id
def read_actividad(db: Session, id: int):
    return db.query(models.Actividades).filter(models.Actividades.id == id).first()

# Actualizar una aactividad por su id
def update_actividad(db: Session, id: int, actividad_update: schemas.ActividadUpdate):
    actividad = read_actividad(db, id=id)
    if actividad:
        for key,value in actividad_update.model_dump(exclude_unset=True).items():
            setattr(actividad, key, value)
        db.commit()
        db.refresh(actividad)
    return actividad

# Borrar una actividad por su id
def delete_actividad(db: Session, id: int):
    actividad = read_actividad(db, id)
    if actividad:
        db.delete(actividad)
        db.commit()
    return actividad