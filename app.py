from flask import Flask, render_template, request
import os
import pandas as pd
import numpy as np
from src.Predict_Pipe.pipeline.prediction import PredictionPipeline

app = Flask(__name__)

@app.route("/", methods=["GET"])
def homepage():
    return render_template("index.html")

@app.route("/train", methods=["GET"])
def training():
    os.system("python main.py")
    return "Training completed!"

@app.route("/predict", methods=["POST","GET"])
def index():
    if request.method=="POST":
        try:
            fixed_acidity = float(request.form.get("Fixed Acidity"))
            volatile_acidity = float(request.form.get("Volatile Acidity"))
            citric_acid = float(request.form.get("Citric Acid"))
            residual_sugar = float(request.form.get("Residual Sugar"))
            chlorides = float(request.form.get("Chlorides"))
            free_sulfur_dioxide = float(request.form.get("Free Sulfur Dioxide"))
            total_sulfur_dioxide = float(request.form.get("Total Sulfur Dioxide"))
            density = float(request.form.get("Density"))
            pH = float(request.form.get("pH"))
            sulphates = float(request.form.get("Sulphates"))
            alcohol = float(request.form.get("Alcohol"))
            
            data = [
                fixed_acidity,
                volatile_acidity,
                citric_acid,
                residual_sugar, 
                chlorides,
                free_sulfur_dioxide,
                total_sulfur_dioxide,
                density,
                pH,
                sulphates,
                alcohol
            ]
            
            data = np.array(data).reshape(1, 11)
            
            pipe = PredictionPipeline()
            prediction = pipe.predict(data)
            
            # Convert prediction to a more readable format if needed
            prediction_value = prediction[0] if isinstance(prediction, np.ndarray) else prediction
            
            return render_template("result.html", prediction=prediction_value)
        
        except Exception as e:
            print(f"Error during prediction: {e}")
            error_message = str(e)
            return render_template("error.html", error=error_message)
    else:
        return render_template("index.html")

if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)