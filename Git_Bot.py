import git
import subprocess
import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import winreg as reg
import os
import sys

today = datetime.date.today() # Get the current date
working_days = [0, 1, 2, 3, 4]  # Monday to Friday

if today.weekday() not in working_days: # If today is not a working day
    exit()

repo_with_changes = {}  # List of repositories with changes

# fetch repo
try:
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

    # DSA repo
    D_repo = git.Repo(path='d:/Projects/C++/Self/DSA')

    # Plant Leaf Classification repo
    Pl_repo = git.Repo(path="d:/Projects/Plant Leaf Classification")

except FileNotFoundError:
    print("Please update the path of the repositories.")


# Difference
if K_repo.is_dirty():

    out1 = subprocess.run(['git', 'add', '-A'],
                            cwd=K_repo.working_dir,
                            capture_output=True)
    repo_with_changes['Kaggle'] = K_repo.working_dir

if ML_repo.is_dirty():
    out2 = subprocess.run(['git', 'add', '-A'],
                            cwd=ML_repo.working_dir,
                            capture_output=True)
    repo_with_changes['ML'] = ML_repo.working_dir

if P_repo.is_dirty():
    out3 = subprocess.run(['git', 'add', '-A'],
                            cwd=P_repo.working_dir,
                            capture_output=True)
    repo_with_changes['Python'] = P_repo.working_dir

if TF_repo.is_dirty():
    out4 = subprocess.run(['git', 'add', '-A'],
                            cwd=TF_repo.working_dir,
                            capture_output=True)
    repo_with_changes['Tensorflow'] = TF_repo.working_dir

if F_repo.is_dirty():
    out5 = subprocess.run(['git', 'add', '-A'],
                            cwd=F_repo.working_dir,
                            capture_output=True)
    repo_with_changes['Earth Engine'] = F_repo.working_dir

if M_repo.is_dirty():
    out6 = subprocess.run(['git', 'add', '-A'],
                            cwd=M_repo.working_dir,
                            capture_output=True)
    repo_with_changes['MAUI'] = M_repo.working_dir

if D_repo.is_dirty():
    out8 = subprocess.run(['git', 'add', '-A'],
                            cwd=D_repo.working_dir,
                            capture_output=True)
    repo_with_changes['DSA'] = D_repo.working_dir

def create_popup():

    # Create the main window
    popup = tk.Tk()
    popup.title("Check for Changes")
    popup.wm_attributes('-topmost', 1)
    style = ttk.Style()
    style.configure('TButton', font=('Segoe UI', 10), borderwidth='4')

    # Create labels and buttons
    label = tk.Label(popup, text="Changes found! Open VSCode?")
    label.pack()

    # Show a list of repositories with changes
    mess = tk.Label(popup, text="Repositories with changes:")
    mess.pack(pady=10)

    dropdown = ttk.Combobox(popup, values=list(repo_with_changes.keys()))
    dropdown.pack(pady=15)

    def on_click():
        repo = dropdown.get()
        path = repo_with_changes[repo]
        popup.destroy()
        try:
            subprocess.run(['code', path], shell=True)
        except FileNotFoundError:
            print("VSCode is not installed or not found in the system path.")

    def on_yes_click():
        on_click()

    def on_no_click():
        popup.destroy()
        sys.exit()

    button_yes = ttk.Button(popup, text="Yes", command=on_yes_click, style='TButton')
    button_yes.pack(side="left", padx=(20, 10), pady=20)

    button_no = ttk.Button(popup, text="No", command=on_no_click, style='TButton')
    button_no.pack(side="right", padx=(10, 20), pady=20)

    # Center the window on the screen
    window_width = 400
    window_height = 200
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    center_x = int((screen_width - window_width) / 2)
    center_y = int((screen_height - window_height) / 2)
    popup.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    # Start the GUI event loop
    popup.mainloop()

if repo_with_changes:
    try:
        create_popup()
    finally:
        sys.exit(0)
