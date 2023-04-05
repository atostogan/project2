from utilities.base_test_case import BaseTestCase
from pages.home_page import HomePage
import time


class TestOpenHomePage(BaseTestCase):

    def test_OpenHomePage(self):
        '''
        Verifies if the HomePage opens
        '''
        assert self.driver.title == "Google"

    def test_GoogleSearch(self):
        '''
        Verifies if page with search results opens
        '''
        home_page = HomePage(self.driver)
        home_page.get_search_field().send_keys('apple')
        time.sleep(1)
        home_page.get_google_search_button().click()
        assert self.driver.title == "apple - Google Search"

