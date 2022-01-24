from selenium.webdriver.common.by import By
from test_sauce import *


class locators:
    URL = 'https://www.saucedemo.com/'
    # LOCATORS FOR LOGIN PAGE(non-functional)
    LOGIN_CREDS = By.CSS_SELECTOR, '#login_credentials'
    PASSWORDS = By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[2]'

    # locators for username field
    USERNAME_FIELD_XPATH = By.XPATH, '//*[@id="user-name"]'
    USERNAME_FIELD_NAME = By.NAME, 'user-name'
    USERNAME_FIELD_ID = By.ID, 'user-name'
    USERNAME_FIELD_CLASS = By.CLASS_NAME, 'input_error.form_input'
    USERNAME_FIELD_CSS = By.CSS_SELECTOR, '#user-name'

    # locators for password name
    PASSWORD_FIELD_XPATH = By.XPATH, '//*[@id="password"]'
    PASSWORD_FIELD_NAME = By.NAME, 'password'
    PASSWORD_FIELD_ID = By.ID, 'password'
    # PASSWORD_FIELD_CLASS = By.CLASS_NAME, 'input_error.form_input'
    PASSWORD_FIELD_CSS = By.CSS_SELECTOR, '#password'

    # locators for login button
    LOGIN_BUTTON_XPATH = By.XPATH, '//*[@id="login-button"]'
    LOGIN_BUTTON_NAME = By.NAME, 'login-button'
    LOGIN_BUTTON_ID = By.ID, 'login-button'
    LOGIN_BUTTON_CLASS = By.CLASS_NAME, 'submit-button.btn_action'
    LOGIN_BUTTON_CSS = By.CSS_SELECTOR, '#login-button'

    # LOCATORS FOR ITEMS PAGE

    # locators for page with goods:

    ALL_GOODS = By.XPATH, '//*[@class="inventory_item"]'
    number_items = ['1', '2', '3', '4', '5', '6']
    ITEM_NAME = By.XPATH, f'//*[@id="item_{number_items}_title_link"]/div'
    ITEM_DESCRIPTION = By.XPATH, f'//*[@id="inventory_container"]/div/div[{number_items}]/div[2]/div[1]/div'
    ITEM_PRICE = By.XPATH, f'//*[@id="inventory_container"]/div/div[{number_items}]/div[2]/div[2]/div'
    ADD_TO_CART_BUTTON = By.ID, '#add-to-cart-sauce-labs-backpack'
    REMOVE_FROM_CART_BUTTON = By.XPATH, '//*[@id="remove-sauce-labs-backpack"]'  # variable can be added for all items
    ITEM_IMAGE = By.XPATH, f'//*[@id="item_{number_items}_img_link"]/img'
    TWITTER_ICON = By.XPATH, 'Twitter'
    FACEBOOK_ICON = By.LINK_TEXT, 'Facebook'
    LINKEDIN_ICON = By.XPATH, 'LinkedIn'
    SORTING_BUTTON = By.CLASS_NAME, 'product_sort_container'
    SHOPPING_CART = By.CLASS_NAME, 'shopping_cart_link'
    BURGER_MENU_BUTTON = By.ID, 'react-burger-menu-btn'
    # locators for sub-elements of dropdown burger menu
    ALL_ITEMS_BUTTON = By.ID, 'inventory_sidebar_link'
    ABOUT_BUTTON = By.ID, 'about_sidebar_link'
    LOGOUT_BUTTON = By.ID, 'logout_sidebar_link'
    RESET_APP_STATE_BUTTON = By.ID, 'reset_sidebar_link'
    SHOPPING_CART_BADGE = By.XPATH, '//*[@id="shopping_cart_container"]/a/span'   # non-functional element

    # locators on the item page
    BACK_TO_PRODUCTS_BUTTON = By.XPATH, '//*[@id="back-to-products"]'

    # cart page
    CONTINUE_SHOPPING_BUTTON = By.XPATH, '//*[@id="continue-shopping"]'
    CHECKOUT_BUTTON = By.XPATH, '//*[@id="checkout"]'

    # checkout your confirmation page
    FIRST_NAME_FIELD = By.XPATH, 'document.querySelector("#first-name")'
    LAST_NAME_FIELD = By.XPATH, '//*[@id="last-name"]'
    ZIP_FIELD = By.XPATH, '//*[@id="postal-code"]'
    CANCEL_BUTTON = By.XPATH, '//button[@id="cancel"]'
    CONTINUE_BUTTON = By.XPATH, '//*[@id="continue"]'
    FINISH_BUTTON = By.XPATH, '//*[@id="finish"]'
    BACK_HOME_BUTTON = By.XPATH, '//*[@id="back-to-products"]'
