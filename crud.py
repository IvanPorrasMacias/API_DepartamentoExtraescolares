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

# Crear una nueva relación entre Alumno y Actividad
def create_actividades_alumno(db: Session, actividades_alumno: schemas.ActividadesAlumnoCreate):
    db_actividades_alumno = models.ActividadesAlumno(**actividades_alumno.model_dump())
    db.add(db_actividades_alumno)
    db.commit()
    db.refresh(db_actividades_alumno)
    return db_actividades_alumno

# Obtener una relación Alumno-Actividad por ID
def get_actividades_alumno(db: Session, actividades_alumno_id: int):
    return db.query(models.ActividadesAlumno).filter(models.ActividadesAlumno.id == actividades_alumno_id).first()

# Actualizar una relación Alumno-Actividad
def update_actividades_alumno(db: Session, actividades_alumno_id: int, actividades_alumno_update: schemas.ActividadesAlumnoCreate):
    db_actividades_alumno = get_actividades_alumno(db, actividades_alumno_id)
    if db_actividades_alumno:
        for key, value in actividades_alumno_update.model_dump().items():
            setattr(db_actividades_alumno, key, value)
        db.commit()
        db.refresh(db_actividades_alumno)
    return db_actividades_alumno

# Borrar una relación Alumno-Actividad
def delete_actividades_alumno(db: Session, actividades_alumno_id: int):
    db_actividades_alumno = get_actividades_alumno(db, actividades_alumno_id)
    if db_actividades_alumno:
        db.delete(db_actividades_alumno)
        db.commit()
    return db_actividades_alumno
