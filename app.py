import flask
from flask import Flask, render_template, request
import pickle
import numpy as np

# Running the flask app
app = Flask(__name__)

#load model using pickle
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    val = request.form.get("exp")
    val = val.split(',')
    val1 = [int(x) for x in val]

    prediction = model.predict([val1])

    return render_template('index.html', prediction_text='The salary is {}'.format(prediction))

if __name__ == '__main__':
    app.run(debug=True)
