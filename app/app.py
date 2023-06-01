import os
from flask import Flask
from views.users import users_app
from views.articles import articles_app
from views.authors import authors_app
from models.database import db
from security import flask_bcrypt
from views.auth import auth_app, login_manager
from flask_migrate import Migrate
from models.tag import Tag
from api import init_api
from admin import admin

app = Flask(__name__)

cfg_name = os.environ.get("CONFIG_NAME") or "ProductionConfig"
app.config.from_object(f"configs.{cfg_name}")
db.init_app(app)
app.config["SECRET_KEY"] = "abcdefg123456"
flask_bcrypt.init_app(app)
migrate = Migrate(app, db)
admin.init_app(app)
api = init_api(app)


@app.cli.command("create-tags")
def create_tags():
    """
    Run in your terminal:
    ➜ flask create-tags
    """
    for name in [
        "flask",
        "django",
        "python",
        "sqlalchemy",
        "news",
    ]:
        tag = Tag(name=name)
        db.session.add(tag)

    db.session.commit()
    print("created tags")


@app.route("/")
def index():
    return 'index page'


app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(articles_app, url_prefix="/articles")
app.register_blueprint(auth_app, url_prefix="/auth")
app.register_blueprint(authors_app, url_prefix="/authors")
login_manager.init_app(app)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True
    )
