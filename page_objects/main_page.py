from selenium.webdriver.common.by import By
from page_objects.base_object import BaseObject


class MainPage(BaseObject):

    login_button = (By.XPATH, '//button[text()="Log in"]')
    dismiss_button = (By.XPATH, '//button[text()="Dismiss"]')
    launch_web_player_button = (By.ID, 'segmented-desktop-launch')
    user_profile_button = (By.CSS_SELECTOR, '[data-testid="user-widget-link"]')
    logout_button = (By.XPATH, '//button[text()="Log out"]')
    see_all_button = (By.XPATH, '//span[text()="See all"]')

    def click_login_button(self):
        self.wait_until_element_clickable(self.login_button)
        self.driver.find_element(*self.login_button).click()

    def click_launch_web_player_button(self):
        self.wait_until_element_clickable(self.launch_web_player_button)
        self.driver.find_element(*self.launch_web_player_button).click()

    def logout(self):
        self.wait_until_element_clickable(self.user_profile_button)
        self.driver.find_element(*self.user_profile_button).click()
        self.wait_until_element_clickable(self.logout_button)
        self.driver.find_element(*self.logout_button).click()
