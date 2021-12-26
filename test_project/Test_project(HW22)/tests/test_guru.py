from imports import all_imports as lib


def test_login_guru_firstname_lastname(browser):
    browser.get(lib.parser('data for case', 'URL'))
    browser.maximize_window()
    firstname_field = browser.find_element(lib.By.NAME, 'firstName')
    firstname_field.send_keys(lib.parser('data for case', 'FIRSTNAME'))
    lastname_field = browser.find_element(lib.By.NAME, 'lastName')
    lastname_field.send_keys(lib.parser('data for case', 'LASTNAME'))
    phone_field = browser.find_element(lib.By.NAME, 'phone')
    phone_field.send_keys(lib.parser('data for case', 'PHONE_NUMBER'))
    email_field = browser.find_element(lib.By.NAME, 'userName')
    email_field.send_keys(lib.parser('data for case', 'EMAIL'))
    address_field = browser.find_element(lib.By.NAME, 'address1')
    address_field.send_keys(lib.parser('data for case', 'ADDRESS'))
    city_field = browser.find_element(lib.By.NAME, 'city')
    city_field.send_keys(lib.parser('data for case', 'CITY'))
    state_field = browser.find_element(lib.By.NAME, 'state')
    state_field.send_keys(lib.parser('data for case', 'STATE'))
    postal_code_field = browser.find_element(lib.By.NAME, 'postalCode')
    postal_code_field.send_keys(lib.parser('data for case', 'POSTAL_CODE'))
    country_dropdown = lib.Select(browser.find_element(lib.By.NAME, 'country'))
    country_dropdown.select_by_value('RUSSIA')
    username_field = browser.find_element(lib.By.NAME, 'email')
    username_field.send_keys(lib.parser('data for case', 'USER_NAME'))
    password_field = browser.find_element(lib.By.NAME, 'password')
    password_field.send_keys(lib.parser('data for case', 'PASSWORD'))
    confirm_password_field = browser.find_element(lib.By.NAME, 'confirmPassword')
    confirm_password_field.send_keys(lib.parser('data for case', 'PASSWORD'))
    send_button = browser.find_element(lib.By.NAME, 'submit')
    send_button.click()
    firstname_lastname = browser.find_element(lib.By.XPATH, "//tbody/tr[3]/td[1]/p[1]/font[1]/b").text
    assert firstname_lastname == f'Dear {lib.parser("data for case", "FIRSTNAME")}' \
                                 f' {lib.parser("data for case", "LASTNAME")},',\
        'There is no user with such firstname and lastname'


def test_login_guru_username(browser):
    browser.get(lib.parser('data for case', 'URL'))
    browser.maximize_window()
    firstname_field = browser.find_element(lib.By.NAME, 'firstName')
    firstname_field.send_keys(lib.parser('data for case', 'FIRSTNAME'))
    lastname_field = browser.find_element(lib.By.NAME, 'lastName')
    lastname_field.send_keys(lib.parser('data for case', 'LASTNAME'))
    phone_field = browser.find_element(lib.By.NAME, 'phone')
    phone_field.send_keys(lib.parser('data for case', 'PHONE_NUMBER'))
    email_field = browser.find_element(lib.By.NAME, 'userName')
    email_field.send_keys(lib.parser('data for case', 'EMAIL'))
    address_field = browser.find_element(lib.By.NAME, 'address1')
    address_field.send_keys(lib.parser('data for case', 'ADDRESS'))
    city_field = browser.find_element(lib.By.NAME, 'city')
    city_field.send_keys(lib.parser('data for case', 'CITY'))
    state_field = browser.find_element(lib.By.NAME, 'state')
    state_field.send_keys(lib.parser('data for case', 'STATE'))
    postal_code_field = browser.find_element(lib.By.NAME, 'postalCode')
    postal_code_field.send_keys(lib.parser('data for case', 'POSTAL_CODE'))
    country_dropdown = lib.Select(browser.find_element(lib.By.NAME, 'country'))
    country_dropdown.select_by_value('RUSSIA')
    username_field = browser.find_element(lib.By.NAME, 'email')
    username_field.send_keys(lib.parser('data for case', 'USER_NAME'))
    password_field = browser.find_element(lib.By.NAME, 'password')
    password_field.send_keys(lib.parser('data for case', 'PASSWORD'))
    confirm_password_field = browser.find_element(lib.By.NAME, 'confirmPassword')
    confirm_password_field.send_keys(lib.parser('data for case', 'PASSWORD'))
    send_button = browser.find_element(lib.By.NAME, 'submit')
    send_button.click()
    username_confirm = browser.find_element(lib.By.XPATH, "//tbody/tr[3]/td[1]/p[3]/font[1]/b").text
    assert username_confirm == f'Note: Your user name is {lib.parser("data for case", "USER_NAME")}.',\
        'There is no user with such username'
