import os
import shutil

directory = os.path.join(os.path.expanduser("~"), "Downloads")

extentions = {

    ".jpg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".mp4": "Videos",
    ".pdf": "School",
    ".ppt": "School",
    ".doc": "School",
    ".txt": "School",
    ".xml": "School",
    ".pptx": "School",
    ".mcpack": "Codes and Games",
    ".zip": "Codes and Games",

}

for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)

    if os.path.join(file_path):
        extention = os.path.splitext(filename)[1].lower()

        if extention in extentions:
            folder_name = extentions[extention]

            folder_path = os.path.join(directory, folder_name)
            os.makedirs(folder_path, exist_ok=True)

            destination_path = os.path.join(folder_path, filename)
            shutil.move(file_path, destination_path)

            print(f"Moved {filename} to {folder_name} folder.")
        else:
            print(f"Skipped {filename}. Unknown file exist.")
    else:
        print(f"Skipped {filename}. It is a directory.")

    print (f"File organization completed.")
