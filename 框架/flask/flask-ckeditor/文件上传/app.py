#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : FLS
# @Software : PyCharm
# @Time     : 2023/6/28 11:27
# @Project  : pycharmlearningproject
# @File     : app.py

from flask import Flask, render_template, request, url_for, send_from_directory
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_moment import Moment

from flask_ckeditor import CKEditor, CKEditorField, upload_fail, upload_success
from flask_wtf import CSRFProtect

import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.secret_key ='sfdsfdsf'
app.config['CKEDITOR_SERVE_LOCAL'] = True
app.config['CKEDITOR_HEIGHT'] = 600
app.config['CKEDITOR_FILE_UPLOADER'] = 'upload'  # 上传函数的端点
app.config['CKEDITOR_ENABLE_CSRF'] = True  # 如果不开启就不要初始化csrf的实例
app.config['UPLOADED_PATH'] = os.path.join(basedir, 'uploads')

csrf = CSRFProtect(app)
ckeditor = CKEditor(app)


class PostForm(FlaskForm):
    title = StringField('Title')
    body = CKEditorField('Body', validators=[DataRequired()])
    submit = SubmitField()


@app.route('/', methods=['GET', 'POST'])
def index():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        # WARNING: use bleach or something similar to clean the data (escape JavaScript code)
        # You may need to store the data in database here
        return render_template('post.html', title=title, body=body)
    return render_template('index.html', form=form)


@app.route('/files/<filename>')
def uploaded_files(filename):
    path = app.config['UPLOADED_PATH']
    return send_from_directory(path, filename)


@app.route('/upload', methods=['POST'])
def upload():
    f = request.files.get('upload')
    extension = f.filename.split('.')[-1].lower()
    if extension not in ['jpg', 'gif', 'png', 'jpeg']:
        return upload_fail(message='Image only!')
    f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
    url = url_for('uploaded_files', filename=f.filename)
    return upload_success(url, filename=f.filename)



if __name__ == '__main__':
    app.run(debug=True)
