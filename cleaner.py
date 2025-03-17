import shutil
import os
import json
import logging
from tqdm import tqdm
from pathlib import Path
import argparse

# Set up logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def load_config(config_path):
    try:
        with open(config_path) as f:
            return json.load(f)
    except FileNotFoundError:
        logging.error("Configuration file not found.")
        raise SystemExit("Configuration file not found.")
    except json.JSONDecodeError:
        logging.error("Configuration file is not a valid JSON.")
        raise SystemExit("Configuration file is not a valid JSON.")

def create_folders(folders, base_dir):
    for folder in folders.keys():
        folder_path = base_dir / folder
        if not folder_path.exists():
            try:
                folder_path.mkdir()
                logging.info(f"Created folder: {folder}")
            except PermissionError:
                logging.error(f"Permission denied: Unable to create folder {folder}")


def organize_files(folders, base_dir, dry_run):
    summary = {"moved": 0, "skipped": 0, "errors": 0}
    for file in tqdm(os.listdir(base_dir)):
        file_path = base_dir / file
        if file_path.is_dir() and file not in folders.keys():
            logging.info(f"Skipping directory: {file}")
            summary["skipped"] += 1
            continue
        for folder, file_types in folders.items():
            if any(file.endswith(file_type) for file_type in file_types):
                destination = base_dir / folder / file
                if destination.exists():
                    logging.warning(f"{file} already exists in {folder} folder, skipping...")
                    summary["skipped"] += 1
                    break
                if dry_run:
                    logging.info(f"[Dry Run] Would move {file} to {folder}")
                    summary["moved"] += 1
                else:
                    try:
                        shutil.move(str(file_path), str(destination))
                        logging.info(f"Moved {file} to {folder}")
                        summary["moved"] += 1
                    except shutil.Error as e:
                        logging.error(f"Error moving {file}: {e}")
                        summary["errors"] += 1
                break
    return summary

def main():
    parser = argparse.ArgumentParser(description="Cleaner 3.0 - Organize your Downloads folder.")
    parser.add_argument("--config", type=str, default=None, help="Path to the configuration file.")
    parser.add_argument("--directory", type=str, help="Path to the directory to organize.")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without moving files.")
    parser.add_argument("--log", type=str, help="Path to the log file.")

    args = parser.parse_args()

    # Set custom log file if provided
    if args.log:
        logging.basicConfig(filename=args.log, level=logging.INFO, 
                            format='%(asctime)s - %(levelname)s - %(message)s')

    # Determine configuration file path
    if args.config:
        config_path = Path(args.config)
    else:
        # Ensure the config.json is located in the same directory as the executable
        config_path = Path(sys._MEIPASS) / 'config.json' if hasattr(sys, '_MEIPASS') else Path(__file__).parent / 'config.json'

    # Load configuration
    if not config_path.exists():
        default_config = {
            "Videos": [".mp4", ".mkv", ".avi", ".mpg", ".mov", ".wmv", ".flv", ".mpg"],
            "Pictures": [".gif", ".jpg", ".png", ".jpeg", ".cr2", ".nef", ".bmp", ".tiff", ".svg", ".ico", ".JPG"],
            "Music": [".aac", ".mp3", ".wma", ".wav"],
            "Compressed": [".zip", ".rar", ".tar", ".tar.gz", ".tgz", ".bz", ".7z", ".tgz", ".tar.bz2"],
            "Books": [".pdf", ".epub"],
            "Documents": [".doc", ".docx", ".txt", ".ppt", ".pptx", ".pdf", ".rtf", ".csv", ".xls", ".xlsx"],
            "Programs": [".exe", ".msi"],
            "VirtualDisk": [".vmdk", ".ova", ".iso", ".img"],
            "Extras": [".html", ".c", ".cpp", ".torrent", ".ino", "ttf", ".otf", ".ipa", "apk", ".lottie", ".json"],
            "Scripts": [".py", ".sh", ".bat", ".ps1"],
            "Adobe": [".xd", ".ai", ".psd", ".svg", ".eps"]
        }
        with open(config_path, "w") as f:
            json.dump(default_config, f, indent=4)
        logging.info(f"Default configuration file created at {config_path}")

    folders = load_config(config_path)

    # Determine base directory
    if args.directory:
        base_dir = Path(args.directory)
    else:
        base_dir = Path.home() / 'Downloads'

    if not base_dir.exists():
        logging.error(f"Directory {base_dir} does not exist.")
        raise SystemExit(f"Directory {base_dir} does not exist.")

    # Create folders
    create_folders(folders, base_dir)

    # Organize files
    summary = organize_files(folders, base_dir, args.dry_run)

    # Display summary
    logging.info("\nSummary:")
    logging.info(f"Files moved: {summary['moved']}")
    logging.info(f"Files skipped: {summary['skipped']}")
    logging.info(f"Errors: {summary['errors']}")

    # Pause to keep terminal open
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()