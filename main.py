from flask import Flask, jsonify, request
import numpy as np
import pickle
app = Flask(__name__)

with open("winner_prediction.p", 'rb') as f:
    clf = pickle.load(f)


@app.route('/')
def index():
    return "League Prediction Server is online."

@app.route('/predict', methods=["POST"])
def predict():
    data = request.get_json()
    if data is None or "features" not in data:
        print("Returning 400:", data)
        return jsonify({"error": "Missing input"}), 400
    features = data.get("features")
    x = np.asarray(features).reshape(1, -1)
    result = clf.predict_proba(x)[0]
    blue_win_prob = round(result[0], 4)
    red_win_prob = round(1 - blue_win_prob, 4)
    return jsonify(
        {
            "blue_win_probability": blue_win_prob,
            "red_win_probability": red_win_prob
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
