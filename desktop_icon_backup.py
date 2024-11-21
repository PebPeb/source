# By: Bryce Keen

import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

app_name = "desktop_icon_backup"  
appDataDir = os.path.join(os.getenv('USERPROFILE'), "Documents" + "\\" + app_name)

def main():
    os.makedirs(appDataDir, exist_ok=True)
    show_main_window()


def show_main_window():
    root = tk.Tk()
    root.title("Desktop Arrangement Backup")
    root.geometry("300x150")

    # Create the Save button
    save_button = tk.Button(root, text="Save Desktop Arrangement", command=save_desktop_arrangement)
    save_button.pack(pady=10)

    # Create the Load button
    load_button = tk.Button(root, text="Load Desktop Arrangement", command=load_desktop_arrangement)
    load_button.pack(pady=10)

    root.mainloop()


def save_desktop_arrangement():
    output_file = filedialog.asksaveasfilename(
        title="Save Desktop Arrangement",
        defaultextension=".reg",
        filetypes=[("Registry Files", "*.reg")],
        initialdir=appDataDir  
    )

    if not output_file:
        messagebox.showwarning("Action Cancelled", "No file location was selected. Operation aborted.")
        return

    registry_key = r"HKEY_CURRENT_USER\Software\Microsoft\Windows\Shell\Bags\1\Desktop"

    command = f'reg export "{registry_key}" "{output_file}" /y'

    try:
        subprocess.run(command, shell=True, check=True)
        messagebox.showinfo("Success", f"Desktop arrangement saved successfully to:\n{output_file}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to save desktop arrangement:\n{e}")


def load_desktop_arrangement():
    input_file = filedialog.askopenfilename(
        title="Load Desktop Arrangement",
        filetypes=[("Registry Files", "*.reg")],
        initialdir=appDataDir  
    )

    if not input_file:
        messagebox.showwarning("Action Cancelled", "No file location was selected. Operation aborted.")
        return

    command = f'reg import "{input_file}"'

    try:
        subprocess.run(command, shell=True, check=True)
        messagebox.showinfo("Success", f"Desktop arrangement loaded successfully from:\n{input_file}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to load desktop arrangement:\n{e}")

    restart_windows_explorer()

def restart_windows_explorer():
    try:
        # Kill the explorer.exe process
        subprocess.run(["taskkill", "/F", "/IM", "explorer.exe"], check=True)
        print("Windows Explorer stopped successfully.")
        
        # Restart explorer.exe
        subprocess.run(["start", "explorer.exe"], shell=True)
        print("Windows Explorer restarted successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to restart Windows Explorer: {e}")

if __name__ == "__main__":
    main()
