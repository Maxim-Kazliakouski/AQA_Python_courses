from imports import all_imports as lib


class Locators:
    LOGIN_BUTTON = (lib.By.CLASS_NAME, 'btn.btn--primary.btn--icon.background-primary.shadow-primary')
    EMAIL_FIELD = (lib.By.CLASS_NAME, 'el-input__inner')
    PASSWORD_FIELD = (lib.By.XPATH, '//*[@id="__layout"]/div/div[2]/div/div/div[2]/div/div/div[3]/form/div[2]/div/div/input')
    ENTER_BUTTON = (lib.By.CLASS_NAME, 'el-button.el-button--primary')
    LOGIN_INFO_FINDING = (lib.By.CLASS_NAME, 'btn.btn--brand.btn--icon.background-primary.shadow-primary')
    LOGIN_INFO_TEXT = (lib.By.CLASS_NAME, 'btn__text')