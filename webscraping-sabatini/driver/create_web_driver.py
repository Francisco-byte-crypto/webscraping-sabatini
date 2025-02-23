from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import  WebDriverException

def create_web_driver(WAIT_SECONDS=60):
    try:
        driver = webdriver.Firefox()
        wait = WebDriverWait(driver, WAIT_SECONDS)
        return driver, wait
    
    except WebDriverException:
        print("Error while creating webdriver.")