from flask import Flask, request, jsonify

app = Flask(__name__)

# Przykładowe licencje w bazie danych (w praktyce to powinno być w DB)
VALID_LICENSES = {
    "ABC123DEF456": "User1",
    "XYZ789GHI012": "User2"
}

@app.route("/check_license", methods=["POST"])
def check_license():
    data = request.json
    license_key = data.get("license")

    if license_key in VALID_LICENSES:
        return jsonify({"status": "valid", "user": VALID_LICENSES[license_key]})
    else:
        return jsonify({"status": "invalid"}), 403

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
