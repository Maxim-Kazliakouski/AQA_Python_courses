from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pytest
import additional_func as add_func
from src.test.sources.SauceDemoLocators import locators


@pytest.mark.parametrize('number_items', locators.number_items)
def test_login_and_log_output(browser, logs, number_items):
    item_name_list = []
    creds = []
    password = []
    browser.get(locators.URL)
    waiting_time = WebDriverWait(browser, 5)
    # getting username list
    add_func.try_except_presence_of_element(browser, logs, locators.LOGIN_CREDS)
    browser.find_element(*locators.LOGIN_CREDS)
    credentials = browser.find_element(*locators.LOGIN_CREDS).text.split('\n')
    for each_credentials in credentials:
        if 'Accepted usernames are:' not in each_credentials \
                and 'locked_out_user' not in each_credentials:
            creds.append(each_credentials)
    # finding username field and send keys
    add_func.try_except_presence_of_element(browser, logs, locators.USERNAME_FIELD_ID)
    username_field = waiting_time.until(EC.presence_of_element_located(locators.USERNAME_FIELD_ID))
    # send random creds from the list
    # username_field.send_keys(creds[random.randrange(0, len(creds))])
    username_field.send_keys(creds[0])
    # username_field.send_keys('standard_user')   # for safari
    # getting password
    add_func.try_except_presence_of_element(browser, logs, locators.PASSWORDS)
    browser.find_element(*locators.PASSWORDS)
    password_for_login = browser.find_element(*locators.PASSWORDS).text.split('\n')
    for each_password in password_for_login:
        if 'Password for all users:' not in each_password:
            password.append(each_password)
    # finding password field and send keys
    add_func.try_except_presence_of_element(browser, logs, locators.PASSWORD_FIELD_NAME)
    password_field = waiting_time.until(EC.presence_of_element_located(locators.PASSWORD_FIELD_NAME))
    # send password from the list
    password_field.send_keys(password[0])
    # password_field.send_keys('secret_sauce')   # for safari
    # finding and clicking on Login button
    add_func.try_except_element_is_clickable(browser, logs, locators.LOGIN_BUTTON_CSS)
    login_button = waiting_time.until(EC.element_to_be_clickable(locators.LOGIN_BUTTON_CSS))
    # send password from the list
    login_button.click()
    # amount of items
    find_all_goods = browser.find_elements(*locators.ALL_GOODS)
    list_goods = []
    for i in find_all_goods:
        list_goods.append(len(i.text))

    def item_description_func(item_name):
        item_name_list.append(item_name)
        item_description = browser.find_element(By.XPATH,
                                                f'//*[@id="inventory_container"]/div/div[{number_items}]/div[2]/div[1]/div')
        item_price = browser.find_element(By.XPATH,
                                          f'//*[@id="inventory_container"]/div/div[{number_items}]/div[2]/div[2]/div')
        logs.info(f'\nThe info about {number_items} good: \nThe name -> {item_name_list[0]}'
                  f'\nThe description -> {item_description.text}'
                  f'\nThe price -> {item_price.text}')
        item_name_list.clear()

    # getting info about certain good(костыли, расскажу потом, почему так):
    if number_items == '1':
        item_name = browser.find_element(By.XPATH, f'//*[@id="item_4_title_link"]/div').text
        item_description_func(item_name)
    elif number_items == '2':
        item_name = browser.find_element(By.XPATH, f'//*[@id="item_0_title_link"]/div').text
        item_description_func(item_name)
    elif number_items == '3':
        item_name = browser.find_element(By.XPATH, f'//*[@id="item_1_title_link"]/div').text
        item_description_func(item_name)
    elif number_items == '4':
        item_name = browser.find_element(By.XPATH, f'//*[@id="item_5_title_link"]/div').text
        item_description_func(item_name)
    elif number_items == '5':
        item_name = browser.find_element(By.XPATH, f'//*[@id="item_2_title_link"]/div').text
        item_description_func(item_name)
    elif number_items == '6':
        item_name = browser.find_element(By.XPATH, f'//*[@id="item_3_title_link"]/div').text
        item_description_func(item_name)
