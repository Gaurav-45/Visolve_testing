import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    b = webdriver.Chrome(PATH)
    b.implicitly_wait(10)
    yield b
    b.quit()
