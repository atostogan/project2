'''
Checks functionality of HomePage
'''
from utilities.base_test_case import BaseTestCase
from pages.home_page import HomePage


class TestHomePage(BaseTestCase):
    '''
    Class for HomePage tests
    '''

    def test_open_home_page(self):
        '''
        Verifies if the HomePage opens
        '''
        home_page_title = "Google"
        self.assertEqual(self.driver.title, home_page_title, "HomePage Failed to load")

    def test_open_gmail_link(self):
        '''
        Verifies if Gmail login page opens
        '''
        home_page = HomePage(self.driver)
        home_page.wait_for_element_to_load(HomePage.gmail_link)
        home_page.get_gmail_link().click()

        gmail_page_title = "Gmail: Private and secure email at no cost | Google Workspace"
        self.assertEqual(self.driver.title, gmail_page_title, "Gmail link failed to load")

    def test_google_search(self):
        '''
        Verifies if page with search results opens
        '''
        home_page = HomePage(self.driver)

        home_page.wait_for_element_to_load(HomePage.search_field)
        home_page.get_search_field().send_keys('apple')

        home_page.wait_for_element_to_load(HomePage.google_search_button)
        home_page.get_google_search_button().click()
        search_results_page_title = "apple - Google Search"

        self.assertEqual(self.driver.title, search_results_page_title, "SearchResultsPage Failed to load")
