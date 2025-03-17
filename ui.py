import os
import shutil
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pathlib import Path
import json
import sys
from pathlib import Path

# Add the Cleaner 2.0 directory to the Python path
sys.path.append(str(Path(__file__).parent / "Cleaner 2.0"))

from cleaner import load_config, create_folders, organize_files

def organize_files_ui():
    source_dir = filedialog.askdirectory(title="Select Source Directory")
    if not source_dir:
        return

    config_path = filedialog.askopenfilename(title="Select Configuration File", filetypes=[("JSON files", "*.json")])
    if not config_path:
        return

    try:
        folders = load_config(config_path)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load configuration: {e}")
        return

    base_dir = Path(source_dir)

    # Create folders based on configuration
    create_folders(folders, base_dir)

    # Organize files
    summary = organize_files(folders, base_dir, dry_run=False)

    messagebox.showinfo("Summary", f"Files moved: {summary['moved']}\nFiles skipped: {summary['skipped']}\nErrors: {summary['errors']}")

def preview_changes_ui():
    source_dir = filedialog.askdirectory(title="Select Source Directory")
    if not source_dir:
        return

    config_path = filedialog.askopenfilename(title="Select Configuration File", filetypes=[("JSON files", "*.json")])
    if not config_path:
        return

    try:
        folders = load_config(config_path)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load configuration: {e}")
        return

    base_dir = Path(source_dir)

    # Preview changes
    summary = organize_files(folders, base_dir, dry_run=True)

    messagebox.showinfo("Preview", f"Files to be moved: {summary['moved']}\nFiles skipped: {summary['skipped']}\nErrors: {summary['errors']}")

def save_settings_ui():
    settings = {
        "source_dir": filedialog.askdirectory(title="Select Source Directory"),
        "config_path": filedialog.askopenfilename(title="Select Configuration File", filetypes=[("JSON files", "*.json")])
    }

    if not settings["source_dir"] or not settings["config_path"]:
        messagebox.showerror("Error", "Both source directory and configuration file must be selected.")
        return

    with open("settings.json", "w") as f:
        json.dump(settings, f)

    messagebox.showinfo("Success", "Settings saved successfully.")

def load_settings_ui():
    try:
        with open("settings.json", "r") as f:
            settings = json.load(f)
        return settings
    except FileNotFoundError:
        messagebox.showerror("Error", "No saved settings found.")
        return None

# Create the main UI window
def create_ui():
    root = tk.Tk()
    root.title("Download Directory Organizer")
    root.geometry("400x300")

    # Organize button
    organize_button = ttk.Button(root, text="Organize Files", command=organize_files_ui)
    organize_button.pack(pady=10)

    # Preview button
    preview_button = ttk.Button(root, text="Preview Changes", command=preview_changes_ui)
    preview_button.pack(pady=10)

    # Save settings button
    save_button = ttk.Button(root, text="Save Settings", command=save_settings_ui)
    save_button.pack(pady=10)

    # Load settings button
    load_button = ttk.Button(root, text="Load Settings", command=lambda: messagebox.showinfo("Settings", load_settings_ui()))
    load_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_ui()