'''
Checks functionality of HomePage
'''
import pytest
from selenium.common.exceptions import TimeoutException
from utilities.base_test_case import BaseTestCase
from utilities.add_logging import create_logger
from pages.home_page import HomePage


class TestHomePage(BaseTestCase):
    '''
    Class for HomePage tests
    '''
    logger = create_logger('test_home_page')

    def test_open_home_page(self, set_up):
        '''
        Verifies if the HomePage opens
        '''
        self.logger.info('Waiting for HomePage to load')
        try:
            set_up.wait_for_element_to_load(HomePage.search_field)
            self.logger.info('HomePage is loaded successfully')
        except TimeoutException as error:
            self.logger.error('Home Page Failed to load')
            pytest.fail(f'Home Page Failed to load: {error}')

    def test_open_gmail_link(self, set_up):
        '''
        Verifies if Gmail login page opens
        '''
        self.logger.info('Waiting for gmail_link element to load')
        set_up.wait_for_element_to_load(HomePage.gmail_link)
        self.logger.info('Click on Gmail link')
        set_up.get_gmail_link().click()

        self.logger.info('Waiting for Gmail login page to load')

        try:
            set_up.wait_for_element_to_load(HomePage.create_an_account_button)
            self.logger.info('Gmail login page is loaded successfully')
        except TimeoutException as error:
            self.logger.error('Gmail login page failed to load')
            pytest.fail(f'Gmail login page failed to load: {error}')
