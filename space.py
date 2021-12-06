from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class HomePage:

    URL = 'http://127.0.0.1:3000/'

   # element search queries
    USER_NAME = (By.NAME, 'email')
    PASS = (By.NAME, 'password')
    LOGIN = (By.CLASS_NAME, 'button')

    def __init__(self, browser):
        self.browser = browser


# functions used in testing

    def load(self):
        self.browser.get(self.URL)

    def uploadFile(self, picture):
        uploadButton = self.browser.find_element(By.ID, "file")
        uploadButton.send_keys(picture)

        submitButton = self.browser.find_element(By.ID, "submit")
        submitButton.click()
        time.sleep(20)

    def solveEquation(self, picture):
        uploadButton = self.browser.find_element(By.ID, "file")
        uploadButton.send_keys(picture)

        submitButton = self.browser.find_element(By.ID, "submit")
        submitButton.click()

        time.sleep(10)
        solveButton = self.browser.find_element(By.ID, "solve")
        solveButton.click()
        time.sleep(10)

    def solveandVis(self, picture):
        uploadButton = self.browser.find_element(By.ID, "file")
        uploadButton.send_keys(picture)

        submitButton = self.browser.find_element(By.ID, "submit")
        submitButton.click()

        time.sleep(10)
        solveButton = self.browser.find_element(By.ID, "solve")
        solveButton.click()
        time.sleep(10)

        visButton = self.browser.find_element(By.ID, "vis")
        visButton.click()
        time.sleep(10)

    def visualize(self, picture):
        uploadButton = self.browser.find_element(By.ID, "file")
        uploadButton.send_keys(picture)

        submitButton = self.browser.find_element(By.ID, "submit")
        submitButton.click()

        time.sleep(10)
        solveButton = self.browser.find_element(By.ID, "graph")
        solveButton.click()
        time.sleep(10)

        homeButton = self.browser.find_element(By.ID, "home")
        homeButton.click()
        time.sleep(5)
