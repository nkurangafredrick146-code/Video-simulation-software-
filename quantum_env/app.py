from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Quantum Environment service is running!"})

@app.route("/compute", methods=["POST"])
def compute_quantum():
    # Placeholder for quantum computation logic
    return jsonify({"status": "Quantum computation started"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)