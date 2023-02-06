from flask import Flask, request, render_template, jsonify
from utils import *
import logging
import json


logger_one = logging.getLogger("one")
file_handler_one = logging.FileHandler("logs/api.log")
formatter_one = logging.Formatter("%(levelname)s : %(asctime)s : %(message)s")
file_handler_one.setFormatter(formatter_one)
logger_one.addHandler(file_handler_one)

app = Flask(__name__, template_folder='templates')
app.config["JSON_AS_ASCII"] = False

@app.route('/')
def page_index():
    posts = load_posts()
    return render_template("index.html", posts=posts)


@app.route('/posts/<post_id>')
def get_post_if(post_id):
    comment = get_comments_by_post_id(int(post_id))
    post = get_post_by_pk(int(post_id))
    return render_template("post.html", post=post, comment=comment)


@app.route('/search')
def get_post_word():
    s = request.args['s']
    posts = search_for_posts(s)
    return render_template("search.html", posts=posts)


@app.route('/users/<username>')
def get_user_name(username):
    posts = get_posts_by_user(username)
    return render_template("user-feed.html", posts=posts)


@app.errorhandler(404)
def error_404(e):
    return 'Такое не найдено', 404


@app.errorhandler(500)
def error_500(e):
    return 'Internal Server Error ', 500


@app.route('/api/posts')
def api_posts():
    try:
        logger_one.info('api request, get all posts')
        posts = load_posts()
        return jsonify(posts)
    except:
        logger_one.error('ERROR')


@app.route("/api/post/<int:pk>")
def api_post(pk):
    post = get_post_by_pk(pk)
    logger_one.info('api request, get all posts')
    return jsonify(post)
    logger_one.error('ERROR')
    print(post)


app.run()
