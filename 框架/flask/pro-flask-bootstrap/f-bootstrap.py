#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : FLS
# @Software : PyCharm
# @Time     : 2023/2/23 18:13
# @Project  : pycharmlearningproject
# @File     : f-bootstrap.py

'''
flask-bootstrap:
提供了基础模块，首先引入相关的基末模板，模板里面定义了页面元素，然后通过集成来修改元素信息，核心应用就3点：
1、base.html的基础模板，定义页面的整体结构，
    可继承的block有doc  html script body navbar content等页面元素
2、wtf.html 对于表单的支持
4、flask-nav 对导航的支持  https://pythonhosted.org/flask-nav/
    Text: 对应 html 标签 span
    Seperator: 对应 html 标签 hr
    View: 对应到 html 超链接，需要 Flask 提供视图函数
    Link: 对应到普通的 html 超链接
    Subgroup: 用于对 Navigation item 进行分组
    Navbar: 通常作为顶层 item

    实际上渲染出来后就是ul和li的组合

5、dev_db="mysql://root:Lexin2022@127.0.0.1:3306/world"
SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG_TB_INTERCEPT_REDIRECTS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db) 对sql的支持

'''

import logging
# 表单导入
import os

from flask import Flask, redirect
from flask import render_template
# bs导入
from flask_bootstrap import Bootstrap
# flask-nav导航
from flask_nav import Nav, register_renderer
from flask_nav.elements import *
# flask_sqlalchemy的导入
from flask_sqlalchemy import SQLAlchemy as sa, get_debug_queries
from flask_sqlalchemy.track_modifications import models_committed
# flask_wtf的导入
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField
from wtforms.validators import DataRequired

'''
flask_nav的使用
'''
# 使用普通的导航
# top是名字，viewer是导航元素，第一个是名字，第二个是url_for
nav = Nav()
nav.register_element(
    'top',
    Navbar(
        View('WidgitsInc', 'index'),
        View('Our Mission', 'about'),
        Subgroup('Products',  # 导航列表，就是里面有多个页面，product='wg240' 这个是在接受参数
                 View('Wg240-Series',
                      'products',
                      product='wg240'),
                 View('Wg250-Series',
                      'products',
                      product='wg250'),
                 # Separator(),  # 之间的分割线
                 # Text('Discontinued Products'),  # 类似label的text标签。解释下面的导航项
                 View('Wg10X',
                      'products',
                      product='wg10x'), ),
        Link('Tech Support', 'http://baidu.com'),  # 导航项是个跳转连接
    )
)

# 渲染器 renderer，就是将标签渲染成htlm的代码
'''
渲染器的代码：他实际上就是访问者模式的代码，去遍历里面涉及的标签，然后转为html相应的代码。比如说navbar他就会转换为ul和li的标签。

from flask import current_app

from dominate import tags
from visitor import Visitor

class Renderer(Visitor):
    """Base interface for navigation renderers.
    Visiting a node should return a string or an object that converts to a
    string containing HTML."""

    def visit_object(self, node):
        """Fallback rendering for objects.
        If the current application is in debug-mode
        (``flask.current_app.debug`` is ``True``), an ``<!-- HTML comment
        -->`` will be rendered, indicating which class is missing a visitation
        function.
        Outside of debug-mode, returns an empty string.
        """
        if current_app.debug:
            return tags.comment('no implementation in {} to render {}'.format(
                self.__class__.__name__,
                node.__class__.__name__, ))
        return ''

class SimpleRenderer(Renderer):
    """A very basic HTML5 renderer.
    Renders a navigational structure using ``<nav>`` and ``<ul>`` tags that
    can be styled using modern CSS.
    :param kwargs: Additional attributes to pass on to the root ``<nav>``-tag.
    """

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def visit_Link(self, node):
        return tags.a(node.text, href=node.get_url())

    def visit_Navbar(self, node):
        kwargs = {'_class': 'navbar'}
        kwargs.update(self.kwargs)

        cont = tags.nav(**kwargs)
        ul = cont.add(tags.ul())

        for item in node.items:
            ul.add(tags.li(self.visit(item)))

        return cont

    def visit_View(self, node):
        kwargs = {}
        if node.active:
            kwargs['_class'] = 'active'
        return tags.a(node.text,
                      href=node.get_url(),
                      title=node.text,
                      **kwargs)

    def visit_Subgroup(self, node):
        group = tags.ul(_class='subgroup')
        title = tags.span(node.title)

        if node.active:
            title.attributes['class'] = 'active'

        for item in node.items:
            group.add(tags.li(self.visit(item)))

        return tags.div(title, group)

    def visit_Separator(self, node):
        return tags.hr(_class='separator')

    def visit_Text(self, node):
        return tags.span(node.text, _class='nav-label')
'''
# 高级功能：自定义渲染器，就是自己控制flask_nav的方法在html的显示方式。
from dominate import tags
from flask_nav.renderers import Renderer


# 自定义渲染器。
class JustDivRenderer(Renderer):
    def visit_Navbar(self, node):
        sub = []
        for item in node.items:
            sub.append(self.visit(item))
        return tags.div('Navigation:', *sub)

    def visit_View(self, node):
        return tags.div('{} ({})'.format(node.text, node.get_url()))

    def visit_Subgroup(self, node):
        # almost the same as visit_Navbar, but written a bit more concise
        return tags.div(node.title, *[self.visit(item) for item in node.items])

    def vist_Link(self, node):  # Link的标签识别不出来，不知道为什么。
        return tags.div(node.title, *[self.visit(item) for item in node.items])
        # return tags.div(node)


# 上面是自定义的渲染器，下面是自定义元素，就是实现一个自动以的 NavigationItem， 重新定义或者重载一个元素类型的方法。
# 下面是一个打招呼的元素，这个是结构是固定的， 只是内部会根据登录人元而变化。
class UserGreeting(Text):
    def __init__(self):
        pass

    @property
    def text(self):
        return 'Hello, {}'.format('bob')


# 动态导航栏，就是用户登录和没登录样式是不一样的，结构发生变化。只需要将一个可调用的对象传递给register_element()  不实现。
# 以上是flask_nav的内容。


'''
2、WTForms的支持。就是表单。以来的是flask-wtf项目： https://flask-wtf.readthedocs.io/en/latest/quickstart/
bootstrap/wtf.html 模板包含了帮助你快速输出表单的宏。 Flask-WTF不是Flask-Bootstrap的依赖，但是必须被正确的安装。 
在最近的几个版本中， Flask-WTF 的API变化很大，Flask-Bootstrap目前为 Flask-WTF 的0.9.2版本开发。
'''


class NoteForm(FlaskForm):
    body = TextAreaField('body: ', render_kw={'class': 'text-body', 'rows': 10, 'placeholder': '请输入你的日志....'},
                         validators=[DataRequired()])  # 文本域，自动换行的写法。
    submit = SubmitField('OK')


logging.basicConfig(level=logging.DEBUG, filemode='a+', filename='query_log.log', format='%(asctime)s -: %(message)s)')
app = Flask(__name__)
bootstrap = Bootstrap(app)
nav.init_app(app)
register_renderer(app, 'just_div', JustDivRenderer)  # 注册renderer

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:Lexin2022@127.0.0.1:3306/world"
app.config['SQLALCHEMY_BINDS'] = {
    'db1': "mysql://root:Lexin2022@127.0.0.1:3306/world",
    'db2': {
        "url": "mysql://root:Lexin2022@127.0.0.1:3306/mysql",
        "pool_recycle": 3600,
    }

}

app.config['SQLALCHEMY_RECORD_QUERIES'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config["SQLALCHEMY_ECHO"] = True

db = sa()
db.init_app(app)


@app.route('/bootstrap/<name>')
def flask(name):
    return render_template('test_bootstrap.html', name=name)


UPLOAD_DIR = 'upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_DIR
app.secret_key = 'aaabbbccc'
basedir = os.path.abspath(os.path.dirname(__file__))
ALLOWED_EXTENSIONS = set(['txt', 'png'])


# 下面是base和flask_nav的例子

@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/products/<product>')
def products(product):
    return render_template('index.html', msg='Buy our {}'.format(product))


@app.route('/wtf-form', methods=['GET', 'POST'])
def flask_wtf_form():
    form = NoteForm()
    if form.validate_on_submit():
        return render_template('index.html')
    return render_template('wft-form.html', form=form)


'''
3、sqlarchemy的支持，
flask-sqlalchemy：  https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/#check-the-sqlalchemy-documentation
这个和sqlalchemy差不多，所以用法是差不多的
主要的点：
1、定义表结构
2、创建表，create_all()    
        1、注意app上下文
        2、注意如果是create_all变更了， 解决方法有两种：一个drop_all()重新建 ，一个是利用 Flask-Alembic or Flask-Migrate 更新表结构
3、操作数据： db.session 
    增加：
        user = User()
        db.session.add(user)
        或者是db.session.add_all(user) 来一次性全部添加
    更改：
        user.verified = True
        db.session.commit()
    删除：
        db.session.delete(user)
        db.session.commit()
    查询：是利用select()函数，
    
        基本方法：   <模型类>.query.<过滤方法>.<查询方法>
                                            first()
                                            all()
                                            one()
                                            get(id)  
                                            count()
                                            one_or_none()  要么是1要么是none
                                            first_or_404()
                                            get_or_404(id)
                                            paginate() 传入一个分页对象
                                            with_parent(instance)  传入模型实例，返回和这个实例关联的对象
                                filter()   
                                filter_by()
                                order_by()
                                group_by()
                                limit()
                                
    
        user = db.session.execute(db.select(User).filter_by(username=username)).scalar_one()
        users = db.session.execute(db.select(User).order_by(User.username)).scalars()
        这个返回的是一个Result的对象，需要scalars   scalar_one 来读取
        
        功能函数：
            SQLAlchemy.get_or_404() will raise a 404 if the row with the given id doesn’t exist, otherwise it will return the instance.
            SQLAlchemy.first_or_404() will raise a 404 if the query does not return any results, otherwise it will return the first result.
            SQLAlchemy.one_or_404() will raise a 404 if the query does not return exactly one result, otherwise it will return the result
    
        遗弃的查询方法：
            Model.query  or session.query  这种方式已经放在sqlalchemy遗弃了，但是应该还能用。
            User.query==db.session.query(User) 
            user.query.get(5) 查询id是5的
            user.query.filter_by(username=username).one() 
            user.query.all().order_by(id)
              
            功能函数依旧是能用的 
              
            分页：    
            page = User.query.order_by(User.join_date).paginate()
            return render_template("user/list.html", page=page)
              

4、配置：  
    1、配置项是在init_app的时候生效的，并且只读取这一次，所以不能放在这之后
    SQLALCHEMY_DATABASE_URI	用于连接数据的数据库。例如： sqlite:////tmp/test.db   mysql://username:password@server/db
    SQLALCHEMY_BINDS	一个映射绑定 (bind) 键到 SQLAlchemy 连接 URIs 的字典。 更多的信息请参阅 绑定多个数据库。
    SQLALCHEMY_ECHO	如果设置成 True，SQLAlchemy 将会记录所有 发到标准输出(stderr)的语句，这对调试很有帮助。
    SQLALCHEMY_RECORD_QUERIES	可以用于显式地禁用或者启用查询记录。查询记录 在调试或者测试模式下自动启用。更多信息请参阅 get_debug_queries()。
    SQLALCHEMY_NATIVE_UNICODE	可以用于显式地禁用支持原生的 unicode。这是 某些数据库适配器必须的（像在 Ubuntu 某些版本上的 PostgreSQL），当使用不合适的指定无编码的数据库 默认值时。
    SQLALCHEMY_POOL_SIZE	数据库连接池的大小。默认是数据库引擎的默认值 （通常是 5）。
    SQLALCHEMY_POOL_TIMEOUT	指定数据库连接池的超时时间。默认是 10。
    SQLALCHEMY_POOL_RECYCLE	自动回收连接的秒数。这对 MySQL 是必须的，默认 情况下 MySQL 会自动移除闲置 8 小时或者以上的连接。 需要注意地是如果使用 MySQL 的话， Flask-SQLAlchemy 会自动地设置这个值为 2 小时。
    SQLALCHEMY_MAX_OVERFLOW	控制在连接池达到最大值后可以创建的连接数。当这些额外的 连接回收到连接池后将会被断开和抛弃。
    SQLALCHEMY_TRACK_MODIFICATIONS	如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。 


5、关系
    1对多
        1、定义外键   外键是标量，定义在多的一侧
        2、定义关系   关系是集合，定义在1的一侧，也可以是双向关系
    多对1 
        和1对多是一样 也是在多的一侧
    多对多


'''

#  sqlalchemy and sqlalchemy.orm   同时支持

#  这种事反射表的方式
class User(db.Model):
    __tablename__ = 'user'
    # __bind_key__='db1'# 要么在里指定bind_key，
    # __bind_key__ = db.bind_key_pattern('db_\d')  # 模式匹配
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100))

    # def __repr__(self):
    #     return '<user %r>' % self.body


# 和sqlalchemy一样，另外一种定义表的方式：  这种是定义表方式
# user=db.Table(
#     'user',
#     sa.Column('username',primary_key=True),
# )

# with  app.app_context():
#     db.create_all()
# 如果是有多个数据库绑定的情况需要指定绑定的数据库
# db.create_all(bind='db1')  # 要么在这里执行bind_key   默认是bind None


# 查询sql的写法
# with app.app_context():
#     res = db.session.execute(db.select(User).filter_by(id=1000)).scalars()  # 和scalar_one() 只能返回一个结果。scalars() 一个或者多个
#     res.get_recorded_queries()
#     print(res.id, res.username, res.email)


class NewUserForm(FlaskForm):
    username = StringField('Username:   ', validators=[DataRequired()])
    submit = SubmitField('Save')


class EditUseroteForm(FlaskForm):
    username = StringField('Username:   ', validators=[DataRequired()])
    submit = SubmitField('Update')


class DeleteUseroteForm(FlaskForm):
    submit = SubmitField('Delete')


@app.route('/new_user', methods=['POST'])
def new_user():
    form = NewUserForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        user = User(username=username, email=email)
        db.session.add(user)
        db.commit()
        return redirect(url_for('show_user'))
    return render_template('new_user.html', form=form)


@app.route('/show_user')
def show_user():
    users = db.session.execute(db.select(User)).scalars()
    # users = User.query.all()
    for user in users:
        print(user.email)
    return render_template('show_user.html', users=users)


# 这个是一个文件上传的例子：
@app.route('/')
def upload_test():
    return render_template('upload.html')


@app.route('/api/upload', methods=['POST', 'get'])
def upload():
    file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    # f=request.files['myfile']
    f = request.files.get('myfile')
    fname = f.filename
    f.save(os.path.join(file_dir, fname))
    return render_template('upload.html')





'''
扩展功能：
1、get_debug_queries 记录sql的执行情况  sql记录和执行时长  主要是 after_request视图
@app.after_request
def after_request(response):
    for query in get_debug_queries():
        logging.info('statement:  ' + query.statement)
        logging.info('parameters:  ' + str(query.parameters))
        logging.info('start_time :  ' + str(query.start_time))
        logging.info('end_time:  ' + str(query.end_time))
        logging.info('duration:  ' + str(query.duration))
        logging.info('location:  ' + str(query.location))
    return response
相同的还有 @app.before_request   @app.teardown_request等

2、SQLALCHEMY_TRACK_MODIFICATIONS 准备对表的修改信息。

3、自定义基类： Modle  Session  都是集成的积，可以自定义。

4、 engine 数据库引擎。数据库引擎实例，负责数据库的接口，但是如果是ORM就不能使用engine，因为需要映射才能转化为sql语句才能执行，
    所以是不能执行对接数据库引擎接口的。flask-sqlalchemy就是这种。

5、分页

'''



#  以上就是整个flask用的整个内容


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)



