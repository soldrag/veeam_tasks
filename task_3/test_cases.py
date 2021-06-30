import time
from pathlib import Path
import os
import psutil
from random import randbytes
from abstract_testcase import AbstractTestCase


class NotEvenSecondsError(Exception):
    pass


class NotEnoughSystemMemoryError(Exception):
    pass


class TestCase1(AbstractTestCase):
    def prep(self):
        if not int(time.time()) % 2:
            raise NotEvenSecondsError()

    def run(self):
        print(*os.listdir(Path.home()), sep='\n')

    def clean(self):
        pass

    def exec(self):
        try:
            super().exec()
        except NotEvenSecondsError as err:
            print(f'Test "{self.name}" filed. {err}')


class TestCase2(AbstractTestCase):
    def prep(self, *args, **kwargs):
        if psutil.virtual_memory().total < 1073741824 * 10:
            raise NotEnoughSystemMemoryError()

    def run(self):
        with open('test', 'wb') as file:
            for _ in range(1024):
                file.write(randbytes(1048576))

    def clean(self):
        os.remove('test')

    def exec(self):
        try:
            super().exec()
        except NotEnoughSystemMemoryError as err:
            print(f'Test "{self.name}" filed. {err}')


if __name__ == '__main__':
    test_1 = TestCase1(tc_id=0, name='even_seconds')
    test_1.exec()
    test_2 = TestCase2(tc_id=1, name='random')
    test_2.exec()
