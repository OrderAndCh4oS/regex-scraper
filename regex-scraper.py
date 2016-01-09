import sys, re, os


path = sys.argv[1]
if os.listdir(path):
    directory = os.listdir(path)
    if sys.argv[3]:
        saveFile = sys.argv[3]
    else:
        saveFile = os.path.basename(os.path.normpath(path)) + '.txt'

    js = open(saveFile, "w")

    for item in directory:
        phpFile = os.path.join(path, item)
        if (os.path.isfile(phpFile)):
            file = os.path.join(path, item)
            html = open(file, "r")
            readfile = html.read()
            regex = re.compile(sys.argv[2], re.DOTALL)
            found = regex.findall(readfile);
            print >> js, "\n\n" + os.path.basename(html.name) +"\n=========================================\n\n"
            for item in found:
                if isinstance(item, tuple):
                    for part in item:
                        print >> js, part
                else:
                    print >> js, item

js.close()
