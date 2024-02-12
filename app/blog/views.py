"""Views for the blog."""
from flask import url_for
from flask import redirect
from flask import Blueprint
from flask import render_template

from app.blog.models import Tag
from app.blog.models import Post
from app.blog.models import PostTag

from peewee import IntegrityError

from app.blog.forms import CreatePost
from app.blog.forms import UpdatePost

from flask_login import login_required

from werkzeug.datastructures import FileStorage

import cloudinary.api
import cloudinary.uploader


blog_bp = Blueprint(
    "blog", __name__, template_folder="templates", static_folder="static"
)


@blog_bp.route("/post/<int:id>")
def post(id) -> str:
    """Show post

    Atributes:
    - id (int): The id of the post to show.

    Returns:
    - The post template with the post data.
    """
    post: Post = Post.get(Post.id == id)

    return render_template("post.html", post=post)


@blog_bp.route("/posts/create", methods=["GET", "POST"])
@login_required
def create_post() -> str:
    """Create new post

    Atributes:
    - title (StringField): The title of the post.
    - tag (StringField): The tag associated with the post.
    - content (TextAreaField): The content of the post.
    - imagen (FileStorage): The image file uploaded for the post.
    - submit (SubmitField): The button to submit the form and create the post.

    Returns:
    - A redirect to the index page.
    """
    form: CreatePost = CreatePost()
    if form.validate_on_submit():
        title: str = form.title.data
        tag: str = form.tag.data
        content: str = form.content.data
        image: FileStorage = form.imagen.data
        folder_name: str = "BlogProject/ImgBlogPosts"
        image_uploaded: dict = cloudinary.uploader.upload(
            image,
            folder=folder_name)

        try:
            if image.filename != "":
                route = image_uploaded["secure_url"]

            new_post: Post = Post.create(title=title,
                                         content=content,
                                         route=route)

            new_tag: Tag = Tag.create(name_tag=tag)

            PostTag.create(post=new_post, tag=new_tag)

            return redirect(url_for("index.index"))

        except IntegrityError:
            return "Title or Tag already exists", 409

    return render_template("create.html", form=form)


@blog_bp.route("/edit/<int:id>", methods=["GET", "POST"])
@login_required
def edit_post(id) -> str:
    """Edit post

    Atributes:
    - id (int): The id of the post to edit.

    Returns:
    - A redirect to the index page.
    """
    form: UpdatePost = UpdatePost()
    if form.validate_on_submit():
        title: str = form.title.data
        tag: str = form.tag.data
        content: str = form.content.data

        try:
            post: Post = Post.update(
                title=title,
                content=content).where(Post.id == id)
            post.execute()

            tag: Tag = Tag.update(name_tag=tag).where(Tag.id == id)
            tag.execute()

            return redirect(url_for("index.index"))

        except IntegrityError:
            return "Title or Tag already exists", 409

    return render_template(
        "edit.html",
        post=Post.get(Post.id == id),
        tag=Tag.get(Tag.id == id),
        form=form,
    )


@blog_bp.route("/delete/<int:id>")
@login_required
def delete_post(id) -> str:
    """Delete post

    Atributes:
    - id (int): The id of the post to delete.

    Returns:
    - A redirect to the index page.
    """
    folder_name: str = "BlogProject/ImgBlogPosts"
    destroy: dict = cloudinary.uploader.destroy(
        "naughty_anteater", folder=folder_name, invalidate=True
    )

    post: Post = Post.get(Post.id == id)
    tag: Tag = Tag.get(Tag.id == id)
    tag.delete_instance()

    post.delete_instance(destroy)

    return redirect(url_for("index.index"))
