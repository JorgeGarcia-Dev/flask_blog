from flask import Blueprint
from flask import render_template

from app.blog.models import Tag
from app.blog.models import Post

index_bp = Blueprint(
    "index", __name__, template_folder="templates", static_folder="static"
)


@index_bp.route("/")
def index() -> str:
    posts: list = Post.select(Post.id, Post.route, Post.title, Post.content)
    tags: list = Tag.select(Tag.name_tag.distinct())

    return render_template("index.html", posts=posts, tags=tags)
