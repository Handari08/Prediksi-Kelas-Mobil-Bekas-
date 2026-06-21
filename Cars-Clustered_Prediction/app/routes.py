from flask import Blueprint, request, jsonify, render_template
from app.model_loader import model, scaler, cluster_labels
from app.utils import preprocess_input
import pandas as pd

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(BASE_DIR, "data", "used_car_clustered.csv")

df = pd.read_csv("data/used_car_clustered.csv")


# ✅ WAJIB ADA INI
main = Blueprint("main", __name__)

# ✅ landing page
@main.route("/")
def home():
    return render_template("index.html")

# ✅ dashboard page
@main.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@main.route("/result")
def result_page():
    return render_template("result.html")

# ✅ predict API
@main.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    try:
        input_data = [[
            int(data["model_year"]),
            int(data["milage"]),
            int(data["horsepower"]),
            float(data["engine_size"]),
            float(data["price"])
        ]]

        print("INPUT:", input_data)

        # ✅ PREDICTION DULU
        prediction = model.predict(input_data)[0]

        print("PRED:", prediction)

        # ✅ BARU FILTER DATA
        filtered = df[df["Cluster"] == int(prediction)].head(5)

        data_list = filtered[[
            "brand",
            "model",
            "model_year",
            "milage",
            "engine_size",
            "horsepower",
            "price"
        ]].to_dict(orient="records")


        return jsonify({
            "cluster_id": int(prediction),
            "cluster_label": cluster_labels[int(prediction)],
            "accuracy": 0.87,
            "data": data_list
        })

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)})