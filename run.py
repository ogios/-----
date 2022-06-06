import pyecharts
import charts
import time


from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config["TEMPLATES_AUTO_RELOAD"] = True

CORS(app)

chart_dict = {
    'map': charts.maps,
    'bar': charts.barcharts,
    'word': charts.words,
}


@app.after_request
def cor(environ):
    environ.headers['Access-Control-Allow-Origin'] = '*'
    environ.headers["Access-Control-Allow-Method"] = "*"
    environ.headers["Access-Control-Allow-Headers"] = "x-requested-with,content-type"
    return environ


@app.route("/")
def index():
    return render_template('test3.html')


@app.route('/test2/')
def test2():
    return render_template('test2.html')


@app.route('/self/')
def self():
    return render_template('自适应test_1.html')


# @app.route('/chart/')
# def chart():
#     c = charts.barchart()
#     return c.dump_options_with_quotes()


# @app.route('/1_map')
# def map_1():
#     c = charts.map_get()
#     return c.dump_options_with_quotes()

# 获取图表的总路由
@app.route('/chart/')
def chart():
    start = time.time()
    type_ = request.args.get('chart')
    num = request.args.get('num')
    c = chart_dict[type_](num)
    d = c.dump_options_with_quotes()
    print(f'{type_}{num}用时', time.time()-start, '\n')
    return d


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8337')
