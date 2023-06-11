#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : FLS
# @Software : PyCharm
# @Time     : 2023/4/26 14:39
# @Project  : pycharmlearningproject
# @File     : f-moment.py


'''moment.js 一个使用 JavaScript 开发的优秀客户端开源代码库，可在浏览器中渲染日期和时间。
flask-moment 是一个 flask 程序扩展，能把 moment.js 集成到 Jinja2 模板中。


1、引用：moment.js 还需要jquery.js
{{ moment.include_moment() }} 远程方式，
{{ moment.include_moment(local_js=url_for('static', filename='js/moment-with-locales.min.js')) }}  本地文件的方式
除了 moment.js，flask-moment 还依赖 jquery.js 。要在 html 文档的某个地方引入这两个库，可以直接引入，这样可以选择使用哪个版本，
也可使用扩展提供的辅助函数，从内容分发网络（CDN，Content Delivery Network）中引入通过测试的版本。Bootstrap 已经引入了 jquery.js，因此只需引入 moment.js 即可


2、使用

https://momentjs.com/docs   丰富的使用样例

'''



from flask import Flask,render_template
from flask_moment import  Moment
from datetime import datetime

app = Flask(__name__)
moment=Moment(app)


@app.route('/')
def index():
    return render_template('moment.html',current_time=datetime.utcnow())
    

if __name__ == '__main__':
    app.run()