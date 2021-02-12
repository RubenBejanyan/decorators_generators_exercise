from functools import wraps
from datetime import datetime
from time import sleep
import random


def ending(number: int):
    if number % 10 == 1 and number % 100 != 11:
        end = 'st'
    elif number % 10 == 2 and number % 100 != 12:
        end = 'nd'
    elif number % 10 == 3 and number % 100 != 13:
        end = 'rd'
    else:
        end = 'th'
    return end


def retry(exceptions: tuple, tries: int, delay: int, backoff: int = 0, logger=None):
    def retry_wrapper(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            my_counter = 1
            my_delay = delay  # ask about it
            while my_counter <= tries:
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    print(f'{datetime.now()} :: Retrying {func.__name__} {my_counter}-{ending(my_counter)} time!')
                    sleep(my_delay)
                    if backoff > 0:
                        my_delay *= backoff
                    my_counter += 1
            return func(*args, **kwargs)

        return wrapper

    return retry_wrapper


@retry((TypeError, ValueError), tries=25, delay=1, backoff=0, logger=None)
def random_numbers_interval(p, q):
    """ function generates random number in interval [0,1], p, q are from [0,1] interval"""
    random_number = random.random()
    if p >= q:
        raise SyntaxError('lower bound must be less then upper bound!')
    if random_number < p:
        raise TypeError('less than lower bound')
    if random_number > q:
        raise ValueError('grader than upper bound')
    return "yes! you guess interval!"


if __name__ == '__main__':
    print(random_numbers_interval(0.7, 0.9))
