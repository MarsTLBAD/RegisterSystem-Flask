import controller
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    record = controller.get_all_record()
    return render_template('index.html', record=record)


@app.route('/add', methods=['POST'])
def add():
    controller.add_record()


@app.route('/del', methods=['POST'])
def delete():
    controller.del_record()
