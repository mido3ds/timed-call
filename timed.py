''' Timed Call for a function, useful for game-dev
    Mahmoud Adas, 2017, mido3ds@gmail.com
'''
from time import time, sleep


def timed_loop(call_per_sec):
    ''' Int -> Yield None 
        generator for timed functions
        Usage:
            >>> for _ in timed_loop(60):
            ...     # do stuff here 60 times per second
            ...     pass
            >>> """get to this after KeyboardInterrupt"""
    '''
    interval = 1 / call_per_sec
    while True:
        start = time()
        yield
        diff = time() - start

        if diff <= interval:
            sleep(interval - diff)


class TimedFunction:

    def __init__(self, function, call_per_sec):
        self.function = function
        self.cps = call_per_sec

    def start(self, *args, **kwargs):
        for _ in timed_loop(self.cps):
            self.function(args, kwargs)
