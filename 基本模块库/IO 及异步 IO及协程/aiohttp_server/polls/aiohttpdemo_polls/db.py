# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

from sqlalchemy import (
	MetaData, Table, Column, ForeignKey,
	Integer, String, Date, DateTime
)

metadata = MetaData()
question = Table('question', metadata,
				 Column('id', Integer, primary_key=True),
				 Column('question_text', String(200), nullable=False),
				 Column('pub_date', DateTime, nullable=False)
				 )

choice = Table('choice', metadata,
			   Column('id', Integer, primary_key=True),
			   Column('choice_text', String(200), nullable=False),
			   Column('votes', Integer, server_default="0", nullable=False),
			   Column('question_id',
					  Integer,
					  ForeignKey('question.id', ondelete='CASCADE'))
			   )
