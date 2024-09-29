import shared
from WebWork import scrapper, inputs
from selenium.webdriver.common.by import By

class Buildings:

    def __init__(self, address, name):
        self.element = scrapper.get_element(address)
        self.object_name = name

        price_text = self.element.find_element(By.CSS_SELECTOR, ".price").text
        if price_text == "" or price_text == " ":  # Checks if the price string is empty (building not listed yet)
            self.price = 0
        else:
            self.price = shared.convert_string_to_price(price_text)

        self.quantity = self.element.find_element(By.CSS_SELECTOR, ".title.owned").text
        self.total_building_cps = shared.driver.execute_script(f"return Game.Objects['{self.object_name}'].storedTotalCps;")
        self.cps_per = shared.driver.execute_script(f"return Game.Objects['{self.object_name}'].storedCps")


        self.quantity = 0
        if not self.quantity:
            self.quantity = 0

        self.value = 0



    def get_price(self):
        return self.price

    def get_building_element(self):
        return self.element

    def get_quantity(self):
        return self.quantity

    def get_total_building_cps(self):
        return self.total_building_cps

    def get_cps_per(self):
        return self.cps_per
    
    def buy(self):
        inputs.click_element(self.element)

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value