# SYSTEM IMPORT
import time
import sys
import os
from random import randint

# SELENIUM + REQUIRED EXCEPTIONS
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from slacker import Slacker

# WEBDRIVER OPTIONS
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(executable_path="/home/matt/TwitterBot/chromedriver", chrome_options=options)
wait = WebDriverWait(driver, 10)

# LOGIN WITH TWITTER
def login():
    driver.get("https://twitter.com/login")
    wait()
    username = driver.find_element_by_class_name("js-username-field")
    username.clear()
    username.send_keys('LandosBio')
    password = driver.find_element_by_class_name("js-password-field")
    password.clear()
    password.send_keys('newLandosTwitter2018')
    password.submit()


# UNFOLLOW LOOP
def unfollowbot():
	 driver.get("https://twitter.com/LandosBio/following")
        users = get_elements_by_class_name("js-actionable-user")
        for usr in users[1:60]:
        	    status = get_elements_by_class_name("FollowStatus")
        	    if status 
        		driver.execute_script("arguments[0].click();", btn)
        		wait()

# UNFOLLOW
login()
wait()
followloop()
driver.quit()
sys.exit()
