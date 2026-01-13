import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from database import db
from models import Character
from datetime import datetime


load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

CORS(app)



VALID_USERS = os.getenv("VALID_USERS", "").split(",")
MD_LICENSE = os.getenv("MD_LICENSE", "").split(",")

@app.route("/check_license", methods=["POST"])
def check_license():
    data = request.json
    user_id = str(data.get("user_id"))

    print(f"📥 Otrzymane user_id: {user_id}")

    if user_id in VALID_USERS:
        print("✅ Licencja poprawna!")
        return jsonify({"status": "valid"})
    else:
        print("❌ Licencja niepoprawna!")
        return jsonify({"status": "invalid"}), 403

@app.route("/verify_license", methods=["POST"])
def verify_license():
    data = request.json
    license = str(data.get("license"))

    print(f"📥 Otrzymana Licencja: {license}")

    if license in MD_LICENSE:
        print("✅ Licencja poprawna!")
        return jsonify({"status": "valid"})
    else:
        print("❌ Licencja niepoprawna!")
        return jsonify({"status": "invalid"}), 403

from datetime import datetime

@app.route("/report_state", methods=["POST"])
def report_state():
    data = request.json or {}
    print("📦 payload:", data)

    license = str(data.get("license"))
    if license not in MD_LICENSE:
        return jsonify({"error": "unauthorized"}), 403

    name = data.get("character")
    world = data.get("world")

    if not name or not world:
        return jsonify({"error": "invalid payload"}), 400

    char = Character.query.filter_by(
        name=name,
        world=world
    ).first()

    if not char:
        char = Character(name=name, world=world)

    char.level = data.get("level")
    char.map = data.get("map")
    char.x = data.get("x")
    char.y = data.get("y")
    char.last_online = datetime.utcnow()

    db.session.add(char)
    db.session.commit()

    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)




