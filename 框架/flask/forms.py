#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : FLS
# @Software : PyCharm
# @Time     : 2023/2/3 15:50
# @Project  : pycharmlearningproject
# @File     : forms.py.py


from flask_ckeditor import CKEditorField
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError


class MyBaseForm(FlaskForm):
    class Meta:
        locales = ['zh']


class LoginForm(MyBaseForm):
    username = StringField('Username:', render_kw={'placeholder': 'Your name'}, validators=[DataRequired()])
    password = PasswordField('Password:', render_kw={'placeholder': 'Your pass'}, validators=[DataRequired(), Length(10, 128)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log in')


# 自定义验证器
# class FortyTwoForm(MyBaseForm):
#     answer= IntegerField('The number:',validators=[DataRequired()])
#     submit=SubmitField('save')
#
#     def validate_answer(form,field):
#         if field.data !=42:
#             raise ValidationError('number must be 42')
#

# 全局验证器
def is_42(form, field):
    if field.data != 42:
        raise ValidationError('Must be 42')


class FortyTwoForm(FlaskForm):
    answer = IntegerField('The Number', validators=[is_42])  # 填入可调用的对象，而不是函数调用
    submit = SubmitField()


# 文件上传: 开启文件上传功能，并对文件进行验证：类型、大小，过滤文件名等操作
from flask_wtf.file import FileField, FileRequired


class UploadFile(MyBaseForm):
    photo = FileField('upload image: ', validators=[FileRequired()])
    # file=FileField('upload file: ',validators=[FileRequired(True),FileAllowed('.txt')])
    submit = SubmitField()


class RichTextForm(FlaskForm):
    titile = StringField('Title', validators=[DataRequired(), Length(1, 50)])
    body = CKEditorField('BODY', validators=[DataRequired()])
    submit = SubmitField()


class NewNoteForm(FlaskForm):
    body = TextAreaField('Body:   ', validators=[DataRequired()])
    submit = SubmitField('Save')


class EditNoteForm(FlaskForm):
    body = TextAreaField('Body:   ', validators=[DataRequired()])
    submit = SubmitField('Update')


class DeleteNoteForm(FlaskForm):
    submit = SubmitField('Delete')
