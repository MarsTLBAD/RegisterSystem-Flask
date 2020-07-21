from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Float, Date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Record(Base):
    __tablename__ = 'Record'
    id = Column(String(32), primary_key=True)
    name = Column(String(32))
    temperature = Column(Float)
    date = Column(Date)


sqlite_url = 'sqlite:///demo.db?check_same_thread=False'

# 创建引擎
engine = create_engine(sqlite_url)

# 创建表
Base.metadata.create_all(engine)

# 创建DBSession类型:
Session = sessionmaker(bind=engine)

# 创建Session类实例
session = Session()
