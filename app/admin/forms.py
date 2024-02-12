from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length


# class SignupForm(FlaskForm):
#     name = StringField("Nombre", validators=[DataRequired(), Length(max=64)])
#     password = PasswordField("Password", validators=[DataRequired()])
#     email = StringField("Email", validators=[DataRequired(), Email()])
#     submit = SubmitField("Registrarme")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Iniciar sesión")
