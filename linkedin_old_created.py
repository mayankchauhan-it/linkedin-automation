from selenium.webdriver.common.keys import Keys
# from unittest import enterModuleContext
from argparse import Action
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import os
import credentials

sys.path.insert(0, os.path.dirname(__file__).replace('parsing-new-script', 'global-files/'))
# from GlobalVariable import *
from GlobalFunctions import *

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
# options.add_argument("headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
# options.add_argument('window-size=800x600')

path = GlobalVariable.ChromeDriverPath


def getting_url(search_name):
    base_url = "https://www.linkedin.com/search/results/people/?keywords={}"
    search_name = search_name.replace(' ', '%20')
    new_url = base_url.format(search_name)
    new_url += "&page={}"
    return new_url


def find(search_name):
    driver = webdriver.Chrome(chrome_options=options, executable_path=path)
    url = getting_url(search_name)
    driver.get(url)
    time.sleep(5)

    f = driver.find_element(By.XPATH, "/html/body/div[1]/main/p[1]/a")
    f.click()
    time.sleep(2)

    email_field = driver.find_element(By.ID, "username")
    email_field.send_keys(credentials.email)
    # time.sleep(2)


    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(credentials.password)
    time.sleep(3)

    submit_button = driver.find_element(By.CLASS_NAME, "login__form_action_container ")
    submit_button.click()
    time.sleep(20)

    f= driver.find_element(By.CLASS_NAME, "search-global-typeahead__input")
    f.send_keys(search_name)
    f.send_keys(Keys.ENTER)
    time.sleep(3)

    for page in range(1,20):
        driver.get(url.format(page))
        button = driver.find_elements(By.TAG_NAME, "button")


        for i in button:

            if i.text == "Connect":
                btn = i
                btn.click()

                c = driver.find_element(By.XPATH, "//button[@aria-label='Send now']")
                c.click()
                time.sleep(4)
            else:
                pass

find("HR Executive")


