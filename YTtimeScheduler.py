import pygetwindow
import psutil
import time
import tkinter
from tkinter import ttk

youtube_quota = 3600 # 1 hour

def alert():
    """
    Creates a pop up notifying user about the exhaustion of limit
    """
    root = tkinter.Tk()
    root.title("Time's Up!")
    root.wm_attributes('-topmost', 1)
    style = ttk.Style()
    style.theme_use('clam')

    def on_click():
        root.destroy()
        for process in psutil.process_iter(['pid', 'name']):
            if process.info['name'] == 'msedge.exe':
                process.kill()

    label = ttk.Label(root, text="Your daily Youtube Quota has been reached!")
    label.pack(pady=20)
    button = ttk.Button(root, text="OK", command=on_click)
    button.pack(pady=10)

    window_width = 400
    window_height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int((screen_width - window_width) / 2)
    center_y = int((screen_height - window_height) / 2)
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    root.mainloop()

def countdown(seconds):
    """
    Countdown timer for Youtube Quota
    """
    while seconds > 0:
        time.sleep(1)
        seconds -= 1
        with open('D:/YouTubeTime.bin', 'wb') as file:
            file.write(seconds.to_bytes(4, 'big'))
    return False

countdown_initiated = False

try:
    with open('D:/YouTubeTime.bin', 'rb') as file:
        youtube_quota = int.from_bytes(file.read(), 'big')
except FileNotFoundError:
    with open('D:/YouTubeTime.bin', 'wb') as file:
        file.write(youtube_quota.to_bytes(4, 'big'))

while True:
    msedge_open = False
    youtube_open = False

    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == 'msedge.exe':  # Checking if browser is open
            msedge_open = True
            try:
                window = pygetwindow.getWindowsWithTitle('YouTube')[0]
                if window.isActive:
                    youtube_open = True
                    break
            except IndexError:
                continue

    if msedge_open and youtube_open:
        if not countdown_initiated:
            countdown_initiated = True
        if countdown(youtube_quota) == False:
            alert()
            break
    else:
        countdown_initiated = False

    time.sleep(10)