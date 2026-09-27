from database.models import User, Upload, Status
from database.db_connection import init_db, SessionLocal

# 1. Initialisation de la base de données (Création des tables)
init_db()

# 2. Création d'une session de travail
db = SessionLocal()

try:
    # Insertion / Mise à jour de l'utilisateur
    user = User(id=209727361, email="perezclaire868@gmail.com")
    db.merge(user)
    db.commit()
    print("Base de données initialisée et utilisateur synchronisé avec succès !")
finally:
    db.close()  # Fermeture propre de la sessionermer la session après utilisation