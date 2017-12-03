#!/usr/bin/python3

# cleanup.py - cleans up (at least in this revision) your desktop by filetype.
"""Imports os for os operations, shutil to move files"""
import sys
import os
import shutil

RUNNING = True

if sys.platform == 'win32':
    DESKTOPDIRECTORY = os.path.join(os.environ.get('USERPROFILE', 'Desktop'))
else:
    DESKTOPDIRECTORY = os.path.join(os.environ.get('HOME'), 'Desktop')


def cleanup():
    """Cleans up the desktop NEED TO ABSTRACT MORE"""
    os.chdir(DESKTOPDIRECTORY)
    desktopcontents = os.listdir()
    extarray = []

    findextensions(desktopcontents, extarray)

    # Make folder for extension(s)
    for extension in extarray:
        extension = extension.replace('.', '')
        os.makedirs(os.path.join(DESKTOPDIRECTORY, extension), exist_ok=True)
        for file in desktopcontents:
            if os.path.isfile(file):
                if extension in file:
                    if os.path.exists(DESKTOPDIRECTORY):
                        # extension = extension.replace('.', '')
                        shutil.move(
                            os.path.join(DESKTOPDIRECTORY, file),
                            os.path.join(DESKTOPDIRECTORY, extension))


def findextensions(desktopcontents, extarray):
    """Finding extension(s) on home directory"""
    for file in desktopcontents:
        ext = os.path.splitext(file)[1]
        if os.path.isfile(file):
            if sys.platform == 'win32':
                if '.lnk' not in file:
                    if ext not in extarray:
                        extarray.append(ext)
            if not file.startswith('.'):
                if ext not in extarray:
                    extarray.append(ext)


while RUNNING:
    print("Cleaning!")
    try:
        cleanup()
    except EnvironmentError as error:
        print("We\'ve ran into an error!")
        print(error)
        print("Cleaning done, but with errors. Please see above.")
    else:
        print("Cleaning Done!")
    # Changing a global 'constant'!? Find a better way.
    RUNNING = False

# ls = os.popen('ls ~/Desktop').read()
# regexFileExtensions = regex.compile(r"(\.\w{1,}$[^\d#~])", regex.MULTILINE)
# items = regexFileExtensions.findall(ls)
# itemSet = set(items)
