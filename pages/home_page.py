'''
Contains functions for getting element reference
'''
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    '''
    Class for storing HomePage elements
    '''
    search_field = (By.CSS_SELECTOR, '[name = "q"]')
    google_search_button = (By.CSS_SELECTOR, '[name = "btnK"]')

    def get_search_field(self):
        '''
        Returns reference to the search_field
        '''
        return self.driver.find_element(*self.search_field)

    def get_google_search_button(self):
        '''
        Returns reference to the google_search_button
        '''
        return self.driver.find_element(*self.google_search_button)
