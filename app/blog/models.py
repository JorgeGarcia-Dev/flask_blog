import peewee

from datetime import datetime

from app.db.database import MySQLDatabaseSingleton


database = MySQLDatabaseSingleton().database


class BaseModel(peewee.Model):
    class Meta:
        database = database


class Post(BaseModel):
    title: str = peewee.CharField(max_length=60)
    content: str = peewee.TextField()
    route: str = peewee.CharField()
    created_at: datetime = peewee.DateTimeField(default=datetime.now)

    class Meta:
        db_table: str = "posts"

    def __str__(self):
        return self.title


class Tag(BaseModel):
    name_tag: str = peewee.CharField(max_length=60)

    class Meta:
        db_table: str = "tags"

    def __str__(self):
        return self.title


class PostTag(BaseModel):
    post: str = peewee.ForeignKeyField(Post, backref="tags", on_delete="CASCADE")
    tag: str = peewee.ForeignKeyField(Tag, backref="posts", on_delete="CASCADE")

    class Meta:
        db_table: str = "posts_tags"

    def __str__(self):
        return self.title
