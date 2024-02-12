from flask_wtf import FlaskForm

from werkzeug.datastructures import FileStorage

from wtforms.validators import DataRequired, Length

from wtforms import FileField
from wtforms import StringField
from wtforms import SubmitField
from wtforms import TextAreaField


class CreatePost(FlaskForm):
    title: str = StringField("Título", validators=[DataRequired(), Length(max=64)])
    tag: str = StringField("Tag", validators=[DataRequired(), Length(max=64)])
    content: str = TextAreaField(
        "Contenido", validators=[DataRequired(), Length(max=2000)]
    )
    imagen: FileStorage = FileField(
        "Imagen", validators=[DataRequired(message="Debe seleccionar una imagen")]
    )
    submit = SubmitField("Crear")


class UpdatePost(FlaskForm):
    title: str = StringField("Título", validators=[DataRequired(), Length(max=64)])
    tag: str = StringField("Tag", validators=[DataRequired(), Length(max=64)])
    content: str = TextAreaField(
        "Contenido", validators=[DataRequired(), Length(max=2000)]
    )
    submit = SubmitField("Actualizar")
