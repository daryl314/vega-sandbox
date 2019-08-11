from flask import render_template
from flask_app import flask_app as app
import os

ROOT = os.path.dirname(__file__)
JSLIB = os.path.join(ROOT, '..', 'jslib')

def ref(name):
    if os.path.isfile(os.path.join(JSLIB, name)):
        return '/' + name
    else:
        return 'https://cdn.jsdelivr.net/npm/' + name

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', 
                           vega=ref('vega@5'), 
                           vega_lite=ref('vega-lite@3'), 
                           vega_embed=ref('vega-embed@4'))

@app.route('/spec')
def spec():
    if 'SPEC' in os.environ:
        with open(os.environ['SPEC'], 'rt') as F:
            return F.read()
    return TEST_SPEC

@app.route('/<data>.json')
def json(data):
    with open(data + '.json', 'rt') as F:
        return F.read()

@app.route('/vega@5')
def vega():
    with open(os.path.join(JSLIB, 'vega@5'), 'rt') as F:
        return F.read()

@app.route('/vega-lite@3')
def vegalite():
    with open(os.path.join(JSLIB, 'vega-lite@3'), 'rt') as F:
        return F.read()

@app.route('/vega-embed@4')
def vegaembed():
    with open(os.path.join(JSLIB, 'vega-embed@4'), 'rt') as F:
        return F.read()

TEST_SPEC='''{
  "$schema": "https://vega.github.io/schema/vega-lite/v3.json",
  "description": "A simple bar chart with embedded data.",
  "data": {
    "values": [
      {"a": "A", "b": 28}, {"a": "B", "b": 55}, {"a": "C", "b": 43},
      {"a": "D", "b": 91}, {"a": "E", "b": 81}, {"a": "F", "b": 53},
      {"a": "G", "b": 19}, {"a": "H", "b": 87}, {"a": "I", "b": 52}
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "a", "type": "ordinal"},
    "y": {"field": "b", "type": "quantitative"}
  }
}'''
