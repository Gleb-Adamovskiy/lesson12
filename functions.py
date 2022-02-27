import json
import logging

def load_posts_from_json():
    """
    загрузка всех постов
    """
    try:
        with open("posts.json", encoding="utf8") as f:
            posts = json.load(f)
        return posts
    except (FileNotFoundError, json.JSONDecodeError):
        print("Файл не открывается")


def get_posts(posts_fragment):
    """
    возвращаем посты по фрагменту
    """
    posts = load_posts_from_json()
    posts_custom = []
    posts_fragment_lower = posts_fragment.lower()
    for post in posts:
        if posts_fragment_lower in post["content"].lower():
            posts_custom.append(post)

    return posts_custom


def post_picture(picture):
    """
    сохранение картинки
    """
    logging.basicConfig(filename="info.log", level=logging.INFO)
    # проверяем расширение файла на допустимый формат
    picture_name = picture.filename
    picture_format = picture_name.split(".")[-1]
    if picture_format not in ["jpg", "jpeg", "png", "svg"]:
        logging.info("Неверный тип файла")
        return "Неверный тип файла"
    try:
        picture.save(f"./uploads/images/{picture_name}")
    except TypeError:
        logging.info("Ошибка загрузки файла")
        print("Файл не загружен")
    return f"/uploads/images/{picture_name}"


def save_post(picture_url, post):
    # перезаписываем файл с постами
    posts = load_posts_from_json()
    posts.append({'pic':picture_url, 'content': post})
    with open("posts.json", "w", encoding="utf8") as f:
        json.dump(posts, f)
