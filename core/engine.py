import threading

import shared
from WebWork import scrapper
from core import achievements
from core.logic import purchases
from progress import saves


def start_logic():
    if saves.save_string.replace(" ", "") == "":
        achievements.get_free_achievements()

    notif_thread = threading.Thread(target=achievements.close_notifications).start()

    while True:
        scrapper.update_cookie_info()

        for i in shared.buildings_array:
            i.update_price()

        purchases.set_values()

        largest_value = max(shared.buildings_array, key=lambda building: building.get_value())
        if shared.current_cookie_count >= largest_value.get_price():
            largest_value.buy()
