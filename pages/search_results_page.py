'''
Contains functions for getting element reference
'''
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchResultsPage(BasePage):
    '''
    Class for storing SearchResultsPage elements
    '''

    result_stats = (By.ID, 'result-stats')

    def get_result_stats(self):
        '''
        Returns reference to the result_stats
        '''
        return self.driver.find_element(*self.result_stats)
