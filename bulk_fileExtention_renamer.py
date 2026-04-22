import os
from pathlib import Path

print("\n\n------------------BUILK FILE EXTENSTION RENAMER------------------\n\n")



while True:
    folder_path = Path(input("Enter the folder path: ").strip())

    if not os.path.exists(folder_path):
        print(f"The folder path {folder_path} does not exists. Try again. ")
        continue 

    files = [f for f in folder_path.iterdir() if f.is_file()]
    if not files:
        print("The folder is empty. ")
        exit()
    
    for file in files:
        if file.suffix == '.txt':
            new_file = file.with_suffix('.md')
            file.rename(new_file)
            print(f"Renamed {file} to {new_file}")
    
    print("Renaming completed.....")


    user_choice = input("Do you want to continue again?(y/n): ").strip().lower()


    if user_choice != "y":
        print(f"You pressed {user_choice}.\nExiting the program....")
        break
