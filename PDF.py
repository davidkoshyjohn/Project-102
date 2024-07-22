import os
import shutil

from_dir = "C:/Users/david/Downloads"
to_dir = "C:/Users/david/OneDrive/Desktop"

listOfFiles = os.listdir(from_dir)

for file_name in listOfFiles:
    name, extension = os.path.splitext(file_name)

    if extension == "":
        continue
    if extension == ".pdf":
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "Pdf"
        path3 = to_dir + '/' + "Pdf" + "/" + file_name

        if os.path.exists(path2):
            print(f"Moving {file_name}......")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print(f"Moving {file_name}......")
            shutil.move(path1,path3)