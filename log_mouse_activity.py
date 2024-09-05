from pynput import mouse
import logging
from datetime import datetime
from time import sleep


# Logg mouse activity
# Projet to send this data to a server and display multiple users activity into a web dashboard




# Setup logging
logging.basicConfig(filename= 'D:\Documents\Python\Log_mouse_activity/mouse_activity.log', level=logging.INFO, format='%(asctime)s: %(message)s')

def on_move(x, y):
    logging.info(f"Mouse moved to ({x}, {y})")
    print(f"Mouse moved to ({x}, {y})")

def on_click(x, y, button, pressed):
    if pressed:
        logging.info(f"Mouse clicked at ({x}, {y}) with {button}")
        print(f"Mouse clicked at ({x}, {y}) with {button}")
    else:
        logging.info(f"Mouse released at ({x}, {y}) with {button}")
        print(f"Mouse released at ({x}, {y}) with {button}")

def on_scroll(x, y, dx, dy):
    logging.info(f"Mouse scrolled at ({x}, {y}) with delta ({dx}, {dy})")
    print(f"Mouse scrolled at ({x}, {y}) with delta ({dx}, {dy})")

# # Set up the listener
# with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
#     listener.join()

# Set up the listener
listener = mouse.Listener(on_click=on_click, on_scroll=on_scroll)  # on_move=on_move, 
listener.start()

# Run the listener for a specified time (e.g., 60 seconds)
sleep(20)
listener.stop()