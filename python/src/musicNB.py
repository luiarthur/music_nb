import re

# match #music-
reMusic = re.compile("#music-*")

def parseFile(path):
    f = open(path)
    fileContents = f.read()
    f.close()
    #
    return fileContents

# Test:

s = parseFile("../test/sample_abs.txt")
re.findall("(?<=music {)[^;]+(?=;)", s)

re.findall("music {[^;]+;", s)
re.findall("};", s)
