# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

# from sys,os


class Schools(object):
    def __init__(self, school_name, school_address):
        self.school_name = school_name
        self.school_address = school_address

    def create_teacher(self, school_name, teacher_name, age, sex, number, salary):
        teacher_date = [school_name, teacher_name, age, sex, number, salary]
        return teacher_date

    def create_lesson(self, school_name, lesson_name, price, period):
        lesson_data = [school_name, lesson_name, price, period]
        return  lesson_data