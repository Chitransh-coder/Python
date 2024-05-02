import git
import subprocess
import datetime
import tkinter as tk
from tkinter import ttk
import sys

today = datetime.date.today() # Get the current date
working_days = [0, 1, 2, 3, 4]  # Monday to Friday

if today.weekday() not in working_days: # If today is not a working day
    exit()


def create_popup():
    popup = tk.Tk()
    popup.wm_title("Popup")

    # Center the window on the screen
    window_width = 400
    window_height = 200
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    center_x = int((screen_width - window_width) / 2)
    center_y = int((screen_height - window_height) / 2)
    popup.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    # Keep the window on top of all others
    popup.wm_attributes('-topmost', 1)

    # Configure the style of the buttons to match Windows 11 appearance
    style = ttk.Style()
    style.configure('TButton', font=('Segoe UI', 10), borderwidth='4')

    # Function to open VSCode
    def open_vscode():
        try:
            subprocess.run(['code', '.'], cwd='d:/Projects', shell=True)
            popup.destroy()
        except FileNotFoundError:
            print("VSCode is not installed or not found in the system path.")

    # Function to exit the application
    def exit_app():
        popup.destroy()
        sys.exit()

    label = tk.Label(popup, text="Changes found! Open VSCode?", font=("Verdana", 10))
    label.pack(side="top", fill="x", pady=10)

    # Create 'Yes' and 'No' buttons using the styled ttk buttons
    button_yes = ttk.Button(popup, text="Yes", command=open_vscode, style='TButton')
    button_yes.pack(side="left", padx=(20, 10), pady=20)

    button_no = ttk.Button(popup, text="No", command=exit_app, style='TButton')
    button_no.pack(side="right", padx=(10, 20), pady=20)

    popup.mainloop()

# Kaggle repo
K_repo = git.Repo(path='d:/Projects/Kaggle')

# ML repo
ML_repo = git.Repo(path='d:/Projects/ML')

# Python repo
P_repo = git.Repo(path='d:/Projects/Python')

# TensorFlow repo
TF_repo = git.Repo(path='d:/Projects/Tensorflow')

# Fassal repo
F_repo = git.Repo(path='d:/Projects/Earth Engine App')

# MAUI repo
M_repo = git.Repo(path='d:/Projects/C#/MAUI')

# REST API repo
R_repo = git.Repo(path='d:/Projects/REST API/Study')

# Difference
if K_repo.is_dirty():

    out1 = subprocess.run(['git', 'add', '-A'],
                            cwd='d:/Projects/Kaggle',
                            capture_output=True)
    create_popup()
    sys.exit()

if ML_repo.is_dirty():
    out2 = subprocess.run(['git', 'add', '-A'],
                            cwd='d:/Projects/ML',
                            capture_output=True)
    create_popup()
    sys.exit()

if P_repo.is_dirty():
    out3 = subprocess.run(['git', 'add', '-A'],
                            cwd='d:/Projects/Python',
                            capture_output=True)
    create_popup()
    sys.exit()

if TF_repo.is_dirty():
    out4 = subprocess.run(['git', 'add', '-A'],
                            cwd='d:/Projects/Tensorflow',
                            capture_output=True)
    create_popup()
    sys.exit()

if F_repo.is_dirty():
    out5 = subprocess.run(['git', 'add', '-A'],
                            cwd='d:/Projects/Earth Engine App',
                            capture_output=True)
    create_popup()
    sys.exit()

if M_repo.is_dirty():
    out6 = subprocess.run(['git', 'add', '-A'],
                            cwd='d:/Projects/C#/MAUI',
                            capture_output=True)
    create_popup()
    sys.exit()

if R_repo.is_dirty():
    out7 = subprocess.run(['git', 'add', '-A'],
                            cwd='d:/Projects/REST API/Study',
                            capture_output=True)
    create_popup()
    sys.exit()
