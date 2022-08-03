class Command:

    def __init__(self, command: str='', arg: str='') -> None:
        self.is_valid = False
        self.valid_commands = ['popular', 'day', 'section']
        self.valid_popular_args = ['day', 'year', 'month']
        self.valid_section_args = [
            'arts', 'books', 'business', 'education', 'fashion', 'food',
            'health', 'home', 'magazine', 'movies', 'national', 'opinion',
            'politics', 'science', 'sports', 'style', 'sundayreview',
            'technology','travel', 'upshot', 'us', 'world'
        ]
        self.validate(command, arg)

    def validate(self, command: str, arg: str) -> None:
        if command in self.valid_commands:
            if command == 'popular':
                if arg in self.valid_popular_args:
                    self.type = command
                    self.detail = arg
                    self.is_valid = True
            if command == 'day':
                if len(arg) == 8 and arg.isnumeric():
                    self.type = command
                    self.detail = arg
                    self.is_valid = True
            if command == 'section':
                if arg in self.valid_section_args:
                    self.type = command
                    self.detail = arg
                    self.is_valid = True
