
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
    shared.cps_without_clicking = shared.driver.execute_script(f"return Game.cookiesPs;")
    shared.current_cookie_count = shared.driver.execute_script(f"return Game.cookies;")
    shared.click_value = shared.driver.execute_script(f"return Game.computedMouseCps;")
    shared.mouse_cps = shared.click_value * shared.clicks_per_second

