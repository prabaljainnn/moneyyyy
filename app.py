from flask import Flask, jsonify, render_template
from EndPoints import YT_ends as Yt
from EndPoints.YT_ends import get_hotness
from EndPoints import NLP as Nlp
from flask import render_template
import json
from pytrends.request import TrendReq

pytrend = TrendReq()

app = Flask(__name__, template_folder='template')


@app.errorhandler(404)
def page_not_found():
    return render_template('index.html'), 404


@app.route('/')
def home():
    return render_template('home.html'), 200


@app.route('/api/v1/tags/short/<name>')
def get_tags(name):
    return jsonify(data=Yt.top_Tags(name)[0:470])


@app.route('/api/v1/tags/large/DD/<name>')
def get_desc(name):
    return jsonify(data=Yt.top_Tags(name))


@app.route('/api/v1/hot?/<name>')
def get_hot(name):
    value = get_hotness(name)
    ans = 0
    if value < 5:
        ans = 0
    elif value < 20:
        ans = 1
    elif 60 > value >= 20.0:
        ans = 2
    elif value >= 60.0:
        ans = 3
    return jsonify(data=ans)


@app.route('/api/v1/naturalLP/<name>')
def get_some_random_desc(name):
    return jsonify(data=Nlp.get_some_random_desc(name))


@app.route('/api/v1/Trends')
def get_Google_Trends():
    return json.dumps(pytrend.trending_searches(pn='india')[0].to_list())


if __name__ == '__main__':
    app.run(debug=False)
