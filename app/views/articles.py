from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

articles_app = Blueprint("articles_app", __name__)
ARTICLES = {
    1: {
        "title": "Title 1",
        "text": "Text 1"
    },
    2: {
        "title": "Title 2",
        "text": "Text 2"
    },
    3: {
        "title": "Title 3",
        "text": "Text 3"
    },
}


@articles_app.route("/", endpoint="list")
def users_list():
    return render_template("articles/list.html", articles=ARTICLES)


@articles_app.route("/<int:article_id>/", endpoint="details")
def user_details(article_id: int):
    try:
        article = ARTICLES[article_id]
    except KeyError:
        raise NotFound(f"Article #{article_id} doesn't exist!")
    return render_template('articles/details.html', article_id=article_id, article=article)
