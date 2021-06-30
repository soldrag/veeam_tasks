from abc import ABC, abstractmethod


class AbstractTestCase(ABC):
    def __init__(self, tc_id, name):
        self.tc_id = tc_id
        self.name = name

    @abstractmethod
    def prep(self, *args, **kwargs):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def clean(self):
        pass

    @abstractmethod
    def exec(self):
        self.prep()
        self.run()
        self.clean()
