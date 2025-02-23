from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

def create_web_driver(WAIT_SECONDS=60):
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, WAIT_SECONDS)
    return driver, wait