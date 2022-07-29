import sys
from command_factory import CommandFactory
from command_bus import CommandBus
from application_context.factory import ApplicationContextFactory


if __name__ == '__main__':

    app_context = ApplicationContextFactory.make('prod')
    command = CommandFactory.make(sys.argv[1:])
    CommandBus.handle(app_context, command)
