import pickle
import time
import logging

import pytest
from selenium.webdriver.common.by import By

import conftest


@pytest.fixture(scope='function')
def get_cookies(browser):
    dump_cookie = pickle.dump(browser.get_cookies(), open('session', 'wb'))
    return dump_cookie


# def test_google_search_page(browser, logs):
#     # browser = self.browser
#     browser.get("http://www.cdot.in")
#     browser.maximize_window()
#     window_before = browser.window_handles[0]
#     logs.info(window_before)
#     browser.find_element_by_xpath('//*[@id="covid-modal"]/div/div/div/div/div[1]/div/div[1]/div/div/a/img').click()
#     window_after = browser.window_handles[1]
#     browser.switch_to.window(window_after)
#     logs.info(window_after)
#     browser.find_element_by_xpath("/html/body/div[1]/div[9]/div[2]/div[2]/p/a").click()
#     info_from_button = browser.find_element_by_xpath("/html/body/div[1]/div[9]/div[2]/div[2]/p/a").text
#     time.sleep(2)
#     browser.switch_to.window(window_before)
#     logs.info(info_from_button)

def test_facebook_with_cookie(browser, get_cookies):
    browser.implicitly_wait(5)
    browser.get('https://www.facebook.com')
    browser.maximize_window()
    email = browser.find_element_by_xpath('//*[@id="email"]')
    email.send_keys('kma1991@rambler.ru')
    password = browser.find_element_by_xpath('//*[@id="pass"]')
    password.send_keys('maksimka91')
    button_login = browser.find_element(By.NAME, 'login')
    button_login.click()
    # get_cookies(browser)
    # dump_cookie = pickle.dump(browser.get_cookies(), open('session', 'wb'))
    # user_name = browser.find_element(By.LINK_TEXT, 'Max Kazliakouski')
    user_name = browser.find_element(By.LINK_TEXT, 'Max Kazliakouski')
    user_name.click()
    # time.sleep(5)
    user = browser.find_element(By.XPATH, "//h1[contains(text(),'Max Kazliakouski')]")
    assert user.text == 'Max Kazliakouski', 'You are not log in'
    browser.delete_all_cookies()
    # time.sleep(2)

# def test_login_with_cooke(browser):
#     browser.get('https://www.facebook.com')
#     browser.maximize_window()
#     for cookie in pickle.load(open('session', 'rb')):
#         browser.add_cookie(cookie)
#     browser.refresh()
#     user_icon = browser.find_element(By.CLASS_NAME, 'uiContextualLayerParent._csi')
#     user_icon.click()
#     password2 = browser.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div/div/div/form/div[2]/div/input')
#     password2.send_keys('maksimka91')
#     button_login = browser.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div/div/div/form/div[4]/button')
#     button_login.click()
#     user_name = browser.find_element(By.CLASS_NAME, 'a8c37x1j.ni8dbmo4.stjgntxs.l9j0dhe7.ltmttdrg.g0qnabr5')
#     user_name.click()
#     time.sleep(5)
#     user = browser.find_element(By.XPATH, "//h1[contains(text(),'Max Kazliakouski')]")
#     assert user.text == 'Max Kazliakouski', 'You are not log in'
#     # time.sleep(5)
