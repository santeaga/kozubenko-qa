from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class BasePage:
    PATH = r"c:\\_my doc\\QA Global Logic\\GIT\\kozubenko-qa\\"
    DRIVER_NAME = "chromedriver.exe"

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(
            service=Service(BasePage.PATH + BasePage.DRIVER_NAME)
            )

    def close(self):
        self.driver.close()
