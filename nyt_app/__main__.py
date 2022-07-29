import sys
from controller import Controller
from application_context.factory import ApplicationContextFactory


if __name__ == '__main__':

    app_context = ApplicationContextFactory.make('prod')

    if sys.argv[1] == 'top':
        valid_intervals = ['day', 'week', 'month']

        if sys.argv[2] in valid_intervals:
            Controller.top(app_context, sys.argv[2])

    if sys.argv[1] == 'day':
        if len(sys.argv[2]) == 8 and sys.argv[2].isnumeric():
            Controller.day(app_context, sys.argv[2])
