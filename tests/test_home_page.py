'''
Checks functionality of HomePage
'''
from utilities.base_test_case import BaseTestCase
from pages.home_page import HomePage


class TestOpenHomePage(BaseTestCase):
    '''
    Class for HomePage tests
    '''

    def test_open_home_page(self):
        '''
        Verifies if the HomePage opens
        '''
        driver = self.driver
        home_page_title = "Google"
        self.assertEqual(driver.title, home_page_title, "HomePage Failed to load")

    def test_google_search(self):
        '''
        Verifies if page with search results opens
        '''
        driver = self.driver
        home_page = HomePage(driver)

        home_page.get_search_field().send_keys('apple')
        driver.implicitly_wait(1)

        home_page.get_google_search_button().click()
        search_results_page_title = "apple - Google Search"
        self.assertEqual(driver.title, search_results_page_title, "SearchResultsPage Failed to load")
