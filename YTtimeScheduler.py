import pygetwindow
import psutil
import time
import tkinter
from tkinter import ttk

def alert():
    """
    Creates a pop up notifying user about the exhaustion of limit
    """
    root = tkinter.Tk()
    root.title("Time's Up!")
    root.wm_attributes('-topmost', 1)
    style = ttk.Style()
    style.configure('TButton', font=('Segoe UI', 10), borderwidth='4')
    def on_click():
        root.destroy()
        for process in psutil.process_iter(['pid', 'name']):
            if process.info['name'] == 'msedge.exe':
                process.kill()
    label = tkinter.Label(root, text="Your daily Youtube Quota has been reached!")
    label.pack()
    button = tkinter.Button(root, text="OK", command=on_click)
    button.pack()
    window_width = 400
    window_height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int((screen_width - window_width) / 2)
    center_y = int((screen_height - window_height) / 2)
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    root.mainloop()


def countdown():
    """
    Countdown timer for Youtube Quota
    """
    seconds = 5
    while True:
        time.sleep(1)
        seconds -= 1
        if seconds == 0:
            break
    return False

countdown_initiated = False

while True:
    for process in psutil.process_iter(['pid', 'name']):
        print("for loop")
        if process.info['name'] == 'msedge.exe': # Checking if browser is open
            print("Browser is open")
            try:
                window = pygetwindow.getWindowsWithTitle('YouTube')[0]
                if window.isActive:
                    print("YouTube is open")
                    if not countdown_initiated:
                        countdown_initiated = True
                        if countdown() == False:
                            alert()
                            break
                    else:
                        print("Countdown already initiated")
                        alert()
                    break
            except IndexError:
                continue
    time.sleep(10)
    print("sleep")  # Wait for 10 seconds before checking again