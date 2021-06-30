import time
from pathlib import Path
import os
import psutil
from random import randbytes
from abstract_testcase import AbstractTestCase
import logging

logger = logging.getLogger()


def cls_logger():
    """Decorator for classes. Getts all attributes in class, filter dunder and not callable, then decorate."""
    def decorator(cls):
        for atr_name in dir(cls):
            if atr_name.startswith('__'):
                continue
            atr = getattr(cls, atr_name)
            if hasattr(atr, '__call__'):
                decorated_atr = logger_for_method(cls, atr)
                setattr(cls, atr_name, decorated_atr)
        return cls

    return decorator


def logger_for_method(cls, func):
    """Adds logger to the attribute"""
    def logged_method(self):
        doc = getattr(cls.__bases__[0], func.__name__).__doc__
        logger.info(f'{doc}')
        func(self)
        return func

    return logged_method


class NotEvenSecondsError(Exception):
    pass


class NotEnoughSystemMemoryError(Exception):
    pass


@cls_logger()
class TestCase1(AbstractTestCase):
    def prep(self):
        seconds = int(time.time())
        if int(seconds) % 2:
            raise NotEvenSecondsError(f'Seconds not even, seconds={seconds}')

    def run(self):
        print(*os.listdir(Path.home()), sep='\n')

    def clean_up(self):
        pass


@cls_logger()
class TestCase2(AbstractTestCase):
    def prep(self):
        if psutil.virtual_memory().total < 1073741824:
            raise NotEnoughSystemMemoryError('System memory < 1Gb.')

    def run(self):
        with open('test', 'wb') as file:
            for _ in range(1024):
                file.write(randbytes(1048576))

    def clean_up(self):
        os.remove('test')


def run_tests():
    test_1 = TestCase1(tc_id=0, name='even_seconds')
    test_1.execute()
    test_2 = TestCase2(tc_id=1, name='random')
    test_2.execute()
