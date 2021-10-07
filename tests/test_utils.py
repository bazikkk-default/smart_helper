from helper.obs import Observer
from utils import get_method_by_comment, exist_method


def test_exist_method():
    obs = Observer()
    assert exist_method(obs, 'test')


def test_get_method_by_comment():
    obs = Observer()
    assert callable(get_method_by_comment(obs, 'test'))
