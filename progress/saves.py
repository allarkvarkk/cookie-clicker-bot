import threading
import os


from WebWork import inputs
from CONSTANTS import OPTIONS_ADDRESS, BIG_COOKIE

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Set the path to save.txt based on the current directory
save_file_path = os.path.join(current_dir, 'save.txt')

with open(save_file_path, 'r') as file:
    save_string = file.readline()

def import_save() -> None:
    inputs.click_address("#langSelect-EN", 1000000)
    if save_string != "":
        inputs.click_address(OPTIONS_ADDRESS, 9999)
        inputs.click_address("#menu > div:nth-child(3) > div > div:nth-child(4) > a:nth-child(2)")
        inputs.send_keys("#textareaPrompt", save_string)
        inputs.click_address("#promptOption0")
    auto_clicker_thread = threading.Thread(target=inputs.auto_clicker)
    auto_clicker_thread.start()
