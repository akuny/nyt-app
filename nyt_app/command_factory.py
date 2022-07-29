from typing import List
from command import Command


class CommandFactory:

    def make(args: List[str]) -> Command:
        if len(args) == 2:
            command, arg = args
            return Command(command, arg)

        return Command()
