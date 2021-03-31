###################### In order to run the app enter: python -m flask run
###################### has to be in: flask-resume-template folder


import oyaml as yaml
from flask import Flask
from flask import render_template
import pandas as pd

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def index():
    website_data = yaml.load(open('_config.yaml'))

    return render_template('index.html', data=website_data)

@app.route('/d3-examples')
def graph():
    graph_data = pd.read_csv('board_games.csv')
    return render_template('d3-graph/graph.html', data = graph_data)

@app.route('/powerbi')
def power_bi():
    return render_template('power_bi.html')

@app.route('/dashboard-screenshots')
def dashboard_screenshots():
    return render_template('dashboard-images.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    #app.run()