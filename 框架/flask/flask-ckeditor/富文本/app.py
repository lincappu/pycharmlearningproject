#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : FLS
# @Software : PyCharm
# @Time     : 2023/6/27 18:30
# @Project  : pycharmlearningproject
# @File     : flask-ckeditor.py

'''
富文本编辑器即WYSIWYG（What You See Is What You Get）编辑器（所见即所得编辑器）。
在Web程序中可用的开源富文本编辑器中，CKEditor是一个流行的选择。Flask-CKEditor简化了将CKEditor集成到Flask项目中的过程，可以让你方便的在Flask项目中添加富文本编辑器。它包含下面这些特性：
提供的功能：
1、提供WTForms/Flask-WTF集成支持
2、支持图片上传与插入
3、通过Flask配置来设置编辑器的语言、高度等参数
4、支持代码块语法高亮



html文件中引入资源的方式:
1、为了使用CKEditor，我们首先要在模板中引入CKEditor的JavaScript等资源文件。
推荐的做法是自己编写资源引用语句，你可以在CKEditor提供的Online Builder构建一个自定义的资源包，下载解压后放到项目的static目录下， 并引入资源包内的ckeditor.js文件，比如（实际路径按需调整）：
<script src="{{ url_for('static', filename='ckeditor/ckeditor.js') }}"></script>

2、如果你不需要自定义，那么也可以从CDN加载：
<script src="//cdn.ckeditor.com/4.9.2/standard/ckeditor.js"></script>

3、最后，作为替代选项，你也可以使用Flask-CKEditor提供的ckeditor.load()方法来生成引用语句：
{{ ckeditor.load() }}
它默认从CDN加载资源，将配置变量CKEDITOR_SERVE_LOCAL设为True会使用扩展内置的本地资源。
另外，你也可以使用custom_url参数来使用自定义资源包：
{{ ckeditor.load(custom_url=url_for('static', filename='ckeditor/ckeditor.js')) }}


'''


# 安装 pip instlal flask-ckeditor
# 使用
from flask import Flask,redirect,url_for,render_template
from flask_ckeditor import CKEditorField,CKEditor
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_wtf import CSRFProtect
from flask_moment import Moment


app=Flask(__name__)

app.config['SECRET_KEY'] ='FSFSDFDSFSDF'
app.config['CKEDITOR_HEIGHT']=600
app.config['CKEDITOR_WIDTH']=1800

csrf=CSRFProtect(app)
moment=Moment(app)
ckeditor=CKEditor(app)
#工厂函数
# ckeditor.init_app(app)


# 富文本功能
class PostForm(FlaskForm):
    title = StringField('Title')
    body = CKEditorField('Body')
    submit = SubmitField('提交')

@app.route('/',methods=['POST','GET'])
def add_post():
    form=PostForm()
    if form.validate_on_submit():
        titie=form.title.data
        body=form.body.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form)



# 图片上传功能







if __name__ == '__main__':
    app.run()











