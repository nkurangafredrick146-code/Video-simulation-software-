from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Scene Environment service is running!"})

@app.route("/simulate", methods=["POST"])
def simulate_scene():
    # Placeholder for scene simulation logic
    return jsonify({"status": "Scene simulation started"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)