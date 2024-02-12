"""Flask-WTF form classes for blog views."""
from flask_wtf import FlaskForm

from werkzeug.datastructures import FileStorage

from wtforms.validators import Length
from wtforms.validators import DataRequired

from wtforms import FileField
from wtforms import StringField
from wtforms import SubmitField
from wtforms import TextAreaField


class CreatePost(FlaskForm):
    """Form for creating a new post.

    Attributes:
    - title (StringField): The title of the post.
    - tag (StringField): The tag associated with the post.
    - content (TextAreaField): The content of the post.
    - imagen (FileStorage): The image file uploaded for the post.
    - submit (SubmitField): The button to submit the form and create the post.
    """

    title: str = StringField(
        "Título", validators=[DataRequired(), Length(max=64)])
    tag: str = StringField("Tag", validators=[DataRequired(), Length(max=64)])
    content: str = TextAreaField(
        "Contenido", validators=[DataRequired(), Length(max=2000)]
    )
    imagen: FileStorage = FileField(
        "Imagen",
        validators=[DataRequired(message="Debe seleccionar una imagen")]
    )
    submit = SubmitField("Crear")


class UpdatePost(FlaskForm):
    """Update post form

    Atributes:
    - title (StringField): The title of the post.
    - tag (StringField): The tag associated with the post.
    - content (TextAreaField): The content of the post.
    - submit (SubmitField): The button to submit the form and update the post.
    """

    title: str = StringField(
        "Título",
        validators=[DataRequired(), Length(max=64)]
    )
    tag: str = StringField("Tag", validators=[DataRequired(), Length(max=64)])
    content: str = TextAreaField(
        "Contenido", validators=[DataRequired(), Length(max=2000)]
    )
    submit = SubmitField("Actualizar")
