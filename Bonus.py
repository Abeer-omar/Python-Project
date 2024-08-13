import shutil
import os
import imghdr

def transfer_images(source, destination):
    # if dest dir not exists make one
    if not os.path.exists(destination):
        os.makedirs(destination)
    
    for root, files in os.walk(source):
        for file in files:
            file_path = os.path.join(root, file)

            # file is image or not
            if imghdr.what(file_path) is not None:

                try:
                    shutil.copy(file_path, destination)
                    print(f"Copied {file} to {destination}")
                except Exception as e:
                    print(f"Error copying {file}: {e}")

source_directory = "F:\SrcFile"
destination_directory = "D:/ITI ICC/Data Engineering/03.1_Python/Project/PythonProject/img_destination"

transfer_images(source_directory, destination_directory)
