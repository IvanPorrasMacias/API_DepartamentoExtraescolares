from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Ruta de la base de datos SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./extraescolares.db"

# Crear el motor de conexión a la base de datos SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Crear la clase Base para definir los modelos
Base = declarative_base()

# Crear la sesión de la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
