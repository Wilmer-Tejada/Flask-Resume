###################### In order to run the app enter: python -m flask run
###################### has to be in: flask-resume-template folder
# https://eu.pythonanywhere.com/forums/topic/24/
# scikit learn: we don't support pickling/unpickling across different scikit-learn version

import oyaml as yaml
from flask import Flask, render_template, request
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def index():
    website_data = yaml.load(open('_config.yaml'))
    return render_template('index.html', data=website_data)

@app.route('/d3-examples')
def graph():
    return render_template('d3-charts.html')

@app.route('/d3-choropleth')
def d3_choropleth():
    return render_template('d3-choropleth.html')

@app.route('/powerbi')
def power_bi():
    return render_template('power_bi.html')

@app.route('/dashboard-screenshots')
def dashboard_screenshots():
    return render_template('dashboard-images.html')

@app.route('/iris_prediction',methods = ['POST', 'GET'])
def ml_model():
    return render_template('ml_model/iris.html')


@app.route('/predict/', methods=['GET', 'POST'])
def predict():
    if request.method == "POST":
        # get form data
        sepal_length = request.form.get('Sepal Length')
        sepal_width = request.form.get('Sepal Width')
        petal_length = request.form.get('Petal Length')
        petal_width = request.form.get('Petal Width')

        # Load Data
        filename = 'finalized_model.sav'
        loaded_model = pickle.load(open('model.pkl', 'rb'))

        ########## User input would go here:
        data =  np.array([sepal_length, sepal_width, petal_length, petal_width])
        data = data.reshape(1, -1)
        # print(test_data)
        prediction = loaded_model.predict(data)
        # pass prediction to template

        return render_template('ml_model/predict.html',prediction=prediction)
    pass


if __name__ == '__main__':
    app.run(debug=True, port=5000)
    #app.run()