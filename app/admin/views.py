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

# from peewee import IntegrityError

from flask_wtf.csrf import generate_csrf

admin_bp = Blueprint(
    "admin", __name__, template_folder="templates", static_folder="static"
)

bcrypt = Bcrypt()


# @admin_bp.route("/users/register", methods=["GET", "POST"])
# def register():
#     form = SignupForm()
#     if form.validate_on_submit():
#         name = form.name.data
#         email = form.email.data
#         password = form.password.data

#         csrf_token: str = generate_csrf()

#         try:
#             new_user = User.create(
#                 name=name,
#                 email=email,
#                 password=bcrypt.generate_password_hash(password).decode("utf-8"),
#             )
#             new_user.save()
#             login_user(new_user)

#         except IntegrityError:
#             return "Username or Email already exists", 409

#         return redirect(url_for("index.index"))

#     return render_template("register.html", form=form, csrf_token=csrf_token)


@admin_bp.route("/users/login", methods=["GET", "POST"])
def login():
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
            return render_template("login.html", form=form, csrf_token=csrf_token)
        

    else:
        return render_template("login.html", form=form)


@admin_bp.route("/logout")
def logout():
    logout_user()

    return redirect(url_for("index.index"))


@admin_bp.route("/users/update/<int:id>", methods=["GET", "POST"])
def update_user(id):
    if request.method == "POST":
        user = User.update(
            name=request.form["name"],
            email=request.form["email"],
            password=request.form["password"],
        ).where(User.id == id)

        user.execute()

        return redirect(url_for("index.index"))

    return render_template("edit.html")
