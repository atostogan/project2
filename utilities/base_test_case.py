'''
Contains class for setting up environment to run test and doing clean up after it is finished
'''
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import config
from pages.home_page import HomePage


class BaseTestCase(unittest.TestCase):
    '''
    Class for setting up environment to run test and doing clean up after it is finished
    '''
    driver = None

    def setUp(self):
        '''
        Setup before running test
        '''

        if self.driver is None:
            # chrome_options = webdriver.ChromeOptions()
            # self.driver = webdriver.Remote(command_executor=config.SELENIUM_GRID_URL,
            #                                options=chrome_options)
            firefox_options = webdriver.FirefoxOptions()
            self.driver = webdriver.Remote(command_executor=config.SELENIUM_GRID_URL,
                                           options=firefox_options)
            # self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get(config.DEFAULT_URL)
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        '''
        Cleanup after running test
        '''
        if self.driver:
            self.driver.quit()
