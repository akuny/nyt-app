import sys
from controller import Controller


if __name__ == '__main__':

    if sys.argv[1] == 'top':
        valid_intervals = ['day', 'week', 'month']

        if sys.argv[2] in valid_intervals:
            Controller.top(sys.argv[2])

    if sys.argv[1] == 'day':
        if len(sys.argv[2]) == 8 and sys.argv[2].isnumeric():
            Controller.day(sys.argv[2])
