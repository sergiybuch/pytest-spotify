import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from page_objects.base_object import BaseObject
from page_objects.login_page import LoginPage
from page_objects.player_page import Player
from page_objects.main_page import MainPage

BROWSERS = ['chrome']

desired_capabilities = {
    'chrome': DesiredCapabilities.CHROME,
    'firefox': DesiredCapabilities.FIREFOX
}


@pytest.fixture(scope='session', params=BROWSERS)
def driver(request):
    """
    Returns a webdriver object to Selenium Grid
    """
    browser = request.param.lower()
    capabilities = desired_capabilities[browser]
    capabilities['testFileNameTemplate'] = "{testName}_{timestamp}_{browser}_{testStatus}"
    capabilities['resolution'] = '1920x1080'
    capabilities['browserstack.geoLocation'] = 'CA'
    capabilities['browserstack.timezone'] = 'MONTREAL'
    webdriver.Remote.accept_next_alert = True
    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=capabilities)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture()
def login_logout(driver, login_page, main_page):
    username = os.environ['SP_USER']
    password = os.environ['SP_PASS']
    driver.get('https://open.spotify.com/')
    main_page.click_login_button()
    login_page.login(username=username, password=password)
    yield
    main_page.logout()
    driver.delete_all_cookies()
    driver.execute_script('localStorage.clear();')


@pytest.fixture(scope='session')
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture(scope='session')
def main_page(driver):
    return MainPage(driver)


@pytest.fixture(scope='session')
def player(driver):
    return Player(driver)


@pytest.fixture(scope='session')
def action(driver):
    return BaseObject(driver)
