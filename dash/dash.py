__author__ = 'wjm'
from flask import render_template

class Dashboard(object):

    def __init__(self, json_data):
        self.data = json_data
        self.charts = []

    def add_chart(self, html_id=None, html_cls=None):
        self.charts.append({'id': html_id, 'class': html_cls})

    def render_js(self):
        return render_template('dash/js.html', data=self.data)

    def render_divs(self):
        return render_template('dash/divs.html', divs=self.charts)


