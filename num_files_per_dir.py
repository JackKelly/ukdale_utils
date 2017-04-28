from __future__ import print_function
import os

dir_to_num_files = {}

for dir_name, subdirs, filenames in os.walk('.'):
    if len(dir_name.split('/')) == 4:
           dir_to_num_files[dir_name] = len(filenames)


dirs = dir_to_num_files.keys()
dirs.sort()

for directory in dirs:
    print(directory, dir_to_num_files[directory])
