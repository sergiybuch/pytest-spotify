# pytest-spotify
Automation test framework written in Python and using pytest and Selenium Webdriver-manager to test Spotify music player.

Prerequisits:
1. Spotify free account

Run Tests in Pycharm:
1. Download project and open in Pycharm
2. Go to Pycharm Preferences/Project interpreter and select Python3.x 
3. Install pytest and selenium packages in Pycharm
4. Add environment variables SP_USER with your profile email and SP_PASS with your spotify password into Run/Debug config
5. Add Run/Debug configuration to use pytest 
5. Install and run Webdriver manager https://www.npmjs.com/package/webdriver-manager
6. Navigate to tests/test_player.py and Run this file

Run tests in Terminal:
1. Install Python https://www.python.org/
2. Install pip https://pip.pypa.io/en/stable/installing/
3. Install selenium for Python https://pypi.org/project/selenium/ 
4. Install pytest https://docs.pytest.org/en/stable/
5. Install and run Webdriver manager https://www.npmjs.com/package/webdriver-manager
6. Download project and create environment variables SP_USER with your profile email and SP_PASS with your spotify password
7. Navigate to project and run *python3 -m pytest tests/test_player.py*
