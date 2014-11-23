__author__ = 'wjm'
from flask import render_template

class PieChart(object):

    __js_template__ = """
    var {js_var} = dc.pieChart("#{div_id}");

    {js_var}
        .width({width})
        .height({height})
        .dimension({dimension})
        .group({groub_by})
    """

    __html_template__ = """
    <div id="{div_id}" class="{div_class"><\div>
    """

    def __init__(self, js_data_name, dimension, div_id, js_var, div_class=None):

        self.js_data_name = js_data_name
        self.div_class = div_class
        self.js_var = js_var
        self.div_id = div_id
        # What to plot on
        self.dimension = dimension

        # defaults
        self.height = 200
        self.width = 200
        self.inner_radius = None
        self.group_by = None

    def size(self, width=None, height=None, inner_radius=None):
        self.width = width if width else self.width
        self.height = height if height else self.height
        self.inner_radius = inner_radius if inner_radius else self.inner_radius

    def plot_on(self, column_name):
        self.dimension = column_name

    def group_by(self, column_name):
        self.group_by = column_name

    def render_js(self):
        temp = self.__js_template__.format(js_var=self.js_var,
                                           div_id=self.div_id,
                                           height=self.height,
                                           width=self.width,
                                           dimension=self.dimension,
                                           group_by=self.group_by)
        if self.inner_radius:
            temp += '.innerRadius({inner_radius})'.format(inner_radius=self.inner_radius)

        return temp + ';'

    def render_html(self):
        return self.__html_template__.format(div_id=self.div_id, div_class=self.div_class)


