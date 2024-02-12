import peewee

from flask_login import UserMixin

from datetime import datetime

from app.db.database import MySQLDatabaseSingleton


database = MySQLDatabaseSingleton().database


class BaseModel(peewee.Model):
    class Meta:
        database = database


class User(UserMixin, BaseModel):
    name = peewee.CharField(max_length=60, null=True)
    email = peewee.CharField(max_length=60, null=True, unique=True)
    password = peewee.CharField(max_length=60, null=True, unique=True)
    active = peewee.BooleanField(default=True)
    created_at = peewee.DateTimeField(default=datetime.now)

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.title
