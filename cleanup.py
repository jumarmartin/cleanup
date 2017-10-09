
import os
import re as regex

ls = os.popen('ls ~/Desktop').read()

regexFileExtensions = regex.compile(r"(\.\w{3,}$[^\d#~])", regex.MULTILINE)

items = regexFileExtensions.findall(ls)

itemSet = set(items)
