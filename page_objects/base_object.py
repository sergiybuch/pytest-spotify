import selenium.webdriver.support.ui as ui
from selenium.webdriver.support import expected_conditions as EC


class BaseObject:

    def __init__(self, driver):
        self.driver = driver

    def wait_element(self, element):
        wait = ui.WebDriverWait(self.driver, 10)
        wait.until(lambda driver: self.driver.find_element(element[0], element[1]))
        return element

    def wait_for_element_invisible(self, element):
        wait = ui.WebDriverWait(self.driver, 10)
        wait.until(EC.invisibility_of_element_located(element))
        return True

    def wait_for_presence_of_element(self, element, wait_time=15):
        wait = ui.WebDriverWait(self.driver, wait_time)
        wait.until(EC.presence_of_element_located(element))

    def wait_until_element_visible(self, element, wait_time=15):
        wait = ui.WebDriverWait(self.driver, wait_time)
        wait.until(EC.visibility_of_element_located(element))

    def wait_until_element_clickable(self, element):
        ui.WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(element))
        return element
