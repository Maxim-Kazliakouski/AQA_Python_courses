import pytest
from configparser import ConfigParser


@pytest.fixture(autouse=True)
def printing_name_case():
    print('\nStarting new positive case...')
    yield
    print('\nEnding new positive case...')


# parser from .ini file
def parser(section, value):
    config = ConfigParser()
    config.read('data_school_parse.ini')
    value = config.get(section, value)
    return value

