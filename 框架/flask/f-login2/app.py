#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : FLS
# @Software : PyCharm
# @Time     : 2023/5/11 19:51
# @Project  : pycharmlearningproject
# @File     : app.py



from flask import Flask, render_template, redirect, url_for, request, flash,make_response,session
from flask_login import LoginManager, login_required, login_user, logout_user, UserMixin, current_user,login_fresh
from flask_sqlalchemy import SQLAlchemy as sa
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:Lexin2022@127.0.0.1:3306/world"
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(seconds=30)

db = sa()
db.init_app(app)


class Register(db.Model):
    __tablename__ = 'register'
    # __bind_key__='db1'# 要么在里指定bind_key，
    # __bind_key__ = db.bind_key_pattern('db_\d')  # 模式匹配
    ids = db.Column(db.String(50), primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100))



class LoginForm(FlaskForm):
    # 域初始化时，第一个参数是设置label属性的
    username = StringField('User Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('remember me', default=False)


class RegisterForm(FlaskForm):
    ids = StringField('id:', validators=[DataRequired()])
    username = StringField('username:', validators=[DataRequired()])
    password = PasswordField('password:', validators=[DataRequired()])
    password2 = PasswordField('Repeat password:', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_ids(self, ids):
        user = Register.query.filter_by(ids=ids.data).first()
        print(user)
        if user is not None:
            raise ValidationError('Please use a different id.')

    def validate_username(self, username):
        user = Register.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username address.')


# with app.app_context():
#     db.create_all()


class User(UserMixin):
    pass


users = [
    {'id': 'Tom', 'username': 'Tom', 'password': '111111'},
    {'id': 'Michael', 'username': 'Michael', 'password': '123456'}
]

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message = "login first"
login_manager.session_protection = None

login_manager.refresh_view = "isfresh"
login_manager.needs_refresh_message = (
    u"To protect your account, please reauthenticate to access this page."
)
login_manager.needs_refresh_message_category = "info"

login_manager.init_app(app)

csrf = CSRFProtect()
csrf.init_app(app)


def query_user(user_id):
    for user in users:
        if user_id == user['id']:
            return user


@login_manager.user_loader
def load_user(user_id): # 这个user_id 就是表示用户在不在的，在session里面是_user_id的形式，这个决定了用哪个参数
    if query_user(user_id) is not None:
        curr_user = User()
        curr_user.id = user_id
        return curr_user

@app.route('/stats')
def stats():
    a=current_user.is_authenticated
    b=current_user.is_active
    c=login_fresh()
    res=make_response("jieguo: %s   %s  %s " %(str(a),str(b),str(c)))
    return res

@login_manager.needs_refresh_handler
@app.route('/isfresh')
def isfresh():
    fre=login_fresh()
    if fre:
        res=make_response('this page is fresh')
    else:
        res = make_response('this page is  NOT  fresh')
    return res


@app.route('/')
@app.route('/index')
@login_required
def index():
    if '_user_id' in session:
        print("okkk")
    print(session)
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('/index'))
    form = LoginForm()
    if request.method == 'POST':
        user_id = request.form.get('username')
        password = request.form.get("password")
        remember_me=request.form.get("remember_me")
        user = query_user(user_id)
        print(user)
        if user is not None and password == user['password']:
            curr_user = User()
            curr_user.id = user_id
            # 通过Flask-Login的login_user方法登录用户
            login_user(curr_user,remember=remember_me,duration=datetime.timedelta(seconds=600))
            return redirect(request.args.get('next') or url_for('index'))
        flash('Wrong username or password!')
    # GET 请求
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    form = LoginForm()
    logout_user()
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = Register(ids=form.ids.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)



# cookie和session的使用
@app.route('/accesstime')
def first_access():
    accesstime=request.cookies.get('accesstime')
    if accesstime is None:
        time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        res=make_response('this is your first time acces')
        res.set_cookie('accesstime',time,max_age=60)
        return res
    else:
        return f"这不是你第一次访问这个网页，你第一次访问的时间是  {accesstime}"




'''
针对session已经过期，但是使用了remerber_me时自动进行的登录，但是在操作敏感操作的时候要确认是登录状态。

第一种方式：
login_manager.refresh_view = "accounts.reauthenticate"
login_manager.needs_refresh_message = (
    u"To protect your account, please reauthenticate to access this page."
)
login_manager.needs_refresh_message_category = "info"


第二种方式：
@login_manager.needs_refresh_handler
def refresh():
    # do stuff
    return a_response
'''




if __name__ == '__main__':
    app.run()
