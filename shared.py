import time
import threading
from typing import Optional
from selenium import webdriver


from WebWork import scrapper, inputs
from CONSTANTS import *
from core import engine
from core.classes.buildings import Buildings
from progress import saves

buildings_array = []
clicks_per_second = 0
cps_without_clicking = 0
mouse_cps = 0
click_value = 0
current_cookie_count = 0

driver: Optional[webdriver] = None

def start(d: webdriver) -> None:
    global driver
    driver = d

    saves.import_save()
    t = threading.Thread(target=fill_buildings_array,).start()
    engine.start_logic()




#Must be hard coded since each building has a different name
def fill_buildings_array() -> None:
    while not scrapper.get_element(OPTIONS_ADDRESS): #Ensures loaded in (options element exists)
        time.sleep(0.1)
    buildings_array.append(Buildings("Cursor"))
    buildings_array.append(Buildings("Grandma"))
    buildings_array.append(Buildings("Farm"))
    buildings_array.append(Buildings("Mine"))
    buildings_array.append(Buildings("Factory"))
    buildings_array.append(Buildings("Bank"))
    buildings_array.append(Buildings("Temple"))
    buildings_array.append(Buildings("Wizard tower"))
    buildings_array.append(Buildings("Shipment"))
    buildings_array.append(Buildings("Alchemy lab"))
    buildings_array.append(Buildings("Portal"))
    buildings_array.append(Buildings("Time machine"))
    buildings_array.append(Buildings("Prism"))
    buildings_array.append(Buildings("Chancemaker"))
    buildings_array.append(Buildings("Fractal engine"))
    buildings_array.append(Buildings("Javascript console"))
    buildings_array.append(Buildings("Idleverse"))
    buildings_array.append(Buildings("Cortex baker"))
    buildings_array.append(Buildings("You"))