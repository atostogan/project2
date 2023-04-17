'''
Contains methods applicable for all other pages
'''
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    '''
    Class for storing methods applicable for all other pages
    '''
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_to_load(self, by_locator, timeout=10):
        '''
        Wait for element to load
        '''
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locator))
