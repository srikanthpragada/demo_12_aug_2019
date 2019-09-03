import os
import sys


def contains_string(filename, string):
    f = None
    try:
        f = open(filename, "rt")
        for line in f:
            if line.find(string) >= 0:
                return True
        else:
            return False
    except:
        return False
    finally:
        if f is not None:
            f.close()


if len(sys.argv) < 3:
    print("Usage: python search_files.py  startfolder searchstring")
    sys.exit(0)

start = sys.argv[1]  # starting path
string = sys.argv[2]  # search string

for (dname, dirs, files) in os.walk(start):
    for file in files:
        filename = dname + "\\" + file  # create absolute path
        if contains_string(filename, string):
            print(filename)
