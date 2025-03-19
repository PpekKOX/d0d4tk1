from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

VALID_USERS = ["9648139", "6736194", "9780355", "9816341"]  # Lista ID jako stringi

@app.route("/check_license", methods=["POST"])
def check_license():
    data = request.json
    user_id = str(data.get("user_id"))  # 🔹 Konwersja na stringa dla pewności
    
    print(f"📥 Otrzymano user_id: {user_id}")  # 🔍 Logowanie, co faktycznie dociera do API

    if user_id in VALID_USERS:
        print("✅ Licencja poprawna!")
        return jsonify({"status": "valid"})
    else:
        print("❌ Licencja niepoprawna!")
        return jsonify({"status": "invalid"}), 403

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
