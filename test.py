from selenium import webdriver
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("http://localhost:3000/")
print(driver.title)


time.sleep(10)
driver.close()
