import os
from shutil import make_archive

currentDirectory = os.getcwd()
folderTobeZipped =currentDirectory + "/" + "dpendency"
# Create object of ZipFile
make_archive("dependency", 'zip', folderTobeZipped)