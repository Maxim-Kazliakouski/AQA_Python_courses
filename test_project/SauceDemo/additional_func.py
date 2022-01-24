import traceback
from selenium.common.exceptions import TimeoutException, NoSuchElementException, InvalidSelectorException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def try_except_element_is_clickable(browser, logs, locator_for_click):
    waiting_time = WebDriverWait(browser, 5)
    try:
        waiting_time.until(EC.element_to_be_clickable(locator_for_click))
    except(TimeoutException, NoSuchElementException, InvalidSelectorException):
        logs.error(traceback.format_exc())
        logs.exception('ERROR ! THE AWAITING TIME IS END')
        raise TimeoutException(f'The time is end, there is no such element with following {" ".join(locator_for_click)} ...')


def try_except_presence_of_element(browser, logs, locator):
    waiting_time = WebDriverWait(browser, 5)
    try:
        waiting_time.until(EC.presence_of_element_located(locator))
    except(TimeoutException, NoSuchElementException, InvalidSelectorException):
        logs.error(traceback.format_exc())
        logs.exception('ERROR ! THE AWAITING TIME IS END')
        raise TimeoutException(f'The time is end, there is no such element with following {" ".join(locator)} ...')
