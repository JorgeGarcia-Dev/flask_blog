"""Views for the admin."""
from flask import flash
from flask import url_for
from flask import request
from flask import redirect
from flask import Blueprint
from flask import render_template

from app.admin.models import User

from app.admin.forms import LoginForm
# from app.admin.forms import SignupForm

from flask_login import login_user
from flask_login import logout_user

from flask_bcrypt import Bcrypt

from flask_wtf.csrf import generate_csrf

admin_bp = Blueprint(
    "admin", __name__, template_folder="templates", static_folder="static"
)

bcrypt = Bcrypt()


@admin_bp.route("/users/login", methods=["GET", "POST"])
def login():
    """Login form. Validates that username matches, and password is correct.

    Atributes:
    - email (StringField): The email of the user.
    - password (PasswordField): The password of the user.
    - submit (SubmitField): The button to submit the form and login the user.

    Returns:
    - A redirect to the index page.
    """
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        csrf_token: str = generate_csrf()

        try:
            user = User.get(User.email == email)
            if bcrypt.check_password_hash(user.password, password):
                login_user(user)
                flash("Logged in successfully.")
                return redirect(url_for("index.index"))

        except User.DoesNotExist:
            flash("Email o Password incorrectos.")
            return render_template("login.html",
                                   form=form,
                                   csrf_token=csrf_token)

    else:
        return render_template("login.html", form=form)


@admin_bp.route("/logout")
def logout():
    """Logout Form

    Atributes:
    - id (int): The id of the user to update.

    Returns:
    - A redirect to the index page.
    """
    logout_user()

    return redirect(url_for("index.index"))


@admin_bp.route("/users/update/<int:id>", methods=["GET", "POST"])
def update_user(id):
    """Update user

    Atributes:
    - id (int): The id of the user to update.

    Returns:
    - A redirect to the index page.
    """
    if request.method == "POST":
        user = User.update(
            name=request.form["name"],
            email=request.form["email"],
            password=request.form["password"],
        ).where(User.id == id)

        user.execute()

        return redirect(url_for("index.index"))

    return render_template("edit.html")
