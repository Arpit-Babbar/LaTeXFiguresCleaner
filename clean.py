# small script that deletes unused graphic files in a latex project.
# specify graphic directory and logfile. Unused files will be deleted in specified directory.
# Originally from https://github.com/sbmueller/LaTeXFiguresCleaner

import os
import argparse
from os.path import join, isdir

parser = argparse.ArgumentParser()
parser.add_argument("-dir", type = str, required = True)
parser.add_argument("-logfile", type = str, required = True)
args = parser.parse_args()

directory = args.dir
logfile = args.logfile
enc = 'utf-8' # For Overleaf, try 'Latin-1' if issues encountered...

def clean(dir):
    opened_file = open(logfile, encoding=enc).read()
    for filename in os.listdir(dir):
        if filename in opened_file:
            full_path = join(dir, filename)
            if isdir(full_path):
                print("Recurively going to ", full_path)
                clean(full_path) # Recursive cleanup
            print(filename + ' in use.')
        else:
            if os.path.isfile(os.path.join(dir, filename)):
                print(filename + ' not in use - deleting.')
                os.remove(os.path.join(dir, filename))
            else:
                print(filename + ' is a directory. Recursively cleaning...')

clean(directory)
