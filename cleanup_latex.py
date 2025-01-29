import os
import shutil

# Get the root directory of the repository (where the script is located)
repo_root = os.path.dirname(os.path.abspath(__file__))

# File extensions to move
extensions = {".aux", ".out", ".log", ".synctex.gz"}
temp_folder_name = "latex_temp_files"

# Walk through all directories and subdirectories
for root, _, files in os.walk(repo_root):
    # Skip any existing latex_temp_files folders to prevent nested structures
    if temp_folder_name in root:
        continue

    files_to_move = [file for file in files if file.endswith(tuple(extensions))]

    if files_to_move:  # Only create the folder if there are files to move
        target_dir = os.path.join(root, temp_folder_name)
        
        # Create only one `latex_temp_files` folder per directory
        os.makedirs(target_dir, exist_ok=True)

        for file in files_to_move:
            source_path = os.path.join(root, file)
            destination_path = os.path.join(target_dir, file)
            
            shutil.move(source_path, destination_path)
            print(f"Moved: {source_path} -> {destination_path}")

print("Cleanup complete!")

