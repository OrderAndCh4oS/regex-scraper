import os
import re
import sys

if len(sys.argv) > 2:
    path = sys.argv[2]
else:
    path = os.path.dirname(os.path.realpath(__file__))

if os.listdir(path):
    directory = os.listdir(path)
    if len(sys.argv) > 3:
        saveFile = sys.argv[3]
    else:
        saveFile = os.path.basename(os.path.normpath(path)) + '.json'

    with open(saveFile, "w") as f:

        for item in directory:
            foundFile = os.path.join(path, item)
            if os.path.isfile(foundFile):
                file = os.path.join(path, item)
                html = open(file, "r")
                readfile = html.read()
                regex = re.compile(sys.argv[1], re.DOTALL)
                found = regex.findall(readfile)
                f.write("\n\n" + os.path.basename(html.name) + "\n=========================================\n\n")
                for match in found:
                    if isinstance(match, tuple):
                        for part in match:
                            f.write(part)
                    else:
                        f.write(match)
