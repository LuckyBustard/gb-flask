from flask import Flask
from views.users import users_app
from views.articles import articles_app
from models.database import db
from models import User
from views.auth import auth_app, login_manager

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////opt/app/data/app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
app.config["SECRET_KEY"] = "abcdefg123456"


@app.route("/")
def index():
    return 'index page'


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("done!")


@app.cli.command("create-users")
def create_users():
    admin = User(username="admin", is_staff=True)
    james = User(username="james")
    db.session.add(admin)
    db.session.add(james)
    db.session.commit()
    print("done! created users:", admin, james)


if __name__ == "__main__":
    app.register_blueprint(users_app, url_prefix="/users")
    app.register_blueprint(articles_app, url_prefix="/articles")
    app.register_blueprint(auth_app, url_prefix="/auth")
    login_manager.init_app(app)

    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True
    )
