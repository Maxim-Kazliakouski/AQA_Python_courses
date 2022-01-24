import os

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import conftest
from locators_for_HW24 import locators_hw24_dynamic_controls as locator
import subprocess


class Test_for_dynamic_controls:
    def test_appearing_text_after_clicking_on_remove_button(self, printing_name_case, browser, logs):
        # finding text "it's gone"
        """
        This case checks appearing text after clicking on remove button
        """
        browser.get(locator.URL)
        remove_button = browser.find_element(*locator.REMOVE_BUTTON)
        remove_button.click()
        waiting_text_1 = browser.find_element(*locator.WAITING_TEXT_1)
        b = "It's gone!"
        assert waiting_text_1.text == b, f'{waiting_text_1} There is no text "It is gone"'

    def test_checkbox_disappearing(self, browser):
        # checking that checkbox absence at the page
        """This case checks that checkbox disappears at the page"""
        browser.get(locator.URL)
        checkbox_element = browser.find_element(*locator.CHECKBOX_ELEMENT)
        remove_button = browser.find_element(*locator.REMOVE_BUTTON)
        remove_button.click()
        browser.find_element(*locator.WAITING_TEXT_1)
        try:
            checkbox = WebDriverWait(browser, 5).until(EC.presence_of_element_located(locator.CHECKBOX_ELEMENT))
            assert False, 'The checkbox still available'
        except(TimeoutException):
            assert TimeoutException


    def test_for_disabled_input_field(self, browser):
        # finding input field
        """This case checks that input field is disabled"""
        browser.get(locator.URL)
        input_field = browser.find_element(*locator.INPUT_FIELD)
        # checking that input is disabled
        assert input_field.is_enabled() is False, 'The input field is clickable'

    def test_appearing_enabled_text(self, browser):
        # finding and clicking on the 'enable' button
        """This case checks that text appears after clicking on enable button"""
        browser.get(locator.URL)
        enable_button = browser.find_element(*locator.ENABLE_BUTTON)
        enable_button.click()
        # finding text "It's enabled!"
        waiting_text_2 = browser.find_element(*locator.WAITING_TEXT_2)
        # Checking that text is appeared
        assert waiting_text_2.text == "It's enabled!", 'There is no text "It is enabled!"'

    def test_enable_input_field(self, browser):
        # checking that input field is enabled
        """This case checks that input field is enabled"""
        browser.get(locator.URL)
        enable_button = browser.find_element(*locator.ENABLE_BUTTON)
        enable_button.click()
        browser.find_element(*locator.WAITING_TEXT_2)
        input_field = browser.find_element(*locator.INPUT_FIELD)
        assert input_field.is_enabled() is True, 'The input field is not clickable'

