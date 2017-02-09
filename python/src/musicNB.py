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
template = parseFile("template.txt")
x = re.findall("(?<=music {)[^;]+(?=;)", s)

div = [ re.sub("ID", str(i), "<div id='music-ID'></div>") \
        for i in xrange(len(x)) ]

js = [ "ABCJS.renderABC('music-" +str(i)+ "','" +str(x[i])+ "');" \
       for i in xrange(len(x)) ]

js_all = "".join(js)

content = s
i = 0
while 
re.findall("(?<=music {)[^;]+(?=;)", content)


re.sub("%js_all", js_all, template)
