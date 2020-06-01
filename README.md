### 创建项目步骤：
1. 使用 PyCharm 创建 Flask 项目
2. 安装 peewee：`pip install peewee`
3. 安装 flask-login：`pip install flask-login`

### cookie 文件夹里内容，运行步骤：
1. models.py（创建数据库及表，只能运行一次）
2. storing_data.py（插入数据，只能运行一次；模拟了一个用户）
3. 运行：`flask run`
4. 访问：`http://127.0.0.1:8001/` ，此时用户未登陆，会跳转到`http://127.0.0.1:5000/need_login?next=%2F`
5. 访问进行登陆动作：`http://127.0.0.1:8001/login`
6. 此时访问：`http://127.0.0.1:8001/` ，会看到页面内容
7. 访问进行登出动作：`http://127.0.0.1:8001/logout`


### 参考资料
参考资料 | 网址
--- | ---
《Flask Web开发实战 : 入门、进阶与原理解析》8.5 使用Flask-Login管理用户认证 | https://weread.qq.com/web/reader/26132b70715ec2fd26119eekc51323901dc51ce410c121b