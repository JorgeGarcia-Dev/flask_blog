import cloudinary

from flask import Flask
from flask import url_for
from flask import redirect
from flask import render_template

from app.blog.models import Tag
from app.blog.models import Post
from app.admin.models import User

from app.blog.views import blog_bp
from app.tags.views import tags_bp
from app.index.views import index_bp
from app.admin.views import admin_bp

from flask_bcrypt import Bcrypt

from app.blog.models import PostTag

from flask_login import LoginManager

from flask_wtf.csrf import CSRFProtect

from decouple import config as config_decouple

from app.db.database import MySQLDatabaseSingleton


app = Flask(__name__)

bcrypt = Bcrypt(app)

csrf = CSRFProtect()

login_manager = LoginManager(app)

cloudinary.config(
    cloud_name=config_decouple("CLOUD_NAME"),
    api_key=config_decouple("API_KEY"),
    api_secret=config_decouple("API_SECRET"),
)

database = MySQLDatabaseSingleton().database


@app.errorhandler(404)
def not_found(error):
    return render_template("errors/404.html"), 404


@app.before_request
def before_request():
    database.connect()


@app.after_request
def after_request(response):
    database.close()
    return response


@login_manager.user_loader
def load_user(id):
    user = User.get(User.id == id)

    return user


def pagina_no_encontrada(error):
    return render_template("errors/404.html")


def pagina_no_autorizada(error):
    return redirect(url_for("admin.login"))


def create_app(config):
    app.register_blueprint(blog_bp)
    app.register_blueprint(tags_bp)
    app.register_blueprint(index_bp)
    app.register_blueprint(admin_bp)
    app.config.from_object(config)
    
    csrf.init_app(app)

    with app.app_context():
        # database.drop_tables([User, Post, Tag, PostTag], safe=True)
        database.create_tables([User, Post, Tag, PostTag], safe=True)

    app.register_error_handler(404, pagina_no_encontrada)
    app.register_error_handler(401, pagina_no_autorizada)

    return app
