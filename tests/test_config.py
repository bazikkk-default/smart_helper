from helper.config import Config
import pathlib
from os import remove


def test_init():
    assert Config() == {}


def test_load_empty():
    conf = Config()
    conf.load()
    assert conf == {}


def test_load_with_path():
    conf = Config()
    conf.load(path_to_conf=pathlib.Path(__file__).parent.resolve() / 'data' / 'config.json')
    assert conf == {'first_task': 'is_shit'}


def test_save_with_path():
    conf = Config()
    conf.load(path_to_conf=pathlib.Path(__file__).parent.resolve() / 'data' / 'config.json')
    conf.update({'second': 'better'})
    conf.save(path_to_conf=pathlib.Path(__file__).parent.resolve() / 'data' / 'test_config.json')
    test_conf = Config()
    test_conf.load(path_to_conf=pathlib.Path(__file__).parent.resolve() / 'data' / 'test_config.json')
    remove(pathlib.Path(__file__).parent.resolve() / 'data' / 'test_config.json')
    assert test_conf == {'first_task': 'is_shit', 'second': 'better'}
