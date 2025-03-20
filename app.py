import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

VALID_USERS = os.getenv("VALID_USERS", "").split(",")

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
