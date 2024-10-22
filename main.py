from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
import crud
import database
from schemas import AlumnoCreate, Alumno

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Dependencia para obtener la sesión de la BD
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Crear un Alumno
@app.post("/alumnos/", response_model=Alumno)
def create_alumno(alumno: AlumnoCreate, db: Session = Depends(get_db)):
    return crud.create_alumno(db=db, alumno=alumno)

# Leer un Alumno por su número de control
@app.get("/alumnos/{numero_control}", response_model=Alumno)
def read_alumno(numero_control: int, db: Session = Depends(get_db)):
    db_alumno = crud.get_alumno(db, numero_control=numero_control)
    if db_alumno is None:
        raise HTTPException(status_code=404, detail="No se encontró el alumno")
    return db_alumno
