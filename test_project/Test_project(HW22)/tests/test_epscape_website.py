from imports import all_imports as lib


def test_epscape_website(browser):
    browser.get(lib.parser('data for escape website', 'URL'))
    waiting_time = lib.WebDriverWait(browser, 5)
    # finding login button
    try:
        waiting_time.until(lib.EC.element_to_be_clickable(lib.Locators.LOGIN_BUTTON))
    except(lib.TimeoutException, lib.NoSuchElementException):
        raise lib.TimeoutException('The time is end, there is no such element')
    login_button = waiting_time.until(lib.EC.presence_of_element_located(lib.Locators.LOGIN_BUTTON))
    login_button.click()
    # finding email field
    try:
        waiting_time.until(lib.EC.element_to_be_clickable(
            lib.Locators.EMAIL_FIELD))
    except(lib.TimeoutException, lib.NoSuchElementException):
        raise lib.TimeoutException('The time is end, there is no such field like email...')
    email_field = waiting_time.until(lib.EC.presence_of_element_located(lib.Locators.EMAIL_FIELD))
    email_field.send_keys('maxim.kazliakouski@gmail.com')
    # finding password field
    try:
        waiting_time.until(lib.EC.element_to_be_clickable(lib.Locators.PASSWORD_FIELD))
    except(lib.TimeoutException, lib.NoSuchElementException):
        raise lib.TimeoutException('The time is end, there is no such field like email...')
    password_field = waiting_time.until(lib.EC.presence_of_element_located(lib.Locators.PASSWORD_FIELD))
    password_field.send_keys('sejmeb-Taqfuv-jykwi4')
    # finding Войти button
    try:
        waiting_time.until(lib.EC.element_to_be_clickable(lib.Locators.ENTER_BUTTON))
    except(lib.TimeoutException, lib.NoSuchElementException):
        raise lib.TimeoutException('The time is end, there is no such button "Войти"...')
    enter_button = waiting_time.until(
        lib.EC.presence_of_element_located(lib.Locators.ENTER_BUTTON))
    enter_button.click()
    # finding login info
    try:
        waiting_time.until(lib.EC.element_to_be_clickable(lib.Locators.LOGIN_INFO_FINDING))
    except(lib.TimeoutException, lib.NoSuchElementException):
        raise lib.TimeoutException('The time is end, there is no such button with login info...')
    button_info = waiting_time.until(lib.EC.presence_of_element_located(lib.Locators.LOGIN_INFO_TEXT)).text
    assert button_info == lib.parser('data for escape website', 'LOGIN'), 'Error, unsuccessfully login'
