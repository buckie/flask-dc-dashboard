__author__ = 'wjm'
from flask import render_template


__js_attr__ = '{js_var}.{js_attr}(js_args);'

__js_init__ = 'var {js_var} = dc.{chart_class}("#{div_id}");'

__div_tag__ = '<div id="{div_id}" class="{div_class}"><\div>'

def render_js_attr(js_var, js_attr, template=__js_attr__, *js_args):
    return template.format(js_var=js_var, js_attr=js_attr, js_args=','.join([str(i) for i in js_args]))

def render_js_init(js_var, chart_class, div_id, template=__js_init__):
    return template.format(js_var=js_var, chart_class=chart_class, div_id=div_id)

def render_div_tag(div_id, div_class, template=__div_tag__):
    return template.format(div_id=div_id, div_class=div_class)

class BaseChart(object):

    __mandatory__ = ['group_by', 'dimension', 'div_class', 'js_var']

    __dc_attrs__ = ['']

    def __init__(self, data, name, dimension, group_by, div_class=None):

        self.data = data
        self.div_class = div_class
        self.js_var = name
        self.div_id = name
        # What to plot on
        self.dimension = dimension
        self.group_by = group_by

        # defaults
        self.height = 200
        self.width = 200
        self.inner_radius = None
        self.transition_duration = None
        self.legend = None

    def render_js(self):
        temp = []
        temp.append(
        if self.inner_radius:
            temp += '.innerRadius({inner_radius})'.format(inner_radius=self.inner_radius)

        return temp + ';'

    def render_html(self):
        return self.__html_template__.format(div_id=self.div_id, div_class=self.div_class)


