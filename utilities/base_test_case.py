'''
Contains class for setting up environment to run test and doing clean up after it is finished
'''
import unittest
from selenium import webdriver


class BaseTestCase(unittest.TestCase):
    '''
    Class for setting up environment to run test and doing clean up after it is finished
    '''

    def setUp(self):
        '''
        Setup before running test
        '''
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://google.com")

    def tearDown(self):
        '''
        Cleanup after running test
        '''
        self.driver.close()
