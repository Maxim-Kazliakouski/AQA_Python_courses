import os


def test_start_allure_report():
    print('\nGenerating allure report...')
    os.system('allure serve /Users/maxkazliakouski/.jenkins/workspace/test_jenkins/allure-results')
