'''
Contains class for setting up environment to run test and doing clean up after it is finished
'''
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import config


class BaseTestCase(unittest.TestCase):
    '''
    Class for setting up environment to run test and doing clean up after it is finished
    '''
    driver_var = None

    def setUp(self):
        '''
        Setup before running test
        '''
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get(config.DEFAULT_URL)

    def tearDown(self):
        '''
        Cleanup after running test
        '''
        if not self.driver_var:
            self.driver.quit()
