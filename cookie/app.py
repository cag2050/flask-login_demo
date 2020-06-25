from flask import Flask
from flask_login import LoginManager, login_required, login_user, logout_user

from cookie.models import Admin

app = Flask(__name__)
app.secret_key = 'secret string'
# 实例化扩展提供的LoginManager类，创建一个login_manager对象
login_manager = LoginManager()
# 在程序包的工厂函数中对login_manager对象调用init_app()方法进行初始化扩展
login_manager.init_app(app)
# 默认情况下，当未登录的用户尝试访问一个 login_required 装饰的视图，Flask-Login 会闪现一条消息并且重定向到登录视图。
# (如果未设置登录视图，它将会以 401 错误退出。)
# 也可以指定跳转到的视图函数
login_manager.login_view = 'need_login'
login_manager.login_message_category = 'warning'


@login_manager.user_loader
def loader_user(user_id):
    from cookie.models import Admin
    user = Admin.select().where(Admin.id == user_id).get()
    return user


@app.route('/')
@login_required
def home():
    return "<h1>Hello Flask!</h1>"


@app.route('/need_login')
def need_login():
    return "<h1>need_login</h1>"


@app.route('/login', methods=['GET'])
def login():
    admin1 = Admin.select().get()
    login_user(admin1)
    print(admin1.name + '登陆成功')
    return "<h1>登陆成功，</h1>"


@app.route('/logout', methods=['GET'])
def logout():
    logout_user()
    print('登出成功')
    return "<h1>登出成功，</h1>"
