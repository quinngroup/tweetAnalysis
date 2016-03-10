from shutil import copy
import os

# To list all the files which have more than 100 lines
# find ALLIN  -name "*.csv" -type f -exec sh -c 'test `wc -l {} | cut -f1 -d" "` -gt "100"' \; -print | tee abc
# get the current path
path = os.getcwd()

# prepare the destination path
dest = path + "/FILTERED/"

# open the file
files = open('abc')

# copy files one by one from source to destination
for src in files:
    src = src.strip()
    copy(src,dest)

#copyfile(src, dst)
