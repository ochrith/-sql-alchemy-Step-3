from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pathlib import Path
# 1. Connexion au moteur SQLite

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "db" / "mydatabase.db"

engine = create_engine(
    f"sqlite:///{DB_PATH}",
    connect_args={"check_same_thread": False}
)

# 2. Base pour les modèles
Base = declarative_base()

# 3. La fabrique de session (définie UNE SEULE FOIS au niveau du module)
SessionLocal = sessionmaker(bind=engine)   # mettr eici pur pas reconstruire a chaque fosi

def init_db():
    """Crée les tables en important les modèles."""
    print("Create Tables ...")
    import database.models  # Important : enregistre les modèles dans Base.metadata
    Base.metadata.create_all(engine)