from selenium.webdriver.common.by import By
from page_objects.base_object import BaseObject


class LoginPage(BaseObject):

    username_input = (By.ID, 'login-username')
    password_input = (By.ID, 'login-password')
    login_button = (By.ID, 'login-button')

    def login(self, username, password):
        self.driver.find_element(*self.username_input).clear()
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).clear()
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
