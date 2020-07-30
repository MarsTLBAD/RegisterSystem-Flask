from datetime import datetime

from models import *


def add_record(data):
    # 转换日期格式为python格式
    data['date'] = datetime.strptime(data['date'], "%Y-%m-%d").date()
    # 查询是否已经提交
    if find_value(data['id']):
        return -1
    add_value(data)
    return 1


def del_record(data):
    id = data['id']
    del_value(id)
    if (find_value(id)):
        return -1
    return 1


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
