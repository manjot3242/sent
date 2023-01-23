#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def get_drvier():
  # Set options to make browsing easier
  options = webdriver.FirefoxOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
 # options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Firefox(options=options)
  driver.get("https://mytoolstown.com/smsbomber/")
  return driver

def sent():
    driver = get_drvier()
    driver.find_element(by= "id" ,value="mobno").send_keys("8872213990")
    driver.find_element(by="id", value="count").send_keys("1" + Keys.RETURN)
    #driver.find_element(by='id', value="startsms").click()
    #time.sleep(30)


sent()
