from .config import Config


class Commander:
    def __init__(self, config: Config):
        self.config = config

    def add(self, *args):
        """new_command"""
        self.config.update({args[0]: {'desc': args[1], 'answer': args[2]}})

    def remove(self, *args):
        """delete_command"""
        return self.config.pop(args[0])

    def check_in(self, name):
        """exist_command"""
        return self.config.get(name)

    def change(self, *args):
        """change_command"""
        if args[0] in self.config:
            self.config[args[0]] = {'desc': args[1], 'answer': args[2]}
            return {'desc': args[1], 'answer': args[2]}

        return None

    def save(self):
        """save"""
        self.config.save()
