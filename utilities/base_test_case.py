import unittest
from selenium import webdriver


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/Users/atostogan/chromedriver/chromedriver")
        self.driver.maximize_window()
        self.driver.get("https://www.google.com")

    def tearDown(self):
        self.driver.close()
