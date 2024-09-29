import time
import pyperclip as pc

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait

import shared


def click_address(address, retries=0, timeout=20) -> None:
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

def click_script(address) -> None:
    shared.driver(f"document.querySelector('{address}').click();")

def send_keys(address, text, timeout=20) -> None:
    pc.copy(text)
    try:
        text_box = WebDriverWait(shared.driver,timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, address))
        )
        text_box.send_keys(Keys.CONTROL, 'v')
    except Exception as e:
        print("ERROR (send_keys) ", address, ": ", e)

def scroll_into_view(address, timeout=10) -> None:
    try:
        button = WebDriverWait(shared.driver, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, address))
        )
        ActionChains(shared.driver).move_to_element(button).perform()
    except Exception as e:
        print("ERROR (scroll_into_view) with address ", address, ": ", e)

def auto_clicker(clicks_per_sec=25) -> None:
    shared.clicks_per_second = clicks_per_sec
    while True:
        shared.driver.execute_script(f"Game.ClickCookie();")
        time.sleep(1/clicks_per_sec)