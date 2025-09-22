
import os
import shutil
from pathlib import Path
from datetime import datetime

# File type dictionary
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Audio": [".mp3", ".wav"],
    "Videos": [".mp4", ".mkv"],
    "Archives": [".zip", ".rar", ".7z"],
    "Installers": [".exe", ".msi"],
    "Torrents": [".torrent"],
    "Apple Images": [".heic"],
    "Configs": [".json", ".ini", ".csv"],
    "Icons": [".ico"]
}

def organize_folder(folder_path):
    folder = Path(folder_path)

    if not folder.exists():
        print("❌ Folder does not exist.")
        return

    # Create or reuse txt file
    log_path = folder / "organizer_log.txt"

    with open(log_path, "a", encoding="utf-8") as log_file:
        log_file.write(f"\n--- Run at {datetime.now()} ---\n")

        for file in folder.iterdir():
            if file.is_file():
                # Skipping the log file so we don't move it while it's open
                if file.name == "organizer_log.txt":
                    continue
                moved = False
                for category, extensions in file_types.items():
                    if file.suffix.lower() in extensions:
                        target_folder = folder / category
                        target_folder.mkdir(exist_ok=True)

                        target_file = target_folder / file.name

                        # Skip duplicates
                        if target_file.exists():
                            log_file.write(f"Skipped (duplicate): {file.name}\n")
                            print(f"⚠️ Skipped duplicate: {file.name}")
                        else:
                            shutil.move(str(file), str(target_file))
                            log_file.write(f"Moved: {file.name} -> {category}/\n")
                            print(f"✅ Moved: {file.name} -> {category}/")
                        moved = True
                        break

                if not moved:
                    log_file.write(f"Uncategorized: {file.name}\n")
                    print(f"❓ Uncategorized: {file.name}")

    print("\n🎉 Organization complete! Log saved at:", log_path)

if __name__ == "__main__":
    folder_input = input("Enter folder path to organize: ")
    organize_folder(folder_input.strip())