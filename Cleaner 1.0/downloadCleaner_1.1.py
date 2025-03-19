import shutil
import os
from tqdm import tqdm

# Define the folders and file types
folders = {
    'Videos': ['.mp4', '.mkv', '.avi', '.mpg', '.mov', '.wmv', '.flv', '.mpg'],
    'Pictures': ['.gif', '.jpg', '.png', '.jpeg', '.cr2', '.nef', '.bmp', '.tiff', '.svg', '.ico', '.JPG'],
    'Music': ['.aac', '.mp3', '.wma', '.wav'],
    'Compressed': ['.zip', '.rar', '.tar', '.tar.gz', '.tgz', '.bz', '.7z', '.tgz', '.tar.bz2'],
    'Books': ['.pdf', '.epub'],
    'Documents': [".doc", ".docx", ".txt", ".ppt", ".pptx", ".pdf", ".rtf", ".csv",".xls" , ".xlsx"],
    'Programs': ['.exe', '.msi'],
    'VirtualDisk': [".vmdk", ".ova", ".iso", ".img"],
    'Extras': [".html", ".c", ".cpp", ".torrent", ".ino", "ttf", '.otf', ".ipa", "apk", ".lottie", ".json"],
    'Scripts': ['.py','.sh','.bat','.ps1'],
    'Adobe': [".xd", ".ai", ".psd", ".svg", ".eps"]
}

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
                    print(f"{file} already exists in {folder} folder, skipping...")
                    continue
                shutil.move(os.path.join(cwd, file), destination)