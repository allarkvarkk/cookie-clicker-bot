import threading

import shared
from WebWork import scrapper
from core import achievements
from progress import saves

cookie_count = 0
total_cps = 0
buildings_array = []

def start_logic():
    if saves.save_string.replace(" ", "") == "":
        achievements.get_free_achievements()

    notif_thread = threading.Thread(target=achievements.close_notifications).start()

    while True:
        scrapper.update_cookie_info()














