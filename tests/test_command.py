from helper.config import Config
from helper.command import Commander


def test_init():
    commander = Commander(config=Config())
    assert commander.config == Config()


def test_add():
    commander = Commander(config=Config())
    commander.add('name', 'description', 'answer')
    assert commander.config == {'name': {'desc': 'description', 'answer': 'answer'}}


def test_remove():
    commander = Commander(config=Config({'name': {'desc': 'description', 'answer': 'answer'}}))
    commander.remove('name')
    assert commander.config == {}


def test_change():
    commander = Commander(config=Config({'name': {'desc': 'description', 'answer': 'answer'}}))
    commander.change('name', 'description', 'ANSWER')
    assert commander.config == {'name': {'desc': 'description', 'answer': 'ANSWER'}}


def test_fail_change():
    commander = Commander(config=Config({'name': {'desc': 'description', 'answer': 'answer'}}))
    commander.change('google', 1, 1)
    assert commander.config == {'name': {'desc': 'description', 'answer': 'answer'}}


def test_check_in():
    commander = Commander(config=Config({'name': {'desc': 'description', 'answer': 'answer'}}))
    assert commander.check_in('name')


def test_fail_check_in():
    commander = Commander(config=Config({'name': {'desc': 'description', 'answer': 'answer'}}))
    assert not commander.check_in('google')


def test_doc():
    methods = [func for func in dir(Commander) if callable(getattr(Commander, func)) and not func.startswith('_')]
    commander = Commander(config=Config())
    assert all([commander.__getattribute__(func).__doc__ for func in methods])
