from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "ML Pipeline service is running!"})

@app.route("/train", methods=["POST"])
def train_model():
    # Placeholder for training logic
    return jsonify({"status": "Training started"})

@app.route("/predict", methods=["POST"])
def predict():
    # Placeholder for prediction logic
    return jsonify({"status": "Prediction complete"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)