"""Flask-WTF form classes for admin views."""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    """Login form

    Validates that username matches, and password is correct.
    """

    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Iniciar sesión")


class RegisterForm(FlaskForm):
    """Register new user

    Atributes:
    - name (StringField): The name of the user.
    - email (StringField): The email of the user.
    - password (PasswordField): The password of the user.
    - submit (SubmitField): The button to submit the form and register the user.
    """

    name = StringField("Nombre", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Registrarme")
