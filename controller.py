from models import *

import json

from datetime import datetime
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    record = get_all_record()
    return render_template('index.html', record=record)


@app.route('/add', methods=['POST'])
def add_record():
    if request.method != 'POST':
        return json.dumps({"result": 0})
    data = json.loads(request.get_data())
    print(data)
    # 转换日期格式为python格式
    data['date'] = datetime.strptime(data['date'], "%Y-%m-%d").date()

    # 查询是否已经提交
    if find_value(data['id']):
        return json.dumps({"result": -1})
    add_value(data)
    return json.dumps({"result": 1})


@app.route('/del', methods=['POST'])
def del_record():
    if request.method != 'POST':
        return json.dumps({"result": 0})
    data = json.loads(request.get_data())
    id = data.values()
    del_value(id)
    if (find_value(id)):
        return json.dumps({"result": -1})
    return json.dumps({"result": 1})


def add_value(data):
    id, name, tem, date = data.values()
    session.add(Record(id=id, name=name, temperature=tem, date=date))
    session.commit()
    session.close()


def del_value(id):
    session.query(Record).filter(Record.id == id).delete()
    session.commit()
    session.close()


def find_value(id):
    res = session.query(Record).filter(Record.id == id).all()
    return True if res else False


def get_all_record():
    return session.query(Record).all()
