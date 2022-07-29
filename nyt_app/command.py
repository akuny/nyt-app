class Command:

    def __init__(self, command: str='', arg: str='') -> None:
        self.is_valid = False
        self.valid_commands = ['top', 'day']
        self.valid_top_args = ['day', 'year', 'month']
        self.validate(command, arg)

    def validate(self, command: str, arg: str) -> None:
        if command in self.valid_commands:
            if command == 'top':
                if arg in self.valid_top_args:
                    self.type = command
                    self.detail = arg
                    self.is_valid = True
            if command == 'day':
                if len(arg) == 8 and arg.isnumeric():
                    self.type = command
                    self.detail = arg
                    self.is_valid = True
