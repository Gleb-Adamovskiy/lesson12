from flask import Blueprint, render_template, request
import functions as func
import logging

main_blueprint = Blueprint('main', __name__)
logging.basicConfig(filename="info.log", level=logging.INFO)

@main_blueprint.route('/')
def main_page():
    return render_template("index.html")

# отображение поиска
@main_blueprint.route("/search")
def page_tag():
    s = request.args['s']
    posts = func.get_posts(s)
    logging.info("Запрос поиска")
    return render_template("post_list.html", posts=posts, s=s)

