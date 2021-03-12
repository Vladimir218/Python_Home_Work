import shutil
import os

project_directory = "my_project"
copy_directory = 'templates'

for root, dirs, files in os.walk(project_directory):
    if copy_directory in root and len(files) == 0:
        shutil.copytree(project_directory, copy_directory, dirs_exist_ok=True, copy_function=shutil.copy2)
