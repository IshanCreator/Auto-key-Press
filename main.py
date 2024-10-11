import pyautogui
import time
from pynput import keyboard
from tkinter import messagebox
key_to_press = 'right'  # Enter your Key 
interval = 6  # Enter your time interval
running = False


def on_presskey(key):
    global running
    try:
        if key.char == '>':  # Start key
            running = True
            print("Auto key presser started.")
            messagebox.showinfo("Ishan Baba ki jai", "Start (chal Gaya) ")
        elif key.char == '<':  # Stop key>
            running = False
            print("Auto key presser stopped.")
            messagebox.showinfo("Ishan Baba ki jai", "Stop (tham ja)")
    except AttributeError:
        pass


def auto_key_presser():
    while True:
        if running:
            pyautogui.press(key_to_press)
            time.sleep(interval)


if __name__ == "__main__":
    listener = keyboard.Listener(on_press=on_presskey)
    listener.start()

    try:
        auto_key_presser()
    except KeyboardInterrupt:
        print("Program terminated.")
    finally:
        listener.stop()

# In this code:
# •  Press '>' to start
#
# •  Press '<' to stop
