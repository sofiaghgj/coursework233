import json


def load_data(filename):
    with open(filename) as file:
        return json.load(file)


def load_posts():
    return load_data('data/posts.json')


def get_comments_all():
    with open('data/comments.json', encoding='utf-8') as f:
        comments = json.load(f)
        return comments


def get_posts_by_user(user_name):
    list_posts = []
    posts = load_posts()
    for post in posts:
        if user_name.lower() == post["poster_name"]:
            list_posts.append(post)
    if len(list_posts) == 0:
        raise ValueError
    return list_posts


def get_comments_by_post_id(post_id):
    list_comments = []
    comments = get_comments_all()
    for comment in comments:
        if post_id == comment["post_id"]:
            list_comments.append(comment)
    if len(list_comments) == 0:
        raise ValueError
    return list_comments


def search_for_posts(query):
    comment = []
    for i in load_posts():
        if query.lower() in i["content"].lower():
            comment.append(i)
    return comment


def get_post_by_pk(pk):
    for i in load_posts():
        if pk == i["pk"]:
            return i

