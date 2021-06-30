from abc import ABC, abstractmethod
import logging


logger = logging.getLogger("logger")


class AbstractTestCase(ABC):
    def __init__(self, tc_id, name):
        self.tc_id = tc_id
        self.name = name
        testcase_type = self.__class__.__name__
        testcase_id = self.tc_id
        testcase_name = self.name
        logger.info(f'Initialize testcase type: {testcase_type}, id: {testcase_id}, name: {testcase_name}.')

    @abstractmethod
    def prep(self, *args, **kwargs):
        """Start prepare for testcase"""
        pass

    @abstractmethod
    def run(self):
        """Run tests for testcase"""
        pass

    @abstractmethod
    def clean_up(self):
        """Cleaning after testcase"""

    @abstractmethod
    def execute(self):
        """Execute test processes"""
        self.prep()
        self.run()
        self.clean_up()
