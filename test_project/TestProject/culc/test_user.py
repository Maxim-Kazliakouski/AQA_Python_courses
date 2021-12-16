import pytest


@pytest.fixture(scope='class')
def class_scope():
    print("setting fixture for tests")
    yield


@pytest.mark.usefixtures('class_scope')
class TestSomething:

    def test_1(self):
        print("test1")

    def test_2(self):
        print("test2")
