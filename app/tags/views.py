"""Views for the tags."""
from flask import Blueprint, render_template

from app.blog.models import Post, Tag, PostTag

tags_bp = Blueprint(
    "tags", __name__, template_folder="templates", static_folder="static"
)


@tags_bp.route("/tags/<name_tag>")
def filter_by_tags(name_tag):
    """Filter posts by tag

    Atributes:
    - name_tag (str): The name of the tag.
    - posts (list): The list of posts associated with the tag.

    Returns:
    - The posts associated with the tag.
    """
    tag = Tag.get(Tag.name_tag == name_tag)
    posts = Post.select().join(PostTag).join(Tag).where(Tag.name_tag == name_tag)  # noqa

    return render_template("posts_tags.html", posts=posts, tag=tag)


@tags_bp.route("/tags/post/<int:id>")
def edit_tags(id):
    """Edit tags

    Atributes:
    - id (int): The id of the post to edit.

    Returns:
    - A redirect to the index page.
    """
    post = Post.get(Post.id == id)

    return render_template("post.html", post=post)
