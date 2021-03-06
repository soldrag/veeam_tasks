import time
from pathlib import Path
import os
import psutil
from random import randbytes
from abstract_testcase import AbstractTestCase
import logging

logger = logging.getLogger()


def cls_logger():
    """Decorator for classes. Gets all attributes in class, filter dunder and not callable, then decorate."""

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


def logger_for_method(cls, atr):
    """Adds logger to the attribute"""

    def logged_method(self):
        doc = getattr(cls.__bases__[0], atr.__name__).__doc__
        logger.info(f'{doc}')
        atr(self)
        return atr

    return logged_method


class NotEvenSecondsError(Exception):
    pass


class NotEnoughSystemMemoryError(Exception):
    pass


@cls_logger()
class TestCase1(AbstractTestCase):
    def prep(self) -> None:
        seconds = int(time.time())
        if int(seconds) % 2:
            raise NotEvenSecondsError(f'Seconds not even, seconds={seconds}')

    def run(self) -> None:
        print(*os.listdir(Path.home()), sep='\n')

    def clean_up(self) -> None:
        pass


@cls_logger()
class TestCase2(AbstractTestCase):
    def prep(self) -> None:
        if psutil.virtual_memory().total < 1073741824:
            raise NotEnoughSystemMemoryError('System memory < 1Gb.')

    def run(self) -> None:
        with open('test', 'wb') as file:
            for _ in range(1024):
                file.write(randbytes(1048576))

    def clean_up(self) -> None:
        os.remove('test')


def run_tests() -> None:
    test_1 = TestCase1(tc_id=0, name='even_seconds')
    test_1.execute()
    test_2 = TestCase2(tc_id=1, name='random')
    test_2.execute()
