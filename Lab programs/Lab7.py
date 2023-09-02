#Develop a program for backing up a given folder (Folder in a current working directory) into a ZIP file by using relevant modules and suitable methods.
import os 
import zipfile 
def backup(source_folder, zip_filename): 
  if not os.path.exists(source_folder): 
    print (f"Error: Source folder '{source_folder}' does not exist.")
    return 
  zipf = zipfile.ZipFile(zip_filename, 'w') 
  for foldername, subfolders, filenames in os.walk (source_folder): 
    for filename in filenames: 
    file_path = os.path.join(foldername, filename) 
    zipf.write(file_path, os.path.relpath(file_path, source_folder)) 
    print(f"Zipping: {file_path}") 
  zipf.close() 
  print(f"Backup successful: '{source_folder}' has been backed up to '{zip_filename}.")
main_folder = input("Enter the name of the folder to backup : ")
zip_filename = f"{main_folder}"
backup(main_folder,zip_filename)
