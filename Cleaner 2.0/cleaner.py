import shutil
import os
import json
import logging
from tqdm import tqdm

# Set up logging
logging.basicConfig(filename='fileorganizer.log', level=logging.INFO)

# Get the directory containing the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the config.json file
config_path = os.path.join(script_dir, 'config.json')

# Load the folders and file types from the configuration file
with open(config_path) as f:
    folders = json.load(f)

# Get the current working directory
cwd = os.path.expanduser("~") + os.sep + "Downloads"
os.chdir(cwd)

# Create the directories if they don't exist
for folder in folders.keys():
    if not os.path.exists(folder):
        os.mkdir(folder)

#list of created folders
folders_list = folders.keys()

for file in tqdm(os.listdir(cwd)):
    for folder, file_types in folders.items():
        if os.path.isdir(file) and file not in folders_list:
            continue
        for file_type in file_types:
            if file.endswith(file_type):
                destination = os.path.join(cwd, folder, file)
                if os.path.exists(destination):
                    logging.warning(f"{file} already exists in {folder} folder, skipping...")
                    continue
                try:
                    shutil.move(os.path.join(cwd, file), destination)
                except shutil.Error as e:
                    logging.error(f"Error moving {file}: {e}")