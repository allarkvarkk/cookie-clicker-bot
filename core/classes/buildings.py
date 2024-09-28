import shared
from WebWork import scrapper, inputs
from selenium.webdriver.common.by import By

class Buildings:
    driver = None

    @classmethod
    def set_driver(cls, driver):
        cls.driver=driver

    def __init__(self, address, name):
        self.element = scrapper.get_element(address)
        self.object_name = name
        price_text = self.element.find_element(By.CSS_SELECTOR, ".price").text

        self.quantity = self.element.find_element(By.CSS_SELECTOR, ".title.owned").text
        self.stored_cps = Buildings.driver.execute_script(f"return Game.Objects['{self.object_name}'].storedTotalCps;")
        self.quantity = 0
        if not self.quantity:
            self.quantity = 0

        if price_text == "" or price_text == " ": #Checks if the price string is empty (building not listed yet)
            self.price = 0
        else:
            self.price = shared.convert_string_to_price(price_text)

    def get_price(self):
        return self.price

    def get_building_element(self):
        return self.element

    def get_quantity(self):
        return self.quantity

    def get_stored_cps(self):
        return self.stored_cps
    
    def buy(self):
        inputs.click_element(self.element)

    # value = (increase in CPS)/(cost)(time to afford)
