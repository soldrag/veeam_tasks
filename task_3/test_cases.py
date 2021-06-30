import time
from pathlib import Path
import os
import psutil
from random import randbytes
from abstract_testcase import AbstractTestCase
from functools import wraps
import logging

logger = logging.getLogger('logger')


def cls_logger():
    def decorator(cls):
        for method in dir(cls):
            if method.startswith('__'):
                continue
            atr = getattr(cls, method)
            if hasattr(atr, '__call__'):
                decorated_atr = log_decorator(cls)(atr)
                setattr(cls, method, decorated_atr)
        return cls
    return decorator


def log_decorator(cls):
    def decorator(func):
        def logged_method(self):
            method_doc_string = getattr(cls.__bases__[0], func.__name__).__doc__
            logger.info(f'{method_doc_string}.')
            func(self)
            return func
        return logged_method
    return decorator


class NotEvenSecondsError(Exception):
    pass


class NotEnoughSystemMemoryError(Exception):
    pass


@cls_logger()
class TestCase1(AbstractTestCase):
    def prep(self):
        """123"""
        if not int(time.time()) % 2:
            raise NotEvenSecondsError()

    def run(self):
        print(*os.listdir(Path.home()), sep='\n')

    def clean_up(self):
        pass

    def execute(self):
        try:
            super().execute()
            logger.info(f'Test "{self.name}" successes\n\n')
        except NotEvenSecondsError as err:
            logger.error(f'Test "{self.name}" filed. {err}\n\n')


@cls_logger()
class TestCase2(AbstractTestCase):
    def prep(self, *args, **kwargs):
        if psutil.virtual_memory().total < 1073741824:
            raise NotEnoughSystemMemoryError()

    def run(self):
        with open('test', 'wb') as file:
            for _ in range(1024):
                file.write(randbytes(1048576))

    def clean_up(self):
        os.remove('test')

    def execute(self):
        try:
            super().execute()
            logger.info(f'Test "{self.name}" successes\n\n')
        except NotEnoughSystemMemoryError as err:
            logger.error(f'Test "{self.name}" filed. {err}\n\n')


def run_tests():
    test_1 = TestCase1(tc_id=0, name='even_seconds')
    test_1.execute()
    test_2 = TestCase2(tc_id=1, name='random')
    test_2.execute()
