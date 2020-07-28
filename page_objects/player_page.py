from selenium.webdriver.common.by import By
from page_objects.base_object import BaseObject


class Player(BaseObject):
    control_panel = (By.CSS_SELECTOR, '.player-controls')
    play_button = (By.CSS_SELECTOR, '[data-testid="control-button-play"]')
    pause_button = (By.CSS_SELECTOR, '[data-testid="control-button-pause"]')
    next_button = (By.CSS_SELECTOR, '[data-testid="control-button-skip-forward"]')
    previous_button = (By.CSS_SELECTOR, '[data-testid="control-button-skip-back"]')
    enable_repeat_button = (By.CSS_SELECTOR, '[data-testid="control-button-repeat"]')
    enable_repeat_one_button = (By.CSS_SELECTOR, '[data-testid="control-button-repeat-one"]')
    disable_repeat_button = (By.CSS_SELECTOR, '[data-testid="control-button-no-repeat"]')
    enable_shuffle_button = (By.CSS_SELECTOR, '[data-testid="control-button-shuffle"]')
    disable_shuffle_button = (By.CSS_SELECTOR, '[data-testid="control-button-disable-shuffle"]')
    progress_bar_1_sec = (By.XPATH, '//div[@as="div" and text()="0:01"]')
    progress_bar_3_sec = (By.XPATH, '//div[@as="div" and text()="0:03"]')
    progress_bar_0_sec = (By.XPATH, '//button[@aria-label="Change progress" and @style="left: 0%;"]')
    control_loading = (By.CSS_SELECTOR, '.control-button--loading')
    now_playing_song = (By.CSS_SELECTOR, '.now-playing')
    playback_bar = (By.CSS_SELECTOR, '.playback-bar')

    def click_play_button(self):
        self.wait_until_element_clickable(self.play_button)
        self.driver.find_element(*self.play_button).click()

    def click_pause_button(self):
        self.wait_until_element_clickable(self.pause_button)
        self.driver.find_element(*self.pause_button).click()

    def click_next_button(self):
        self.wait_until_element_visible(self.next_button)
        self.wait_until_element_clickable(self.next_button)
        self.driver.find_element(*self.next_button).click()

    def click_previous_button(self):
        self.wait_until_element_clickable(self.previous_button)
        self.driver.find_element(*self.previous_button).click()

    def click_enable_shuffle_button(self):
        self.wait_until_element_clickable(self.enable_shuffle_button)
        self.driver.find_element(*self.enable_shuffle_button).click()

    def click_disable_shuffle_button(self):
        self.wait_until_element_clickable(self.disable_shuffle_button)
        self.driver.find_element(*self.disable_shuffle_button).click()

    def click_enable_repeat_button(self):
        self.wait_until_element_clickable(self.enable_repeat_button)
        self.driver.find_element(*self.enable_repeat_button).click()

    def click_enable_repeat_one_button(self):
        self.wait_until_element_clickable(self.enable_repeat_one_button)
        self.driver.find_element(*self.enable_repeat_one_button).click()

    def click_disable_repeat_button(self):
        self.wait_until_element_clickable(self.disable_repeat_button)
        self.driver.find_element(*self.disable_repeat_button).click()
