
import uuid

import flask
from pathlib import Path
from datetime import datetime
#from logger import setup_logger
from api.logger import setup_logger
from database.db_connection import SessionLocal
from database.models import User, Upload, Status

BASE_DIR = Path(__file__).resolve().parent.parent
UPLOADS_DIRECTORY = BASE_DIR / "uploads"
OUTPUTS_DIRECTORY = BASE_DIR / "outputs"

db=SessionLocal()


server=flask.Flask(__name__)
#Par défaut, Flask cherche le dossier templates/ dans le même répertoire que le fichier Python où tu as instancié ton application (server = flask.Flask(__name__)).
#Request , Response --> sont stockées dans l'objet global request fourni par Flask.
setup_logger(server)
@server.route("/")
def home():
    return flask.render_template("index.html")


@server.route("/about")
def about():
    return flask.render_template("about.html")

import json

@server.route("/status/", defaults={'uid': None}, methods=['GET'])
@server.route("/status/<uid>", methods=['GET'])

def status(uid):



    upload = db.query(Upload).filter(
        Upload.uid == uid
    ).first()

    if not upload:
        return flask.jsonify({
            "messageError": "no such uuid",
            "uid": uid
        }), 404

    explanation = None

    if upload.status == Status.DONE:
        output_path = OUTPUTS_DIRECTORY / f"{upload.uid}.json"

        if output_path.exists():
            with open(output_path, "r", encoding="utf-8") as f:
                explanation = json.load(f)

    response = {
        "uid": upload.uid,
        "status": upload.status.value,
        "filename": upload.filename,
        "upload_time": upload.upload_time,
        "finish_time": upload.finish_time,
        "explanation": explanation
    }

    return flask.jsonify(response), 200


def generate_uid():
    return str(uuid.uuid4())[:8]
@server.route("/upload",methods=['POST'])   # Cette ligne est un décorateur Python qui sert à mapper une URL spécifique et une méthode HTTP à une fonction Python.

def upload(user_id):
    new_uid = generate_uid()

    file = flask.request.files.get("file")

    if not file:
        return flask.jsonify({
            "messageError": "no file in your request"
        }), 400

    original_name = Path(file.filename).stem   # extrait uniquement le nom du fichier sans son extension (et sans le chemin du dossier).
    extension = Path(file.filename).suffix
    #Path transforme ce texte en un objet intelligent capable d'effectuer des opérations complexes sans code supplémentaire.
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    new_file_name = f"{original_name}_{timestamp}_{new_uid}{extension}"

    destination = UPLOADS_DIRECTORY / new_file_name

    file.save(destination)

    # 1. Création de l'instance du modèle
    nouveau_fichier = Upload(
        id=new_uid,
        uid=user_id,
        status=Status.PENDING,  # Attention à la faute de frappe "PENDIND" -> "PENDING"
        filename=new_file_name,
        upload_time=timestamp
    )

    # 2. Ajout et enregistrement en base de données
    db.session.add(nouveau_fichier)
    db.session.commit()

    return flask.jsonify({
        "uid": new_uid
    }), 200



server.run( host="0.0.0.0",port=5000,debug=True)