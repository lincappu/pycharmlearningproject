from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, login_required, login_user, logout_user, UserMixin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

# Flask-Login 初始化
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# 在此处模拟用户
class User(UserMixin):
    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return f"<User {self.id}>"

# 模拟数据库
users = {'foo@bar.tld': {'password': 'secret'}}

# 通过用户 ID 加载用户
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

# 登录页面
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        if email in users and password == users['password']:
            user = User(email)
            login_user(user)
            return redirect(url_for("index"))

    return render_template("login.html")

# 登出
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))


# 主页
@app.route("/")
@login_required
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)