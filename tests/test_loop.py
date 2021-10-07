from record.task_array import Loop, Task
from unittest.mock import MagicMock, patch
from uuid import UUID


def test_init():
    loop = Loop()
    assert loop.baggage == []


def test_append():
    loop = Loop()
    with patch('record.task_array.uuid4', MagicMock(return_value=UUID('11111111-1111-1111-1111-111111111111'))):
        loop.append('test')

    for task in loop.baggage:
        assert '11111111-1111-1111-1111-111111111111' in task
        assert task['11111111-1111-1111-1111-111111111111']
        assert task['11111111-1111-1111-1111-111111111111']['status'] == None
        assert task['11111111-1111-1111-1111-111111111111']['question'] == None


def test_run():
    loop = Loop()
    with patch('record.task_array.uuid4', MagicMock(return_value=UUID('11111111-1111-1111-1111-111111111111'))):
        loop.append('test')

    assert loop.run() == True
    assert loop.current_task
