from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""This class is the parent of all pages"""
"""It contains all generic methods and utilities for all the pages"""

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(by_locator))
        for element in elements:
            element.click()
    
    def do_send_keys(self, by_locator, text):
        elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(by_locator))
        for element in elements:
            element.send_keys(text)
    
    
    