import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.mark.ui
def test_check_incorrect_username():
    # Створення об'єкту для керування бразуером
    driver = webdriver.Chrome(
        service=Service(r'c:\_my doc\QA Global Logic\GIT\kozubenko-qa\chromedriver.exe')
        )

    # відкриваємо сторінку https://github.com/login 
    driver.get("https://github.com/login")

    # Закриваємо браузер
    driver.close()
