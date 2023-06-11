#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : FLS
# @Software : PyCharm
# @Time     : 2023/5/28 20:57
# @Project  : pycharmlearningproject
# @File     : auth.py

from flask import render_template, flash, redirect, url_for, Blueprint
from flask_login import login_user, logout_user, login_required, current_user


from bluelog.forms import LoginForm
from bluelog.models import Admin
from bluelog.utils import redirect_back

auth_bp=Blueprint("auth",__name__)

@auth_bp.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated():
        return redirect(url_for('blog.index'))

    form=LoginForm()
    if form.validate_on_submit():

