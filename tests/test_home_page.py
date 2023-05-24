'''
Checks functionality of HomePage
'''
import logging
from selenium.common.exceptions import TimeoutException
from utilities.base_test_case import BaseTestCase
from utilities.add_logging import create_logger
from pages.home_page import HomePage


class TestHomePage(BaseTestCase):
    '''
    Class for HomePage tests
    '''
    logger = create_logger('test_home_page')

    def test_open_home_page(self):
        '''
        Verifies if the HomePage opens
        '''
        self.logger.info('Waiting for HomePage to load')

        try:
            self.home_page.wait_for_element_to_load(HomePage.search_field)
            self.logger.info('HomePage is loaded successfully')
        except TimeoutException as error:
            self.logger.error('Home Page Failed to load')
            self.fail(f'Home Page Failed to load: {error}')

    def test_open_gmail_link(self):
        '''
        Verifies if Gmail login page opens
        '''
        self.logger.info('Waiting for gmail_link element to load')
        self.home_page.wait_for_element_to_load(HomePage.gmail_link)
        self.logger.info('Click on Gmail link')
        self.home_page.get_gmail_link().click()

        self.logger.info('Waiting for Gmail login page to load')

        try:
            self.home_page.wait_for_element_to_load(HomePage.create_an_account_button)
            self.logger.info('Gmail login page is loaded successfully')
        except TimeoutException as error:
            self.logger.error('Gmail login page failed to load')
            self.fail(f'Gmail login page failed to load: {error}')
