import json

import controller
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    record = controller.get_all_record()
    return render_template('index.html', record=record)


@app.route('/add', methods=['POST'])
def add():
    data = request.json

    res = controller.add_record(data)
    return json.dumps({"result": res})


@app.route('/del', methods=['POST'])
def delete():
    data = request.json
    res = controller.del_record(data)
    return json.dumps({"result": res})
