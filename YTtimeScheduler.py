import pygetwindow
import psutil
import time
import datetime
import tkinter
from tkinter import ttk

today = datetime.date.today()  # Get the current date
working_days = {0, 1, 2, 3, 4}  # Monday to Friday
free_days = {5, 6}  # Saturday and Sunday
if today.weekday() in working_days:
    youtube_quota = 3600  # 1 hour in seconds
elif today.weekday() in free_days:
    youtube_quota = 7200 # 2 hours in seconds
else:
    youtube_quota = 3600

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
    def on_close():
        root.destroy()
        for process in psutil.process_iter(['pid', 'name']):
            if process.info['name'] == 'msedge.exe':
                process.kill()
    root.protocol("WM_DELETE_WINDOW", on_close)
    style.configure('TButton', font=('Segoe UI', 10), borderwidth='4')
    root.resizable(False, False)
    root.attributes('-toolwindow', 1)

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
    return False

countdown_initiated = False

while True:
    msedge_open = False
    youtube_open = False
    print("Checking for browser and YouTube...")
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == 'msedge.exe':  # Checking if browser is open
            msedge_open = True
            try:
                window = pygetwindow.getWindowsWithTitle('YouTube')[0]
                if 'YouTube' in window.title:
                    youtube_open = True
            except IndexError:
                continue
    print(f"msedge_open: {msedge_open}, youtube_open: {youtube_open}")
    if msedge_open and youtube_open:
        if not countdown_initiated:
            countdown_initiated = True
        if countdown(youtube_quota) == False:
            alert()
            break
    else:
        countdown_initiated = False

    time.sleep(1)