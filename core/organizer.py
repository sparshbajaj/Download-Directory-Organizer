import os
import shutil
import json
from pathlib import Path

class DownloadOrganizer:
    def __init__(self, config_path=None):
        import sys
        import os
        
        if config_path is None:
            # Handle PyInstaller bundled executable path
            if getattr(sys, 'frozen', False):
                base_path = os.path.dirname(sys.executable)
                config_path = os.path.join(base_path, 'config.json')
            else:
                config_path = 'config.json'
                
        self.config = self._load_config(config_path)
        self.file_lists = {category: [] for category in self.config.keys()}
        
    def _load_config(self, config_path):
        """Load and sanitize configuration file"""
        with open(config_path) as f:
            config = json.load(f)
        
        cleaned = {}
        for category, exts in config.items():
            cleaned[category] = list({
                ext.lower().strip() if ext.startswith('.') else f'.{ext.strip().lower()}'
                for ext in exts
            })
        return cleaned
    
    def organize(self, source_dir, dry_run=False):
        """Main organization routine returns list of planned moves"""
        source = Path(source_dir)
        self._categorize_files(source)
        planned_moves = []
        
        for category, files in self.file_lists.items():
            if not files:
                continue
                
            dest = source / category
            self._create_dir(dest)
            
            for file in files:
                src_path = source / file
                dest_path = dest / file
                planned_moves.append((str(src_path), str(dest_path)))
                
                if dry_run:
                    print(f"[Dry] Would move {src_path} -> {dest_path}")
                else:
                    try:
                        shutil.move(str(src_path), str(dest_path))
                        print(f"Moved {file} to {category}")
                    except Exception as e:
                        print(f"Error moving {file}: {str(e)}")
        
        if dry_run and planned_moves:
            preview_path = source / "preview_changes.txt"
            with open(preview_path, 'w') as f:
                f.write("Planned file moves:\n\n")
                f.write("\n".join([f"{src} -> {dest}" for src, dest in planned_moves]))
            print(f"\nPreview file created: {preview_path}")
    
    def _categorize_files(self, source_dir):
        """Categorize files based on config"""
        for item in source_dir.iterdir():
            if item.is_file():
                for category, exts in self.config.items():
                    if item.suffix.lower() in exts:
                        self.file_lists[category].append(item.name)
                        break
    
    def _create_dir(self, path):
        """Create directory if needed"""
        if not path.exists():
            path.mkdir()
            print(f"Created directory: {path.name}")