import git
import subprocess
import datetime
import tkinter as tk
from tkinter import ttk

today = datetime.date.today()  # Get the current date
working_days = {0, 1, 2, 3, 4}  # Monday to Friday

if today.weekday() not in working_days:  # If today is not a working day
    exit()

repo_with_changes = {}  # Dictionary of repositories with changes

# Define repository paths
repo_paths = {
    'Kaggle': 'd:/Projects/Kaggle',
    'ML': 'd:/Projects/ML',
    'Python': 'd:/Projects/Python',
    'Tensorflow': 'd:/Projects/Tensorflow',
    'Earth Engine': 'd:/Projects/Earth Engine App',
    'MAUI': 'd:/Projects/C#/MAUI',
    'DSA': 'd:/Projects/C++/Self/DSA',
    'Plant Leaf Classification': 'd:/Projects/Plant Leaf Classification'
}

# Fetch repositories and check for changes
for name, path in repo_paths.items():
    try:
        repo = git.Repo(path=path)
        if repo.is_dirty():
            subprocess.run(['git', 'add', '-A'], cwd=repo.working_dir, capture_output=True)
            repo_with_changes[name] = repo.working_dir
    except git.exc.NoSuchPathError:
        print(f"Repository path not found: {path}")
    except Exception as e:
        print(f"Error accessing repository {name}: {e}")

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
        try:
            subprocess.run(['code', path], shell=True)
            popup.destroy()
            exit()
        except FileNotFoundError:
            print("VSCode is not installed or not found in the system path.")
        except Exception:
            l = tk.Label(text=f"Error occured, {Exception.__name__}")
            l.pack()
            b = tk.Button(text="OK", command=popup.destroy())
            b.pack()
            exit()

    def on_yes_click():
        on_click()

    def on_no_click():
        popup.destroy()
        exit()

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
        exit(0)
