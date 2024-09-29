
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import shared


def main():
    options = Options()
    options.binary_location = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
    options.add_experimental_option("detach", True)
    options.add_argument("--disable-extensions")

    # Use ChromeDriverManager to manage Brave since it's Chromium-based
    driver = webdriver.Chrome(options=options)

    driver.maximize_window()
    driver.get("https://orteil.dashnet.org/cookieclicker/")

    shared.start(driver)

if __name__ == "__main__":
    main()
