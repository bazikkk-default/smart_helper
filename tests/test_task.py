from record.task_array import Task
from helper.obs import Observer


def test_init():
    task = Task(question='really', method=Observer().test(), status=None)
    assert task.question == 'really'
    assert task.status is None
    assert task.method.__name__ == 'test'


def test_is_active():
    task = Task(question='really', method=Observer().test(), status='running')
    assert task.is_active()


def test_not_active():
    task = Task(question='really', method=Observer().test(), status='finish')
    assert not task.is_active()


def test_save():
    method = Observer().test()
    task = Task(question='really', method=method, status='finish')
    assert task.save() == {'question': 'really', 'status': 'finish', 'method': method}
