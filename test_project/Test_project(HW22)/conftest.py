import pytest
from selenium import webdriver
from configparser import ConfigParser


@pytest.fixture(autouse=True)
def printing_name_case():
    print('\nStarting new positive case...')
    yield
    print('Ending new positive case...')


def pytest_addoption(parser):
    parser.addoption('--browser.name', action='store', default=None,
                     help="Choose browser: chrome or safari")
    parser.addoption('--headmode', action='store', default='false',
                     help='Choose turn on or turn off headless mode')
    # parser.addoption('--language', action='store', default=None,
    #                  help='Choose language: ru, en...(etc)')


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser.name')
    headless = request.config.getoption('headmode')
    # opt = Options()
    # opt.add_argument("--disable-infobars")
    # opt.add_argument("start-maximized")
    # opt.add_argument("--disable-extensions")
    # opt.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
    print(f'Starting browser {browser_name.upper()}...')
    global browser
    # user_language = request.config.getoption('language')
    if browser_name == 'chrome':
        # здесь мы задаём в командной строке выбор на headless mode
        if headless == 'true':
            options = webdriver.ChromeOptions()
            # добавление опций браузера!!! important
            prefs = {"profile.default_content_setting_values.notifications": 2}
            options.add_experimental_option("prefs", prefs)
            # options.add_argument("--disable-notifications")
            options.add_argument(
                "user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36")
            options.headless = True
            browser = webdriver.Chrome('/Volumes/Work/TestProject/tools/chromedriver', options=options)
        else:
            # options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
            options = webdriver.ChromeOptions()
            prefs = {"profile.default_content_setting_values.notifications": 2}
            options.add_experimental_option("prefs", prefs)
            options.add_argument(
                "user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36")
            options.headless = False
            browser = webdriver.Chrome('/Volumes/Work/Python_courses/Project/AQA_Python_courses/test_project/Test_project(HW22)/tools/chromedriver', options=options)
            print('\n\nStart chrome browser for test...')
    elif browser_name == 'safari':
        if headless == 'true':
            # options = webdriver.Safari()
            # options.headless = True
            browser = webdriver.Safari()
        else:
            # fp = webdriver.FirefoxProfile(options=options)
            # fp.set_preference("intl.accept_languages", user_language)
            # browser = webdriver.Firefox(executable_path='/Users/maxkazliakouski/Downloads/geckodriver')
            browser = webdriver.Safari()
            print(f'Start {browser_name} browser for test...')
    else:
        print('Browser <browser_name> still not implemented')

    yield browser
    print(f'\nQuit browser {browser_name.upper()}...')
    # browser quit don't fit for safari, get the error about refuse connection
    browser.quit()


def parser(section, value):
    config = ConfigParser()
    config.read('/Volumes/Work/Python_courses/Project/AQA_Python_courses/test_project/Test_project(HW22)/data_for_test(HW22)/test_data_hw21.ini')
    value = config.get(section, value)
    return value
