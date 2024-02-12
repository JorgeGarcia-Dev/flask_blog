"""Models for the admin."""
import peewee

from flask_login import UserMixin

from datetime import datetime

from app.db.database import MySQLDatabaseSingleton


database = MySQLDatabaseSingleton().database


class BaseModel(peewee.Model):
    """Base model."""

    class Meta:
        database = database


class User(UserMixin, BaseModel):
    """User model

    Atributes:
    - name (CharField): The name of the user.
    - email (CharField): The email of the user.
    - password (CharField): The password of the user.
    - active (BooleanField): Whether the user is active or not.
    - created_at (DateTimeField): The date and time the user was created.
    """

    name = peewee.CharField(max_length=60, null=True)
    email = peewee.CharField(max_length=60, null=True, unique=True)
    password = peewee.CharField(max_length=60, null=True, unique=True)
    active = peewee.BooleanField(default=True)
    created_at = peewee.DateTimeField(default=datetime.now)

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.title
