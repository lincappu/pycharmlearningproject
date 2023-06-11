from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkclassroom.v3.region.classroom_region import ClassroomRegion
from huaweicloudsdkclassroom.v3 import *
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : FLS
# @Software : PyCharm
# @Time     : 2023/2/23 15:06
# @Project  : pycharmlearningproject
# @File     : views.py


from flask import flash,redirect,render_template,url_for

# 从构造文件导入变量不需要注明构造文件的路径，只需要从包名称导入即可，
from bbs import db,app
from bbs.forms import  MessageForm
from bbs.models  import Message


@app.route('/',methods=['POST','GET'])
def index():
    form=MessageForm()
    if form.validate_on_submit():
        name=form.name.data
        body=form.body.data
        message=Message(body=body,name=name)
        db.session.add(message)
        db.session.commit()
        flash('Your message have been sent to the world!')
        return redirect(url_for('index'))
    messages=Message.query.order_by(Message.timestamp.desc()).all()
    return render_template('index.html',form=form,messages=messages)
