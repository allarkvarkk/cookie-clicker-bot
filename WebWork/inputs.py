import time
import pyperclip as pc

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait

import shared


def click_address(address, retries=0, timeout=20):
    tries = 0
    while tries <= retries:
        try:
            button = WebDriverWait(shared.driver, timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, address))
            )
            button.click()
            return
        except Exception as e:
            if tries == retries:
                print("ERROR (click_element) ", address, ": ", e)
                tries += 1
def click_element(element):
    element.click()

def send_keys(address, text, timeout=20):
    pc.copy(text)
    try:
        text_box = WebDriverWait(shared.driver,timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, address))
        )
        text_box.send_keys(Keys.CONTROL, 'v')
    except Exception as e:
        print("ERROR (send_keys) ", address, ": ", e)

def scroll_into_view(address, timeout=10):
    try:
        button = WebDriverWait(shared.driver, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, address))
        )
        ActionChains(shared.driver).move_to_element(button).perform()
    except Exception as e:
        print("ERROR (scroll_into_view) with address ", address, ": ", e)

def auto_clicker(address, clicks_per_sec=25, retry_time=0.05, timeout=1):
    while True:
        try:
            button = WebDriverWait(shared.driver,timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, address))
            )
            while button.is_displayed():
                button.click()
                shared.clicks_per_second = clicks_per_sec
                time.sleep(1/clicks_per_sec)
            raise Exception("Can't click cookie")
        except Exception as e:
            time.sleep(retry_time)