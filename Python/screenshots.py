import os
import shutil

# Get user home directory
home = os.path.expanduser("~")
desktop_path = os.path.join(home, "Desktop")
pictures_path = os.path.join(home, "Pictures")

# List all files on Desktop
files = os.listdir(desktop_path)

# Define common screenshot prefixes
screenshot_prefixes = ["Screen Shot", "Screenshot"]

# Loop through files and move screenshots
for file_name in files:
    if any(file_name.startswith(prefix) for prefix in screenshot_prefixes):
        source = os.path.join(desktop_path, file_name)
        destination = os.path.join(pictures_path, file_name)
        try:
            shutil.move(source, destination)
            print(f"Moved: {file_name}")
        except Exception as e:
            print(f"Failed to move {file_name}: {e}")

print("✅ Done moving screenshots.")
