from abc import ABC, abstractmethod
import logging

logger = logging.getLogger()


class AbstractTestCase(ABC):
    """Abstract class for testcases"""

    def __init__(self, tc_id: int, name: str) -> None:
        self.tc_id = tc_id
        self.name = name
        testcase_type = self.__class__.__name__
        testcase_id = self.tc_id
        testcase_name = self.name
        logger.info(f'Initialize testcase type: {testcase_type}, id: {testcase_id}, name: {testcase_name}')

    @abstractmethod
    def prep(self) -> None:
        """Start prepare for testcase"""  # These docstrings uses for logging
        pass

    @abstractmethod
    def run(self) -> None:
        """Run tests for testcase"""
        pass

    @abstractmethod
    def clean_up(self) -> None:
        """Cleaning after testcase\n\n"""

    def execute(self) -> None:
        """Execute test processes"""
        try:
            self.prep()
            self.run()
            logger.info(f'Test "{self.name}" successes')
        except BaseException as err:
            logger.error(f'Test "{self.name}" filed. {err}')
        finally:
            self.clean_up()
