import PyInstaller.__main__
import os
import sys

# Configure paths for PyInstaller
add_data = [
    f'config.json{os.pathsep}.',
    f'core{os.pathsep}core',
    f'organizer.ico{os.pathsep}.'
]

if getattr(sys, 'frozen', False):
    base_dir = sys._MEIPASS
else:
    base_dir = os.path.dirname(__file__)

PyInstaller.__main__.run([
    'ui.py',
    '--name=DownloadOrganizer',
    '--onefile',
    '--windowed',
    '--icon=organizer.ico',
    *[f'--add-data={item}' for item in add_data],
    '--hidden-import=tkinter',
    '--clean',
    '--noconfirm'
])