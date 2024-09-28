import time
import threading

from WebWork import scrapper, inputs
from CONSTANTS import *
from core import engine
from core.classes.buildings import Buildings
from core.engine import total_cps
from progress import saves

buildings_array = []
total_cps = 0
current_cookie_count = 0

def start(driver):
    scrapper.set_driver(driver)
    Buildings.set_driver(driver)
    inputs.set_driver(driver)

    saves.import_save()
    T = threading.Thread(target=fill_buildings_array,).start()
    engine.start_logic()




#Must be hard coded since each building has a different name
def fill_buildings_array():
    while not scrapper.get_element(OPTIONS_ADDRESS): #Ensures loaded in (options element exists)
        time.sleep(0.1)
    buildings_array.append(Buildings(CURSOR_ADDRESS, "Cursor"))
    buildings_array.append(Buildings(GRANDMA_ADDRESS, "Grandma"))
    buildings_array.append(Buildings(FARM_ADDRESS, "Farm"))
    buildings_array.append(Buildings(MINE_ADDRESS, "Mine"))
    buildings_array.append(Buildings(FACTORY_ADDRESS, "Factory"))
    buildings_array.append(Buildings(BANK_ADDRESS, "Bank"))
    buildings_array.append(Buildings(TEMPLE_ADDRESS, "Temple"))
    buildings_array.append(Buildings(WIZARD_ADDRESS, "Wizard tower"))
    buildings_array.append(Buildings(SHIPMENT_ADDRESS, "Shipment"))
    buildings_array.append(Buildings(ALCHEMY_ADDRESS, "Alchemy lab"))
    buildings_array.append(Buildings(PORTAL_ADDRESS, "Portal"))
    buildings_array.append(Buildings(TIME_ADDRESS, "Time machine"))
    buildings_array.append(Buildings(PRISM_ADDRESS, "Prism"))
    buildings_array.append(Buildings(CHANCEMAKER_ADDRESS, "Chancemaker"))
    buildings_array.append(Buildings(FRACTAL_ADDRESS, "Fractal engine"))
    buildings_array.append(Buildings(JAVASCRIPT_ADDRESS, "Javascript console"))
    buildings_array.append(Buildings(IDLEVERSE_ADDRESS, "Idleverse"))
    buildings_array.append(Buildings(CORTEX_ADDRESS, "Cortex baker"))
    buildings_array.append(Buildings(YOU_ADDRESS, "You"))

def convert_string_to_price(num_string):
    num_string = num_string.replace(',','')
    last_character = num_string[-1]
    if last_character.isdigit():
        return int(num_string)
    else:
        num = num_string.split()[0]
        unit = num_string.split()[1]
        match unit:
            case "million":
                return num * (10**6)
            case "billion":
                return num * (10**9)
            case "trillion":
                return num * (10**12)
            case "quadrillion":
                return num * (10**15)