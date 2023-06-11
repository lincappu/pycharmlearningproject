#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : FLS
# @Software : PyCharm
# @Time     : 2023/3/20 16:24
# @Project  : pycharmlearningproject
# @File     : views.py


import os
import uuid
from urllib.parse import urlparse, urljoin

from flask import Flask, abort,make_response,Response,session
from flask import url_for, request, redirect, render_template, flash, send_from_directory
from flask_sqlalchemy import SQLAlchemy
# 表单导入
from wtforms import TextAreaField
import werkzeug

from app import app,db
from modles import *
from forms  import *


@app.route('/new', methods=['POST', 'GET'])
def new_note():
    form = NewNoteForm()
    if form.validate_on_submit():
        body = form.body.data
        note = Note(body=body)  # 这个
        db.session.add(note)
        db.session.commit()
        flash('Your note is saved')
        return redirect(url_for('index'))
    return render_template('new_note.html', form=form)


@app.route('/edit/<int:note_id>', methods=['POST', 'GET'])
def edit_note(note_id):
    form = EditNoteForm()
    note = Note.query.get(note_id)
    if form.validate_on_submit():
        note.body = form.body.data
        db.session.commit()
        flash('Your note is updated.')
        return redirect(url_for('index'))
    form.body.data = note.body
    return render_template('edit_note.html', form=form)


@app.route('/delete/<int:note_id>', methods=['POST'])
def delete_note(note_id):
    form = DeleteNoteForm()
    if form.validate_on_submit():
        note = Note.query.get(note_id)
        db.session.delete(note)
        db.session.commit()
    else:
        abort(400)
    return redirect(url_for('index'))


@app.route('/')
def index():
    form = DeleteNoteForm()
    notes = Note.query.all()
    return render_template('index.html', notes=notes, form=form)



@app.route('/watchlist')
def watchlist():
    return render_template('watchlist.html', user=user, movies=movies)



@app.route('/flash')
def just_flash():
    flash('你好，我是闪电。')
    return redirect(url_for('foo'))

# errorhandle
@app.errorhandler(404)  # 注册handler  这个是标准的做法，补货对应的code就处理
def page_not_found(e):
    return render_template('errors/404.html'), 404


@app.route('/basic')
def basic():
    form = LoginForm()
    return render_template('login.html', form=form)


def random_filename(filename):
    ext = os.path.splitext(filename)[1]
    print(ext)
    new_filename = uuid.uuid4().hex + ext
    return new_filename


# cookies
@app.route('/cookies')
def test_cookies():
    res=make_response('set-cookies')
    res.set_cookie('username','fls',max_age=3600)
    username=request.cookies.get('username')
    res.delete_cookie('username')
    print(username)
    return res

@app.route('/session')
def test_session():
    session['username']='sss'
    session.permanent=True # 默认是一个月
    name=session.get('username')
    session.pop('username',None)
    session['username']=False
    print(name)
    return 'ok'
