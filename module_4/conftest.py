import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en",
                     help="Choose language: for example: fr, ru etc.")

@pytest.fixture()
def language(request):    
    language = request.config.getoption("language")
    if language == None:
        raise pytest.UsageError("--language should be passed")
    return language



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
