# SYSTEM IMPORT
import time
import sys
import os
import random as rand 

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


# WEBDRIVER OPTIONS
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(executable_path="/home/matt/TwitterBot/chromedriver", chrome_options=options)
#wait = WebDriverWait(driver, 10)

def randpharm():
	pharmas = ["pfizer", "abbvie", "sanofi", "JNJCares", "Celgene", "Roche"]
	return random.choice(pharmas)

# WAIT FUNCTION
def wait():
	time.sleep(rand.randint(3,60))

# LOGIN WITH TWITTER
def login():
    driver.get("https://twitter.com/login")
    #wait()
    username = driver.find_element_by_class_name("js-username-field")
    username.clear()
    username.send_keys('LandosBio')
    password = driver.find_element_by_class_name("js-password-field")
    password.clear()
    password.send_keys('newLandosTwitter2018')
    password.submit()

# FOLLOW BOT
def followbot():
        driver.get("https://twitter.com/" + randpharm() + "followers")
        buttons = get_elements_by_class_name(follow-text)
        for btn in buttons[1:50]:
        		driver.execute_script("arguments[0].click();", btn)
        		wait()
    



# ACTIVITY
login()
wait()
followbot()
driver.quit()
sys.exit()

    


