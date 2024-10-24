from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
import crud
import database
import schemas

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
@app.post("/alumnos/", response_model=schemas.Alumno)
def create_alumno(alumno: schemas.AlumnoCreate, db: Session = Depends(get_db)):
    return crud.create_alumno(db=db, alumno=alumno)

# Leer un Alumno por su número de control
@app.get("/alumnos/{numero_control}", response_model=schemas.Alumno)
def read_alumno(numero_control: int, db: Session = Depends(get_db)):
    db_alumno = crud.read_alumno(db, numero_control=numero_control)
    if db_alumno is None:
        raise HTTPException(status_code=404, detail="No se encontró el alumno")
    return db_alumno

# Actualizar un alumno por su número de control
@app.patch("/alumnos/{numero_control}", response_model=schemas.Alumno) 
def update_alumno(numero_control: int, alumno_update: schemas.AlumnoUpdate, db: Session = Depends(get_db)):
    db_alumno = crud.update_alumno(db, numero_control=numero_control, alumno_update=alumno_update)
    if db_alumno is None:
        raise HTTPException(status_code=404, detail="No se encontró el alumno")
    return db_alumno

# Borrar un alumno por su número de control
@app.delete("/alumnos/{numero_control}", response_model=schemas.Alumno)
def delete_alumno(numero_control: int, db: Session = Depends(get_db)):
    db_alumno = crud.delete_alumno(db, numero_control=numero_control)
    if db_alumno is None:
        raise HTTPException(status_code=404, detail="No se encontró el alumno")
    return db_alumno

# Crear una Actividad
@app.post("/actividades/", response_model=schemas.ActividadCreate)
def create_actividad(actividad: schemas.ActividadCreate, db: Session = Depends(get_db)):
    return crud.create_actividad(db=db, actividad=actividad)

# Leer una Actividad por su id
@app.get("/actividades/{id}", response_model=schemas.Actividad)
def read_actividad(id: int, db: Session = Depends(get_db)):
    db_actividad = crud.read_actividad(db, id=id)
    if db_actividad is None:
        raise HTTPException(status_code=404, detail="No se encontró la actividad")
    return db_actividad

# Actualizar una actividad por su id
@app.patch("/actividades/{id}", response_model=schemas.Actividad)
def update_actividad(id: int, actividad_update: schemas.ActividadUpdate, db: Session = Depends(get_db)):
    db_actividad = crud.update_actividad(db, id=id, actividad_update=actividad_update)
    if db_actividad is None:
        raise HTTPException(status_code=404, detail="No se encontró la actividad")
    return db_actividad

# Borrar una actividad por su id
@app.delete("/actividades/{id}", response_model=schemas.Actividad)
def delete_actividad(id: int, db: Session = Depends(get_db)):
    db_actividad = crud.delete_actividad(db=db, id=id)
    if db_actividad is None:
        raise HTTPException(status_code=404, detail="No se encontró la actividad")
    return db_actividad

# Crear una relación Alumno-Actividad
@app.post("/actividades_alumno/", response_model=schemas.ActividadesAlumno)
def create_actividades_alumno(actividades_alumno: schemas.ActividadesAlumnoCreate, db: Session = Depends(get_db)):
    return crud.create_actividades_alumno(db=db, actividades_alumno=actividades_alumno)

# Obtener una relación Alumno-Actividad por ID
@app.get("/actividades_alumno/{actividades_alumno_id}", response_model=schemas.ActividadesAlumno)
def read_actividades_alumno(actividades_alumno_id: int, db: Session = Depends(get_db)):
    db_actividades_alumno = crud.get_actividades_alumno(db, actividades_alumno_id)
    if db_actividades_alumno is None:
        raise HTTPException(status_code=404, detail="Relación no encontrada")
    return db_actividades_alumno

# Actualizar una relación Alumno-Actividad
@app.patch("/actividades_alumno/{actividades_alumno_id}", response_model=schemas.ActividadesAlumno)
def update_actividades_alumno(actividades_alumno_id: int, actividades_alumno: schemas.ActividadesAlumnoCreate, db: Session = Depends(get_db)):
    db_actividades_alumno = crud.update_actividades_alumno(db, actividades_alumno_id, actividades_alumno)
    if db_actividades_alumno is None:
        raise HTTPException(status_code=404, detail="Relación no encontrada")
    return db_actividades_alumno

# Borrar una relación Alumno-Actividad
@app.delete("/actividades_alumno/{actividades_alumno_id}", response_model=schemas.ActividadesAlumno)
def delete_actividades_alumno(actividades_alumno_id: int, db: Session = Depends(get_db)):
    db_actividades_alumno = crud.delete_actividades_alumno(db, actividades_alumno_id)
    if db_actividades_alumno is None:
        raise HTTPException(status_code=404, detail="Relación no encontrada")
    return db_actividades_alumno
