"""Models for the blog."""
import peewee

from datetime import datetime

from app.db.database import MySQLDatabaseSingleton


database = MySQLDatabaseSingleton().database


class BaseModel(peewee.Model):
    class Meta:
        database = database


class Post(BaseModel):
    """Post model

    Atributes:
    - title (CharField): The title of the post.
    - content (TextField): The content of the post.
    - route (CharField): The route of the post.
    - created_at (DateTimeField): The date and time the post was created.
    """

    title: str = peewee.CharField(max_length=60)
    content: str = peewee.TextField()
    route: str = peewee.CharField()
    created_at: datetime = peewee.DateTimeField(default=datetime.now)

    class Meta:
        db_table: str = "posts"

    def __str__(self):
        return self.title


class Tag(BaseModel):
    """Tag model

    Atributes:
    - name_tag (CharField): The name of the tag.
    """

    name_tag: str = peewee.CharField(max_length=60)

    class Meta:
        db_table: str = "tags"

    def __str__(self):
        return self.title


class PostTag(BaseModel):
    """PostTag model

    Atributes:
    - post (ForeignKeyField): The post associated with the tag.
    - tag (ForeignKeyField): The tag associated with the post.
    """

    post: str = peewee.ForeignKeyField(
        Post,
        backref="tags",
        on_delete="CASCADE")
    tag: str = peewee.ForeignKeyField(
        Tag,
        backref="posts",
        on_delete="CASCADE")

    class Meta:
        db_table: str = "posts_tags"

    def __str__(self):
        return self.title
