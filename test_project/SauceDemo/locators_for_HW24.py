from selenium.webdriver.common.by import By
from test_sauce import *


class locators_hw24_dynamic_controls:
    URL = 'http://the-internet.herokuapp.com/dynamic_controls'
    CHECKBOX_ELEMENT = By.XPATH, '//*[@id="checkbox"]'
    WAITING_TEXT_1 = By.ID, 'message'
    REMOVE_BUTTON = By.XPATH, '//*[@id="checkbox-example"]/button'
    INPUT_FIELD = By.XPATH, '//*[@id="input-example"]/input'
    ENABLE_BUTTON = By.XPATH, '//*[@id="input-example"]/button'
    WAITING_TEXT_2 = By.ID, 'message'


class locators_hw_24_iframe:
    URL = 'http://the-internet.herokuapp.com/frames'
    IFRAME_LINK = By.XPATH, '//*[@id="content"]/div/ul/li[2]/a'
    FRAME = By.ID, 'mce_0_ifr'
    TEXT_IN_FRAME = By.XPATH, '//*[@id="tinymce"]/p'
