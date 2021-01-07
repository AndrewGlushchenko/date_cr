#! /usr/bin/env python

# (C) Andrew Glushchenko.2020
# date_cr.py
# Data correctors

import os
import time
import argparse

version = "0.1"

wrongYear = 2076
wrongMonth = 11
wrongDay = 29
wrongYear2 = 1975
totalFileCount = 0

folder = "./"

def corrFileTime(fileName: str):
    global totalFileCount
    mtime = os.path.getmtime(fileName)
    fileMTime = time.localtime(mtime)

    if ((fileMTime.tm_year == wrongYear) and (fileMTime.tm_mon == wrongMonth) and (fileMTime.tm_mday == wrongDay)) \
            or (fileMTime.tm_year < wrongYear2):
        ctime = os.path.getctime(fileName)
        atime = os.path.getatime(fileName)
        print(fileName,"Worng date. Change date to ", time.ctime(ctime))
        os.utime(fileName,(atime,ctime))
        totalFileCount += 1
    pass
pass

def correctTimeFile(folder: str):
    for path, dirs, files in os.walk(folder):
        for fileN in files:
            fileWPath = os.path.join(path, fileN)
            corrFileTime(fileWPath)
        pass
    pass
pass

# __________main___________
#required=True,
def main():
    parser = argparse.ArgumentParser(prog  = 'date_cr',
                            usage='%(prog)s [options] \n With no arguments - walk all tree and corrected all files',
                            description='This script corrects date of files.')
    parser.add_argument('-f', action="store", dest="fileName",
                        help = "Specify file for correcting of date")
    parser.add_argument('--version', action="version",
                       help="Version number.", version = '%(prog)s {}'.format(version))
  #  parser.add_argument('', help="With no arguments - walk all tree and corrected all files")
    args = parser.parse_args()
    print(args.fileName)

    print('now is', time.strftime("%c"))

    if args.fileName == None:
        print("Top folder: ", folder)
        correctTimeFile(folder)
    else:
        print("Correcting date for file: ", args.fileName)
        corrFileTime(args.fileName)


    print("Corrected ", totalFileCount, " files.")
pass

if __name__ == '__main__':
    main()

#print('now is', time.strftime("%Y %d %h %H:%M"))
# print('now is', time.strftime("%c"))
#d = time.localtime()
#print(d)
#print("Top folder: ", folder)
#correctTimeFile(folder)
# corrFileTime(fileTestWPath)
# deleteEmptyFolders(folder)
#print("Corrected ", totalFileCount, " files.")

