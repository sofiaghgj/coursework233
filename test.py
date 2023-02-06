import pytest
from utils import *


def test_data():
    assert type(load_data("data/posts.json")) == list
    assert type(load_data("data/posts.json")[0]) == dict


def test_comment():
    assert type(get_comments_all() == list)
