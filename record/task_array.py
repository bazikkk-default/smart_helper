from helper.obs import Observer
from utils import exist_method, get_method_by_comment
from voice.main import Voice

from uuid import uuid4
from typing import List, Callable, Union


class Task:
    question: Union[str, None] = None
    status: Union[str, None] = None
    method: Union[Callable, None] = None

    def __init__(self, **kwargs):
        self.question = kwargs.get('question', None)
        self.method = kwargs.get('method', Observer().test())
        self.status = kwargs.get('status', None)

    def is_active(self):
        return self.status == 'running'

    def save(self):
        return {'question': self.question, 'status': self.status,
                'method': self.method}


class Loop:
    baggage: List = []
    result: List = []
    current_task:  Union[str, None, Task] = None

    def __init__(self, obs: Observer = None):
        self.obs = obs or Observer()

    def __create_task(self, query):
        if exist_method(self.obs, query):
            method = get_method_by_comment(self.obs, query)
            self.method = method()
            return Task(observer=self.obs, method=self.method)
        else:
            Voice.say('Ага ещё чего')
        return

    def append(self, query):
        task = self.__create_task(query)
        if task:
            self.baggage.append({str(uuid4()): task.save()})
        return bool(task)

    def run(self):
        if not self.current_task:
            self.current_task = self.baggage[0] if self.baggage else None

        for source in self.baggage:
            number, task_kwargs = next(iter(source)), source[next(iter(source))]

            task = Task(**task_kwargs)
            task.question, attr = task.method.__next__()
            if attr:
                self.baggage[self.baggage.index({number: task_kwargs})] = {number: task.save()}
                return task.question, attr

            else:
                self.baggage.remove({number: task_kwargs})
                self.current_task = self.baggage[0] if self.baggage else None
                return self.run()

        if not self.current_task:
            return None, None

    def answer(self, answer):
        self.result.append(answer)
        return self.run()




