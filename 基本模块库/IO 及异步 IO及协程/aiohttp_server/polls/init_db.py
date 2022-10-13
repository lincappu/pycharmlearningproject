# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

from sqlalchemy import  create_engine,MetaData

from aiohttpdemo_polls.settings import  config
from aiohttpdemo_polls.db import question,choice

DSN='mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8mb4'

def create_talbes(engine):
	meta=MetaData()
	meta.create_all(bind=engine,tables=[question,choice])

def sample_data(engine):
	conn=engine.connect()
	conn.execute(question.insert(),[
        {'question_text': 'What\'s new?',
         'pub_date': '2015-12-15 17:17:49.629'}
    ])

	conn.execute(choice.insert(),[
		{'choice_text': 'Not much', 'votes': 0, 'question_id': 1},
        {'choice_text': 'The sky', 'votes': 0, 'question_id': 1},
        {'choice_text': 'Just hacking again', 'votes': 0, 'question_id': 1},
    ])

	conn.close()



if __name__ == '__main__':
	db_url=DSN.format(**config['mysql'])
	print(db_url)
	engine=create_engine(db_url,echo=True,max_overflow=10)
	# create_talbes(engine)
	sample_data(engine)


