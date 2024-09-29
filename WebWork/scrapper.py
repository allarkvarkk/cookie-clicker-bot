
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import shared
from CONSTANTS import COOKIES_INFO_BAR

def get_element(address, timeout=10):
    try:
        button = WebDriverWait(shared.driver, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, address))
        )
        return button
    except Exception as e:
        print("ERROR (get_element) with address ", address, ": ", e)


def does_element_exist(address):
    try:
        button = WebDriverWait(shared.driver, 0).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, address))
        )
        return True
    except Exception as e:
        return False


def update_cookie_info():
    try:
        cookies = WebDriverWait(shared.driver, 0).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,COOKIES_INFO_BAR))
        )
        shared.cps_without_clicking = cookies.text.split(" ")[0]
        shared.current_cookie_count = cookies.text.split(": ")[1]
        #shared.mouse_cps = driver.execute_script(f"return Game.computeMouseCps;")


    except Exception as e:
        print("ERROR (get_num_of_cookies): ", e)

