# automation tool for auto file organizer
import os #for device drives
import shutil #works for files input output,organize
#path to organize
path_to_organize = ""
#define all file types
file_types = {
    "Images":[".jpg",".png",".jpeg",".gif",".bmp"],
    "Documents": [".pdf", ".docs", ".docx",".ppt",".pptx"],
    "videos": [],
    "Archives":[],
    "Music":[]
}
#load through my path where i need to organize and list them
for filename in os.listdir(path_to_organize):
    print(filename)
    file_path= os.path.join(path_to_organize, filename)
    print(file_path)
    #no need to use folders. so check first
    if os.path.isdir(file_path):
        continue

    #check for each file extension and then move to respective created folders
    moved = False
    for folder,extensions in file_types.items():
        if filename.lower().endswith(tuple(extensions)):
            folder_path = os.path.join(path_to_organize, folder)
            # if there is no folder then create
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)
            #move the files to folder
            shutil.move(file_path, folder_path)
            moved = True
            break

        if not moved:
            other_path = os.path.join(path_to_organize, "other_files")
            if not os.path.exists(other_path):
                os.mkdir(other_path)
            shutil.move(file_path, other_path)

    print("Files moved successfully")




