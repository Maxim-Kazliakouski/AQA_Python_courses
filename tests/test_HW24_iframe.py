from locators_for_HW24 import locators_hw_24_iframe as locator


class Test_suit_iframe:
    def test_iframe(self, browser, printing_name_case):
        browser.implicitly_wait(3)
        browser.get(locator.URL)
        browser.maximize_window()
        iframe_link = browser.find_element(*locator.IFRAME_LINK)
        iframe_link.click()
        browser.switch_to.frame(browser.find_element(*locator.FRAME))
        text_in_frame = browser.find_element(*locator.TEXT_IN_FRAME)
        assert text_in_frame.text == 'Your content goes here.', 'There is no such text'
