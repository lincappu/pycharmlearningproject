'''
关于flask的完整文档：https://flask.palletsprojects.com/en/2.2.x/

这个文档是根据上面官方文档学习整理

'''

# from werkzeug import secure_filename
import os
from datetime import datetime,timedelta
import uuid
from urllib.parse import urlparse, urljoin

from flask import Flask, abort,make_response,Response
from flask import url_for, request, redirect, render_template, flash, send_from_directory
from flask_sqlalchemy import SQLAlchemy
# 表单导入
from wtforms import TextAreaField



app = Flask(__name__)
app.secret_key = 'aaabbbccc'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:Lexin2022@127.0.0.1:3306/world"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['MAX_CONTENT_LENGTH'] = 3 * 1024 * 1024
app.config['UPLOAD_PATH'] = os.path.join(app.root_path, 'uploads')
app.config['CKEDITOR_SERVE_LOCAL'] = True
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000   # 限制最大的upload大小
app.config['PERMAENT_SESSION_LEFETIME']=timedelta(days=7) # 重写session的有效期


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'xlsm'])
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app.config.update(
    MAIL_SERVER=os.getenv('MAIL_SERVER'),
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME=os.getenv('MAIL_USERNAME'),
    MAIL_PASSWORD=os.getenv('MAIL_PASSWORD'),
    MAIL_DEFAULT_SENDER=('Grey Li', os.getenv('MAIL_USERNAME')),
)

user = {
    'username': 'Grey Li',
    'bio': 'A boy who loves movies and music.',
}
movies = [
    {'name': 'My Neighbor Totoro', 'year': '1988'},
    {'name': 'Three Colours trilogy', 'year': '1993'},
    {'name': 'Forrest Gump', 'year': '1994'},
    {'name': 'Perfect Blue', 'year': '1997'},
    {'name': 'The Matrix', 'year': '1999'},
    {'name': 'Memento', 'year': '2000'},
    {'name': 'The Bucket list', 'year': '2007'},
    {'name': 'Black Swan', 'year': '2010'},
    {'name': 'Gone Girl', 'year': '2014'},
    {'name': 'CoCo', 'year': '2017'},
]

'''
1、安装
依赖的组件：
Werkzeug  WSGI实现。
Jinja   模板语言
MarkupSafe 和jinja一样，只是加重了防注入功能。
ItsDangrous签名数据，保证session安全的
Click创建命令行工具，支持客户自动以的flask命令
Blinker 提供信号
python-dotenv  提供env的环境变量
Watchdog提供文件更新重载
异步的支持： greenlet或者是eventlet
'''



''' 上下文
内置的上下文变量：
config  当前的配置对象
request  当前的请求对象，在已激活的请求环境下可用
session  当前的会话对象， 在已激活的请求环境下可用
g    与请求绑定的全局变量，在已激活的请求环境下可用


app上下文：
    应用上下文和请求上下文都是存放到一个LocalStack的栈中的，和应用app相关的操作就必须用到请求上下文，比如用url_for反转视图函数
    1、在视图函数中，不用担心上下文的问题，因为视图函数要执行，那么肯定是通过访问url方式来执行，这种情况下，flask底层就已经自动把请求上下文和应用上下文都推入到了相应的栈中
    2、如果想要在视图函数外执行相关操作，比如获取当前app(current_app)，或者是反转url，则必须手动推入上下文
    　　1.手动推入app上下文
    　　　　第一种方式
    　　　　　　app_context = app.app_context()
    　　　　　　app_context.push()
    　　　　　　print(current_app)
    　　　　第二种方式
    　　　　　　with app.app_context():
    　　　　　　print(current_app)
    　　2.手动推入请求上下文：
    　　推入请求上下文到栈中，会首先判断有没有应用上下文，如果没有则会先推入应用上下文到栈中，然后再推入请求上下文到栈中
    　　　　with app.text_request_context():
    　　　　　　print(current_app)
    3、上下文需要放在栈中的原因
    　　1.应用上下文
    　　flask底层是基于werkzeug，werkzeug是可以包含多个app的，所以这个时候用一个栈来保存，如果要使用app1，则app1需在栈的顶部，如果用完了app1，则app1应该从栈中删除，方便其他代码使用下面的app
    　　2.请求上下文
    　　如果在写测试代码或者离线脚本的时候，有时候可能需要穿件多个请求上下文，这个时候就需要存放到另一个栈中，使用哪个请求上下文的时候，就把对应的请求上下文放到栈的顶部，用完了就要把这个请求上下文从栈中移除掉
    
    自动激活上下文的场景：
    1、使用flask  run 命令启动程序
    2、使用app.run()方法启动程序
    3、使用@app.cli.command()装饰器装饰
    4、使用flask shell启动shell时
    当请求进入时，flask会自动激活请求上下文，所以request和session可以自动使用。

2、请求上下文：就是针对请求的上下文
with app.request_context(environ):
    assert request.method == 'POST'

# 针对某个请求的上下文：
with app.test_request_context('/hello',method='POST')
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'
    
    
自定义上下文：
如果多个模板都需要使用同一变量，那么比起在多个视图函数中重复传入，更好的方法是能够设置一个模板全局变量。Flask提供了一个app.context_processor装饰器，可以用来注册模板上下文处理函
以帮我们完成统一传入变量的工作。模板上下文处理函数需要返回一个包含变量键值对的字典,返回的必须是字典，哪怕是空的字典，并且在所有模板中可见
@app.context_processor
def inject_foo():
foo = 'I am foo.'
return dict(foo=foo) # 等同于return {'foo': foo}

当我们调用render_template（）函数渲染任意一个模板时，所有使用app.context_processor装饰器注册的模板上下文处理函数（包括Flask内
置的上下文处理函数）都会被执行，这些函数的返回值会被添加到模板中，因此我们可以在模板中直接使用foo变量。
    
'''




# with  app.app_context():
#     app2=current_app
#     print(app2)
#
# # 临时请求
# with app.test_request_context('/hello'):
#     request.method


'''
2.5   重定向后返回上一个页面
就是重定向的操作完成后再返回原来的页面继续执行。
两种方法：
1、request.referfer
2、设置一个查询参数来记录页面的url,这样在挑战后会记录用这个参数来记录原来url，然后再获取到后再跳转回原来的页面
'''


# 示例 第二种
# @app.route('/foo')
# def foo():
#     return "<h1>FOO page</h1><a href=%s>Do something and redirect</a>"  %url_for("do_something",next=request.full_path)
# @app.route('/do_something')
# def do_something():
#     return 'this is do_somethins'

# 完整代码

@app.route('/foo')
def foo():
    return "<h1>FOO page</h1><a href=%s>Do something and redirect</a>" % url_for("do_something", next=request.full_path)

@app.route('/bar')
def bar():
    return "<h1>bar page</h1><a href=%s>Do something and redirect</a>" % url_for("do_something", next=request.full_path)

@app.route('/do_something_and_redirect')
def do_something():
    return redirect_back()

def redirect_back(default='foo', **kwargs):
    for target in request.args.get('next'), request.referrer:
        if not target:
            continue
        if is_safe_url(target):
            return redirect(target)
    return redirect(url_for(default, **kwargs))


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc


'''
netloc 包含net工作location 其中包括域本身(和子域，如果存在)、端口号，以及使用 username:password 形式的可选凭据
'''

'''
3.1 jinjia2 模板语言：
'''



'''
4. 表单
使用flask-WTF集成的WTFforms,来操作表单，并且还有数据解析，CSRF保护，文件上传、reCAPTCHA等功能
字段属性名称大小写敏感，不能以下划线或validate开头。
'''



'''1、文件上传的功能： 
核心的点：
最基本的点
A <form> tag is marked with enctype=multipart/form-data and an <input type=file> is placed in that form.
The application accesses the file from the files dictionary on the request object.
use the save() method of the file to save the file permanently somewhere on the filesystem.

数据类型： enctype="multipart/form-data"
对象： request.files    file object
save()方法保存
默认server是不保存client上传的文件名，是随机生成的，如果要使用client的文件名，要使用secure_filename
'''

# 文件类型的校验
def allow_file_type(filename):
    return '.' in filename and filename.split('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/upload',methods=['POST','GET'])
# def upload():
#     form=UploadFile()
#     return render_template('upload.html',form=form)

# @app.route('/upload', methods=['GET', 'POST'])
# def upload():
#     form = UploadFile()
#     if form.validate_on_submit():
#         f = form.photo.data
#         filename = random_filename(f.filename)
#         file_name = secure_filename(file.filename)
#         f.save(os.path.join(app.config['UPLOAD_PATH'], filename))
#         flash('Upload success')
#         session['fliename'] = [filename]
#         return redirect(url_for('show_images'))
#     return render_template('upload.html', form=form)

# 如果不用bs 直接用html代码的话：
# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         # check if the post request has the file part
#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
#         file = request.files['file']
#         # If the user does not select a file, the browser submits an  empty file without a filename.
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)
#         if file and allow_file_type(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             return redirect(url_for('download_file', name=filename))
#     return '''
#     <!doctype html>
#     <title>Upload new File</title>
#     <h1>Upload new File</h1>
#     <form method=post enctype=multipart/form-data>
#       <input type=file name=file>
#       <input type=submit value=Upload>
#     </form>
#     '''

# 反向配置，client从server下载文件
# @app.route('/uploads/<path:filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)

# 注册download_file endpont 作为build_only这样就不需要视图函数了
'''
add_url_rule()这个方法的作用是将url和对应的视图函数名联系起来，建立映射关系，这以前都是通过route装饰器实现的,
app.route()这个就是这个装饰器，它背后就是调用了add_url_rule()的方法，
add_url_rule三个参数解释：
第一个参数：函数对应的url规则，满足条件和app.route()的第一个参数一样，必须以'/'开始
endpoint：站点，就是在使用url_for()进行反转的时候，这个里面传入的第一个参数就是这个endpoint对应的值。这个值也可以不指定，那么默认就会使用函数的名字作为endpoint的值
view_func：对应的函数，即这个url对应的是哪一个函数，注意，这里函数只需要写函数名字，不要加括号，加括号表示将函数的返回值传给了view_func参数了。程序就会直接报错。
'''
app.add_url_rule("/uploads/<filename>", endpoint='download_file', build_only=True)




'''2、类视图：
    就是以类来实现的视图，好处就是可以继承，但是类视图需要用app.add_url_rule(url_rule,url_func)来进行注册，有两种类视图

    标准类视图：
    标准类视图是继承自flask.views.View，并且在子类中必须实现dispatch_request方法，这个方法就是相当于视图函数，所有的逻辑操作我们都要放在这个里面完成。也必须的返回一个值，函数视图能返回什么类型的值，这里就可以返回什么类型的值。其实类视图和函数视图基本都是一样的，只是我们在做添加url规则的时候不一样而已。
    from flask import Flask,views
    app = Flask(__name__)
    class ProfileView(views.View):
        def dispatch_request(self):
            return '个人中心页面'
    app.add_url_rule('/profile/',endpoint='profile',view_func=ProfileView.as_view('profile'))
    add_url_rule里面的参数的意思相信大家也知道了，这里说一下as_view里面传入的参数的意思吧。
    View.as_view(’<指定函数的名称>’)：因为我们所以的类视图都会继承自View类，并且都要重写dispatch_request方法，那么flask怎么知道我们绑定的是哪一个类的dispatch_request方法呢？就是通过这个参数来指定的。相当于给我们的dispatch_request方法起一个名字。当我们没有写endpoint参数的时候，那么endpoint的值就会是我们这个函数的名字。通过url_for进行反转的时候也是用的这个值。如果指定了endpoint的值，url_for就会使用endpoint的值，我们指定的函数名称对于我们来说没有什么太大的用处了，但是flask内部还是很有用处的。
    
    基于调度方法的视图:
    在flask中，还提供了另外一种类视图flask.views.MethodView，对每个HTTP的请求方法执行不同的函数，映射到对应小写的同名方法上面。例如：
    class LoginView(views.MethodView):
        def get(self):
            return 'get 请求'
        def post(self):
            return 'post 请求'
    app.add_url_rule('/login/', view_func=LoginView.as_view('login'))
    这样，当我们以GET请求访问/login/页面的时候，就会执行get方法，以POST请求访问/login/页面的时候，就会执行post方法。
    比如我们登陆的时候，如果用户使用的是get方法请求我们的页面，那么我们就渲染一个html页面给客户端，而当使用post方法请求的时候，我们就对上传的数据进行处理，然后返回相应的信息。
'''


'''3、cookies和session的使用：
见笔记
'''


''' 4、 redirect和abort和错误错误
1、sentry的日志错误收集
2、errorhandle的处理
    依赖于werkzeug的httpException errorcode的的匹配，当匹配到就进入处理程序。


'''




'''
5 数据库
SQLAlchemy

'''
import click
# 第一种方式：就是引入上下文，
# with  app.app_context():
#     app=current_app
# with  app.app_context():
#     db = SQLAlchemy(app)
#     class Note(db.Model):
#         __tablename__ = 'note'
#         id = db.Column(db.Integer, primary_key=True)
#         body = db.Column(db.Text)
#     db.create_all()

# 第二种就是手动push这个不演示

#  在视图函数中操作数据库
db = SQLAlchemy(app)


#  创建表： 这个是
# with  app.app_context():
#     db = SQLAlchemy(app)
#     class Note(db.Model):
#         __tablename__ = 'note'
#         id = db.Column(db.Integer, primary_key=True)
#         body = db.Column(db.Text)
#     db.create_all()
# 或者是下面这种用command的方式
@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop')
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('initdb databse OK!')



#  5.5 定义关系
'''
关系就是不同表之间的字段建立联系：主要是定义外键和字段之间建立关系
'''

# flask shell 自动将对象推入上下文：
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Note=Note)


# one to many 关系从一的方向出发
class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(20))
    # article = db.relationship('Article')


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), index=True)
    body = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))


#  建立关系: 一种方式是为外键赋值，一种方式是通过关系函数将关系属性赋值给实际的对象就是append对象关系的实例

### 高级操作部分
'''
级联操作 cascade 就是定义双向关系的表当其中一个关系删除后另外一个对象的默认操作。
save-update、delete、delete-orphone、merge、all
'''


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), index=True)
    body = db.Column(db.Text)
    comments = db.relationship('Comment', cascade='save-update,merge,delete')


class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    post = db.relationship('Post', back_populates='comments')




'''
事件监听：
listen_for() 注册事件回调函数：
第一个参数是target就是监听的对象：模型类、类实例、类属性都可以，
第二个：indentifier 被监听事件的标识符，不同的操作类型对应不同的事件：

set设置某个字段值将触发set事件  设置值
append  remove  init_scalar init_collection 等
'''


class Draft(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    edit_time = db.Column(db.Integer, default=0)


# @db.event.listen_for(Draft.body, 'set')
# def increment_edit_time(target, value, oldvalue, initiator):
#     if target.edit_time is not None:
#         target.edit_time += 1


'''
6 电子邮件 
网页中涉及的电子邮件
'''
from sendgrid.helpers.mail import Email

from_mail = Email('')




from views import  * # 这个放这里的原因


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
