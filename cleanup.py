
import os
import shutil
import re as regex

desktopDirectory = os.path.join(os.environ.get('HOME'), 'Desktop')

os.chdir(desktopDirectory)

desktopContents = os.listdir()

extArray = []

# Finding extension(s)
for file in desktopContents:
    ext = os.path.splitext(file)[1]
    if os.path.isfile(file) == True:
        if not file.startswith('.'):
            if ext not in extArray:
                extArray.append(ext)


# Make folder for extension(s)
for extension in extArray:
    extension = extension.replace('.', '')
    os.makedirs(os.path.join(desktopDirectory, extension), exist_ok=True)
    for file in desktopContents:
        if os.path.isfile(file) == True:
            if extension in file:
                if os.path.exists(desktopDirectory):
                    shutil.move(os.path.join(desktopDirectory, file),
                                os.path.join(desktopDirectory, extension))


# ls = os.popen('ls ~/Desktop').read()
# regexFileExtensions = regex.compile(r"(\.\w{1,}$[^\d#~])", regex.MULTILINE)
# items = regexFileExtensions.findall(ls)
# itemSet = set(items)
