import shared
from WebWork import scrapper, inputs
from selenium.webdriver.common.by import By

class Buildings:

    def __init__(self, name: str):
        self.price = 0
        self.object_name = name

        self.quantity = shared.driver.execute_script(f"return Game.Objects['{self.object_name}'].amount;")
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
    
    def buy(self) -> None:
        shared.driver.execute_script(f"Game.Objects['{self.object_name}'].buy();")

    def get_value(self):
        return self.value

    def set_value(self, value) -> None:
        self.value = value

    def update_price(self) -> None:
        self.price = shared.driver.execute_script(f"return Game.Objects['{self.object_name}'].price;")
