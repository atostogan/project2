'''
Contains functions for getting element reference
'''

from selenium.webdriver.common.by import By


class HomePage:
   def __init__(self, driver):
      self.driver = driver

   search_field = (By.CSS_SELECTOR, '[name = "q"]')
   google_search_button = (By.CSS_SELECTOR, '[name = "btnK"]')

   def get_search_field(self):
      '''
      Returns reference to the search_field
      '''
      return self.driver.find_element(*HomePage.search_field)

   def get_google_search_button(self):
      '''
      Returns reference to the google_search_button(
      '''
      return self.driver.find_element(*HomePage.google_search_button)




