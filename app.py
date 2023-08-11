from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route('/',)
def Home():
    return render_template('frontend.html')

@app.route("/predict", methods = ["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    return render_template("frontend.html", prediction_text = " The High Price Prediction is {}".format(prediction))

if __name__ == '__main__':
    app.run(port=3000, debug=True)