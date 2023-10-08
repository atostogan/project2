'''
Contains class for setting up environment to run test and doing clean up after it is finished
'''
import pytest
from selenium import webdriver
import config
from pages.home_page import HomePage


class BaseTestCase:
    '''
    Class for setting up environment to run test and doing clean up after it is finished
    '''
    home_page = None

    @staticmethod
    @pytest.fixture(scope='class')
    def driver(browser):
        '''
        Returns driver when test gets to run and quits driver after the test finished running
        '''
        chrome_options = webdriver.ChromeOptions()
        firefox_options = webdriver.FirefoxOptions()
        edge_options = webdriver.EdgeOptions()
        driver_map = {
            'chrome': chrome_options,
            'firefox': firefox_options,
            'edge': edge_options
        }
        driver = webdriver.Remote(command_executor=config.SELENIUM_GRID_URL, options=driver_map[browser])
        driver.get(config.DEFAULT_URL)
        yield driver
        driver.quit()

    @pytest.fixture(scope='class')
    def home_page(self, driver):
        '''
        Returns HomePage object which is being used to run tests
        '''
        driver.get(config.DEFAULT_URL)
        return HomePage(driver)
