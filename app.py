from flask import Flask, request, jsonify
from flask_cors import CORS  # Obsługa CORS

app = Flask(__name__)
CORS(app)  # Pozwala na zapytania z przeglądarki

VALID_USERS = ["9648139"]  # Lista ID

@app.route("/check_license", methods=["POST"])
def check_license():
    data = request.json
    user_id = data.get("user_id")

    print(f"📥 Otrzymano user_id: {user_id}")  # Debugowanie w logach Render

    if user_id in VALID_USERS:
        return jsonify({"status": "valid"})
    else:
        return jsonify({"status": "invalid"}), 403

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
