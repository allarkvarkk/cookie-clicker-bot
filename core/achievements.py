import threading
import time

from WebWork import scrapper, inputs
from CONSTANTS import *

news_clicks = 50

def get_free_achievements():
    threads = []

    def news_achievement():
        for i in range(news_clicks+1): #achievement requires 50 clicks on news
            inputs.click_address(NEWS_ADDRESS, retries=10) #sometimes takes a while to load

    def stat_achievements():
        inputs.click_address(STATS_ADDRESS, retries=10) #somtimes takes a while to load
        inputs.click_address(SMALL_COOKIE_ADDRESS)
        inputs.scroll_into_view(HIDDEN_ACHIEVEMENT_ADDRESS)
        inputs.click_address(ACHIEVEMENT_POP_UP_X)
        inputs.click_address(HIDDEN_ACHIEVEMENT_ADDRESS)
        inputs.click_address(STATS_ADDRESS)  # exit stats tab

    def rename_achievement():
        inputs.click_address(NAME_ADDRESS)
        inputs.send_keys(NAME_BOX_ADDRESS, "BOT", )
        inputs.click_address(NAME_CONFIRM_ADDRESS)

    threads.append(threading.Thread(target=news_achievement))
    threads.append(threading.Thread(target=stat_achievements))

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    rename_achievement()

def close_notifications(do_once=False):
    def close():
        if scrapper.does_element_exist(ACHIEVEMENT_POP_UP_X):
            inputs.click_address(ACHIEVEMENT_POP_UP_X)
        else:
            if scrapper.does_element_exist(BACK_UP_SAVE_NOTIFICATION_X):
                inputs.click_address(BACK_UP_SAVE_NOTIFICATION_X)
    if not do_once:
        while True:
            close()
            time.sleep(20)
    else:
        close()
