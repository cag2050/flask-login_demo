from flask_login import UserMixin
from peewee import Model, SqliteDatabase, CharField, AutoField

# 路径写死了，待解决：怎么不写死
db = SqliteDatabase('/Users/chenag/Documents/PycharmProjects/flask-login_demo' + '/cookie/people.db')


class Admin(Model, UserMixin):
    class Meta:
        database = db

    id = AutoField()
    name = CharField()


db.connect()
db.create_tables([Admin])
