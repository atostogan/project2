'''
Checks functionality of SearchResultsPage
'''
import logging
from selenium.common.exceptions import TimeoutException
from utilities.base_test_case import BaseTestCase
import utilities.add_logging as log
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage


class TestSearchResultsPage(BaseTestCase):
    '''
        Class for SearchResultsPage tests
    '''
    logger = log.create_logger('test_search_results_page')

    def test_open_search_results_page(self):
        '''
        Verifies if page with search results opens
        '''
        self.logger.info('Waiting for search_field to load')
        self.home_page.wait_for_element_to_load(HomePage.search_field)
        self.logger.info('Fill in the search field')
        self.home_page.get_search_field().send_keys('apple')

        self.logger.info('Waiting for google_search_button to load')
        self.home_page.wait_for_element_to_load(HomePage.google_search_button)
        self.logger.info('Click on Google Search button')
        self.home_page.get_google_search_button().click()

        self.logger.info('Waiting for SearchResultsPage to load')
        try:
            self.home_page.wait_for_element_to_load(SearchResultsPage.result_stats)
            self.logger.info('SearchResultsPage is loaded successfully')
        except TimeoutException as error:
            self.logger.error('SearchResultsPage Failed to load')
            self.fail(f'SearchResultsPage Failed to load: {error}')
