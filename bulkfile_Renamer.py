import os
from pathlib import Path

print("\n\n------------------BUILK FILE RENAMER------------------\n\n")



while True:
    folder_path = Path(input("Enter the folder path: ").strip())

    if not os.path.exists(folder_path):
        print(f"The folder path {folder_path} does not exists. Try again. ")
        continue 

    files = [f for f in folder_path.iterdir() if f.is_file()]
    if not files:
        print("The folder is empty. ")
        exit()
    
    prefix = "asmita"
    for index,file in enumerate(files,start=1):
        extension = file.suffix #to extract suffix of the file like .jpg,.png,etc
        new_name = f"{prefix}_{index}{extension}"

        #create entirely new path
        new_file = folder_path / new_name 

        if new_file.exists():
            print(f"Skipping {new_file}. Already exists...")
            continue

        file.rename(new_file)

        print(f"{file} renamed to {new_file}")
    
    print("Renaming completed.....")


    user_choice = input("Do you want to continue again?(y/n): ").strip().lower()


    if user_choice != "y":
        print(f"You pressed {user_choice}.\nExiting the program....")
        break
