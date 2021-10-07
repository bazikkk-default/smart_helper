from json import load, dump
from os import path


class Config(dict):
    def save(self, path_to_conf: str = 'config.json'):
        with open(path_to_conf, 'w') as fp:
            dump(self, fp)

    def load(self, path_to_conf: str = 'config.json'):
        if path.isfile(path_to_conf):
            with open(path_to_conf, 'r') as fp:
                self.update(load(fp))
        else:
            self.update({})
