# Download Directory Organizer

Organizes files in the downloads directory by classifying them into different folders according to their file types. This project is inspired by [DropIt](http://dropit.sourceforge.net/).

## Getting Started

### Using the UI

1. Clone or download the project.
2. Run the following command to start the UI:
   ```
   python3 ui.py
   ```
3. Use the UI to:
   - Select the source directory (e.g., your Downloads folder).
   - Select a configuration file (e.g., `config.json`) to define file types and their corresponding folders.
   - Preview changes to see what files will be moved.
   - Organize files into folders based on their types.
   - Save and load settings for future use.

### Using the Command Line

1. Run the script directly:
   ```
   python3 Cleaner\ 2.0/cleaner.py --directory <path_to_directory> --config <path_to_config.json>
   ```
2. Use additional arguments:
   - `--dry-run`: Preview changes without moving files.
   - `--log <path_to_log_file>`: Save logs to a file.

### Configuration

The `config.json` file defines the file types and their corresponding folders. You can customize it to add or modify file types. Example:
```json
{
  "Videos": [".mp4", ".mkv", ".avi"],
  "Pictures": [".jpg", ".png", ".gif"],
  "Documents": [".pdf", ".docx", ".txt"]
}
```

### Prerequisites

- Python 3.x
- `tkinter` (for the UI)

Install `tkinter` on Linux if not already installed:
```bash
sudo apt-get install python3-tk
```

## Features

- **UI**: A modern and minimal interface for organizing files.
- **Preview Changes**: See what files will be moved before making changes.
- **Save/Load Settings**: Save frequently used configurations for quick access.
- **Customizable**: Easily modify file types and folders in the `config.json` file.
- **Error Handling**: Handles file name conflicts and logs errors.

## Authors

- **Sparsh Bajaj** 
