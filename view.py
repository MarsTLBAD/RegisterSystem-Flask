import json
from datetime import datetime

import controller
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    record = controller.get_all_record()
    return render_template('index.html', record=record)


@app.route('/add', methods=['POST'])
def add():
    data = json.loads(request.get_data())
    # 转换日期格式为python格式
    data['date'] = datetime.strptime(data['date'], "%Y-%m-%d").date()
    res = controller.add_record(data)
    return json.dumps({"result": res})


@app.route('/del', methods=['POST'])
def delete():
    data = json.loads(request.get_data())
    print(request.get_json())
    res = controller.del_record(data)
    return json.dumps({"result": res})
