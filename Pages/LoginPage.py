from Config.config import TestData
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):


    """By locators - OR"""
    EMAIL = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Continue')]")
    COOKIES = (By.ID, "rcc-confirm-button")
    


    """Constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
    
    """Page Actions"""
    
    """this is used to login to the web app"""    
    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.COOKIES)
        self.do_click(self.LOGIN_BUTTON)
    



