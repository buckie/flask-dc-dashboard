from flask import Flask, render_template, json
import pandas as pd
from dash.dash import Dashboard

app = Flask(__name__)


@app.route('/')
def hello_world():
    dash = Dashboard(spendData.to_json(orient='records'))
    dash.add_chart(html_id="chart-ring-year")
    dash.add_chart(html_id="chart-hist-spend")
    dash.add_chart(html_id="chart-row-spenders")
    return render_template('layout.html', dash=dash)


spendData = pd.DataFrame([
    {"Name": 'Mr A', "Spent": 40, "Year": 2011},
    {"Name": 'Mr B', "Spent": 10, "Year": 2011},
    {"Name": 'Mr C', "Spent": 40, "Year": 2011},
    {"Name": 'Mr A', "Spent": 70, "Year": 2012},
    {"Name": 'Mr B', "Spent": 20, "Year": 2012},
    {"Name": 'Mr B', "Spent": 50, "Year": 2013},
    {"Name": 'Mr C', "Spent": 30, "Year": 2013}])

print spendData.to_json(orient='records')

if __name__ == '__main__':
    app.run()
