import os
import shutil

path_to_organise = r"D:\some_files"

file_types = {
   "Images":[".jpg",".png",".jpeg",".gif",".bmp"],
   "Documents":[".pdf",".doc",".docx",".ppt",".pptx"],
   "Videos":[".mp4",".mov",".avi",".wmv"],
   "Archives":[".zip",".tar",".tar.gz",".tar.bz"],
   "Music":[".mp3",".m4a",".flac"]
}

for filename in os.listdir(path_to_organise):
    print("Checking:", filename)
    file_path = os.path.join(path_to_organise, filename)

    if os.path.isdir(file_path):
        continue

    moved = False
    for folder, extensions in file_types.items():
        if filename.lower().endswith(tuple(extensions)):
            folder_path = os.path.join(path_to_organise, folder)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # Skip if file already exists
            if os.path.exists(os.path.join(folder_path, filename)):
                print(f"{filename} already exists in {folder}, skipping")
            else:
                shutil.move(file_path, folder_path)
                print(f"{filename} moved to {folder}")
            moved = True
            break

    # Move to "others_files" if not matched
    if not moved:
        others_path = os.path.join(path_to_organise, "other_files")
        if not os.path.exists(others_path):
            os.makedirs(others_path)

        if os.path.exists(os.path.join(others_path, filename)):
            print(f"{filename} already exists in others_files, skipping")
        else:
            shutil.move(file_path, others_path)
            print(f"{filename} moved to others_files")

print("All files processed successfully")
