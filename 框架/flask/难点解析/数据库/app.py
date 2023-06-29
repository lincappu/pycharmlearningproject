'''
关于flask的完整文档：https://flask.palletsprojects.com/en/2.2.x/

这个文档是根据上面官方文档学习整理


主要理解表的关系:
一对一
一对多
多对一
多对多

重点：
外键是标量只有一个值，定义在多的一侧
关系是集合，定义一的一侧

back_populates 显示定义关系  backref隐试的定义关系


'''

# 1、一对多 是基础
# class Author(db.Model):
#     __tablename__='author'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(70), unique=True)
#     phone = db.Column(db.String(20))
#
#     #关系属性定义在关系出发的一侧，一对多，就是一这一侧。关系就是对端的表，和哪张表建立关系。
#     articles=db.relationship('Article')  # 不是column，而是relationship 代表集合关系，他会去找对端表的外键字段。
#
# class Article(db.Model):
#     __tablename__ = 'article'
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(50), index=True)
#     body = db.Column(db.Text)
#
#     # 外键就是在A表中定义个字段和B表的中主键做关联，这样两个表就通过这个这两个字段做了关联。
#     author_id=db.Column(db.Integer,db.ForeignKey('author.id'))

# 一对多的双向关系：是在单向关系的基础上，建立反向的关系，将两个关系进行关联。
# 操作双向关系也是和一对多一样的，也是在多的一侧进行操作，另一侧就自动关联了。
# class Author(db.Model):
#     __tablename__='author'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(70), unique=True)
#     phone = db.Column(db.String(20))
#
#     # 定义第一个关系：
#     articles=db.relationship('Article',back_populates='author')  # back_populates就是另一个反向关系。两个是相对的
#
# class Article(db.Model):
#     __tablename__ = 'article'
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(50), index=True)
#     body = db.Column(db.Text)
#
#     # 外键还是必须的，
#     author_id=db.Column(db.Integer,db.ForeignKey('author.id'))
#     # 定义第二个关系
#     author=db.relationship('author',back_populates='articles')


# 2、多对一的关系，就是一对多关系反着来。
# 外键永远定义在多一侧，关系定义在出发的一侧，多对一就是定义在多的一侧。
# class Citizen(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(70), unique=True)
#     city_id = db.Column(db.Integer, db.ForeignKey('city.id'))
#     city = db.relationship('City')
#
#
# class City(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(30), unique=True)


# 3、一对一的关系
# 和一对多定义是一样的，区别在于一这一侧的集合关系要变成标量关系。uselist=False来设置。这个是基于双向关系的一对多来实现了一对一，但又没有定义反向关系
# class Country(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(30), unique=True)
#     capital = db.relationship('Capital', uselist=False)
#
#
# class Capital(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(30), unique=True)
#     country_id = db.Column(db.Integer, db.ForeignKey('country.id'))
#     country = db.relationship('Country')


# 4、多对多
# 按照一对多和多对一，多对多就需要两个外键和两个关系。，而外键是通过关联表的形式来关联的
# association_table = db.Table('st_te_tb',
#                              db.Column('id',db.Integer,primary_key=True),
#                              db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
#                              db.Column('teacher_id', db.Integer, db.ForeignKey('teacher.id'))
#                              )
# class Student(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(70), unique=True)
#     grade = db.Column(db.String(20))
#     teachers = db.relationship('Teacher', secondary=association_table, back_populates='students')
# class Teacher(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(70), unique=True)
#     office = db.Column(db.String(20))
#     age=db.Column(db.Integer    )
#     students = db.relationship('Student',secondary=association_table,back_populates='teachers')  # 如果没有他，就是单向的关系


# 5、级联操作
# 通过一对多关系来演示：级联操作定义在关系上面，caseade 参数来设置
# all，delete-orphan 一般是这两个。
# 有隐患，慎用
# class Author(db.Model):
#     __tablename__='author'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(70), unique=True)
#     phone = db.Column(db.String(20))
#
#     # 定义第一个关系：
#     articles=db.relationship('Article',back_populates='author',cascade='all delete-arphan')  # back_populates就是另一个反向关系。两个是相对的
#
# class Article(db.Model):
#     __tablename__ = 'article'
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(50), index=True)
#     body = db.Column(db.Text)
#
#     # 外键还是必须的，
#     author_id=db.Column(db.Integer,db.ForeignKey('author.id'))
#     # 定义第二个关系
#     author=db.relationship('author',back_populates='articles')


# 6、事件监听
# 针对db的操作设置监听机制，不同的事件类型：set append  remove  init_scalar  init_collect
# 修改一次body  edit_time+1
# class Draft(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     body = db.Column(db.Text)
#     edit_time = db.Column(db.Integer, default=0)
#
# @db.event.listen_for(Draft.body,'set')
# def incr_edit_time(target,value,oldvalue,initiator):
#     if target.edit_time is not None:
#         target.edit_time+=1


# 7、邻接列表关系： 就是在一个表内进行的一对多的关系，
# 下面是一个评论的模型，因为评论还有回复，所以就出现了在单表内连接的情况，
# 原理按照一对多的模型：需要一个外键和双向关系，这里面核心就是分清，哪个是一，哪个是多，

# from werkzeug import secure_filename


import os
from datetime import timedelta

from flask_ckeditor import CKEditorField, CKEditor
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask import Flask, redirect, url_for, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, URL, Optional

# 表单导入

app = Flask(__name__)

basedir = os.path.abspath((os.path.dirname(__file__)))

app.secret_key = 'aaabbbccc'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data-dev.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['MAX_CONTENT_LENGTH'] = 3 * 1024 * 1024
app.config['UPLOAD_PATH'] = os.path.join(app.root_path, 'uploads')
app.config['CKEDITOR_SERVE_LOCAL'] = True
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000  # 限制最大的upload大小
app.config['PERMAENT_SESSION_LEFETIME'] = timedelta(days=7)  # 重写session的有效期
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

bootstrap = Bootstrap()
bootstrap.init_app(app)
moment = Moment()
moment.init_app(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
csrf = CSRFProtect()
csrf.init_app(app)
ckeditor = CKEditor()
ckeditor.init_app(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow(), index=True)
    can_comment = db.Column(db.Boolean, default=True)
    comments = db.relationship('Comment', back_populates='post', cascade='all,delete-orphan')


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(30))
    email = db.Column(db.String(254))
    site = db.Column(db.String(255))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)

    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    post = db.relationship('Post', back_populates='comments')

    replied_id = db.Column(db.Integer, db.ForeignKey('comment.id'))  # 这个是一
    replies = db.relationship('Comment', back_populates='replied', cascade='all, delete-orphan')
    replied = db.relationship('Comment', back_populates='replies', remote_side=[id])  # 用remote_side来定义远端，那么replied_id就是本地端。


# 下面的例子用来专门演示这个邻接列表关系。
class CommentForm(FlaskForm):
    author = StringField('Name', validators=[DataRequired(), Length(1, 30)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(1, 254)])
    site = StringField('Site', validators=[Optional(), URL(), Length(0, 255)])
    body = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField()


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(1, 20)])
    body = CKEditorField('Body', validators=[DataRequired()])
    submit = SubmitField()


@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    # 这个是先过滤条件，后查询条件，
    pagination = Comment.query.order_by(Comment.timestamp.desc()).paginate(page=page, per_page=per_page)
    comments = pagination.items
    return render_template('index.html', comments=comments, pagination=pagination)


@app.route('/add_comment', methods=['POST', 'GET'])
def add_comment():
    form = CommentForm()
    if form.validate_on_submit():
        author = form.author.data
        email = form.email.data
        site = form.site.data
        body = form.body.data
        comment = Comment(author=author, email=email, site=site, body=body)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_comment.html', form=form)


@app.route('/comment/<int:comment_id>/delete', methods=['POST'])
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    db.session.delete(comment)
    db.session.commit()
    flash('Comment delete')
    return redirect(url_for('index'))


@app.route('/post/<int:post_id>/set_post', methods=['POST'])
def set_comment(post_id):
    post = Post.query.get_or_404(post_id)
    if post.can_comment:
        post.can_comment = False
        flash('this post comment is disable')
    else:
        post.can_comment = True
        flash('this post commen is enable')
    db.session.commit()
    return redirect(url_for('man_posts'))


@app.route('/add_post', methods=['POST', 'GET'])
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        post = Post(title=title, body=body)
        db.session.add(post)
        db.session.commit()
        flash('post create.')
        return redirect(url_for('index'))
    return render_template('add_post.html', form=form)


@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def show_post(post_id):
    post = Post.query.get_or_404(post_id)
    page = request.args.get('page', 1, type=int)
    per_page = 10
    # 通过post_id来查对用得comments的方法
    pagination = Comment.query.with_parent(post).order_by(Comment.timestamp.desc()).paginate(page=page, per_page=per_page)
    comments = pagination.items

    form = CommentForm()
    if form.validate_on_submit():
        author = form.author.data
        email = form.email.data
        site = form.site.data
        body = form.body.data
        comment = Comment(author=author, email=email, site=site, body=body, post=post)

        replied_id = request.args.get('reply')
        if replied_id:
            replied_comment = Comment.query.get_or_404(replied_id)
            comment.replied = replied_comment
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('show_post', post_id=post.id))

    return render_template('post.html', post=post, pagination=pagination, comments=comments, form=form)


@app.route('/reply/comment/<int:comment_id>')
def reply_comment(comment_id):
    commnet = Comment.query.get_or_404(comment_id)
    if not commnet.post.comments:
        flash('Comment is disable')
    #前端接收参数的规则，第一个参数是？ 后面都是#，post_id是填充了url中。
    return redirect(url_for('show_post', post_id=commnet.post_id, reply=commnet.id, author=commnet.author) + '#comment-form')


@app.route('/man_posts', methods=['GET'])
def man_posts():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    # 这个是先过滤条件，后查询条件，
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(page=page, per_page=per_page)
    posts = pagination.items
    return render_template('man_posts.html', posts=posts, pagination=pagination)


@app.route('/post/<int:post_id>/delete', methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted.', 'success')
    return redirect(url_for('index'))


# with app.app_context():
#     # db.drop_all()
#     # db.create_all()
#     #
#     # st1=Student(name='f1',grade=1)
#     # st2=Student(name='f2',grade=2)
#     # st3=Student(name='f3',grade=3)
#     #
#     # te1=Teacher(name='te1',office='math')
#     # te2=Teacher(name='te2',office='bio')
#     # te3=Teacher(name='te3',office='his')
#     # te4=Teacher(name='te4',office='yuwen')
#     # te5=Teacher(name='te5',office='chem')
#     #
#     # st1.teachers.append(te1)
#     # st1.teachers.append(te2)
#     # st1.teachers.append(te3)
#     #
#     # st2.teachers.append(te2)
#     # st2.teachers.append(te3)
#     # st2.teachers.append(te3)
#     #
#     # st3.teachers.append(te3)
#     # st3.teachers.append(te4)
#     # st3.teachers.append(te5)
#     #
#     # # 定义了双向关系后只需要在一侧进行操作，另一侧的关系会自动添加的
#     # db.session.add(st1)
#     # db.session.add(st2)
#     # db.session.add(st3)
#     # db.session.commit()
#
#
#     # migrate 数据库迁移：
#
#     db.create_all()

# with app.app_context():
#     db.drop_all()
#     db.create_all()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
