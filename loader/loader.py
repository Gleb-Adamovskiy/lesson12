from flask import Blueprint, render_template, request, send_from_directory
import functions as func

loader_blueprint = Blueprint('loader', __name__)
# отображение страницы добавления поста, метод GET
@loader_blueprint.route('/post', methods=["GET"])
def loader_page():
    return render_template("post_form.html")

# отображение страницы добавленного поста, метод POST
@loader_blueprint.route("/post", methods=["POST"])
def page_post_upload():
    # захват картинки и текста
    picture = request.files.get("picture")
    content = request.form.get("content")
    # исключение отсутствия контента
    if not picture or not content:
        return "Данных нет("
    # сохоранение картинки и текста поста
    picture_url = func.post_picture(picture)
    func.save_post(picture_url, content)
    return render_template("post_uploaded.html", content=content, picture_url=picture_url)

# добавление папки с загрузками в исключение
@loader_blueprint.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)
