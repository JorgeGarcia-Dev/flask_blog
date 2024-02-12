from flask import Blueprint, render_template

from app.blog.models import Post, Tag, PostTag

tags_bp = Blueprint(
    "tags", __name__, template_folder="templates", static_folder="static"
)


@tags_bp.route("/tags/<name_tag>")
def filter_by_tags(name_tag):
    tag = Tag.get(Tag.name_tag == name_tag)
    posts = Post.select().join(PostTag).join(Tag).where(
                                                    Tag.name_tag == name_tag)

    return render_template("posts_tags.html", posts=posts, tag=tag)


@tags_bp.route("/tags/post/<int:id>")
def edit_tags(id):
    post = Post.get(Post.id == id)

    return render_template("post.html", post=post)
