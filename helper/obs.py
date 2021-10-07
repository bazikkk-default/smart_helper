from .config import Config
from .command import Commander


class Observer:
    method = None

    def __init__(self):
        self.config = Config()
        self.config.load()
        self.commander = Commander(self.config)

    def new_command(self):
        """новая команда"""
        for question, attr in [('Назовите команду', 'name'),
                               ('Что она должна делать', 'desc'),
                               ('Что мне вам отвечать', 'answer'),
                               ('Новая команда создана', None)]:
            yield (question, attr)

    def delete_command(self):
        """удалить команду"""
        for question, attr in [('Какую вы команду хотите удалить', 'name'),
                               ('Хорошо, удаляю', None)]:
            yield (question, attr)

    def test(self):
        """test"""
        for question, attr in [('Кря', None)]:
            yield (question, attr)

