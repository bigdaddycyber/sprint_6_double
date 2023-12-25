import pytest
from selenium import webdriver
import random
import string



@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()