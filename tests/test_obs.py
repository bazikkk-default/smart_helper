from helper.obs import Observer


def test_init():
    obs = Observer()
    assert obs.commander.config == {}
    assert obs.config == {}


def test_new_command():
    obs = Observer()
    for question, attr in obs.new_command():
        assert (question, attr) in [('Назовите команду', 'name'),
                                    ('Что она должна делать', 'desc'),
                                    ('Что мне вам отвечать', 'answer'),
                                    ('Новая команда создана', None)]


def test_delete_command():
    obs = Observer()
    for question, attr in obs.delete_command():
        assert (question, attr) in [('Какую вы команду хотите удалить', 'name'),
                                    ('Хорошо, удаляю', None)]
        
        
def test_duck():
    obs = Observer()
    for question, attr in obs.test():
        assert (question, attr) in [('Кря', None)]


def test_doc():
    methods = [func for func in dir(Observer) if callable(getattr(Observer, func)) and not func.startswith('_')]
    obs = Observer()
    assert all([obs.__getattribute__(func).__doc__ for func in methods])
