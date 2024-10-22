from sqlalchemy.orm import Session
import models
import schemas

# Obtener un Alumno por número de control
def get_alumno(db: Session, numero_control: int):
    return db.query(models.Alumno).filter(models.Alumno.numero_control == numero_control).first()

# Crear un nuevo Alumno en la base de datos
def create_alumno(db: Session, alumno: schemas.AlumnoCreate):
    db_alumno = models.Alumno(**alumno.model_dump())
    db.add(db_alumno)
    db.commit()
    db.refresh(db_alumno)
    return db_alumno

def delete_alumno(db: Session, numero_control: int):
    alumno = get_alumno(db, numero_control)
    if alumno:
        db.delete(alumno)
        db.commit()
    return alumno

# Similarmente para Actividades y ActividadesAlumno
