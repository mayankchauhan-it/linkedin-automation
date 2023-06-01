import credentials

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import sys
import os
from datetime import date, time
from re import *
import time




sys.path.insert(0, os.path.dirname(__file__).replace('parsing-files', 'global-files/'))

optionss = webdriver.ChromeOptions()
optionss.add_argument('--ignore-certificate-errors')
optionss.add_argument('--ignore-ssl-errors')
# optionss.add_argument("--headless")
optionss.add_argument("--no-sandbox")
optionss.add_argument("--disable-dev-shm-usage")
optionss.add_argument('window-size=800x600')
optionss.add_experimental_option("useAutomationExtension", False)
optionss.add_experimental_option("excludeSwitches",["enable-automation"])


def getting_url(search_name):
    base_url = "https://www.linkedin.com/search/results/people/?keywords={}"
    search_name = search_name.replace(' ', '%20')
    new_url = base_url.format(search_name)
    new_url += "&page={}"
    return new_url


def find(search_name):
    driver = webdriver.Chrome( ChromeDriverManager().install() ,options=optionss)
    url = getting_url(search_name)
    driver.get(url)
    time.sleep(5)

    f = driver.find_element(By.XPATH, "/html/body/div[1]/main/div/p/a")
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
    time.sleep(10)


    for page in range(1,3):
        driver.get(url.format(page))
        button = driver.find_elements(By.TAG_NAME, "button")


        for i in button:

            if i.text == "Connect":
                # btn = i
                i.click()

                c = driver.find_element(By.XPATH, "//button[@aria-label='Send now']")
                message_button = driver.find_element(By.XPATH, "//button[@aria-label='Add a note']")
                message_button.click()
                time.sleep(3)
                m_box = driver.find_element(By.XPATH, "//*[@id='custom-message']")
                m_box.send_keys(credentials.message)
                time.sleep(2)
                c.click()

                time.sleep(2)
            else:
                pass

find("Graphic Desinger")
