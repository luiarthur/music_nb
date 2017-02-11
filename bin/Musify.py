import re
import os

MUSICNB_HOME = os.environ["MUSICNB_HOME"]

def readFile(path):
    f = open(path)
    fileContents = f.read()
    f.close()

    return fileContents

def writeFile(path, contents):
    f = open(path, 'w')
    f.write(r'' + contents)
    f.close()

def subBold(s):
    print "HERE!!!"
    m = re.findall("\*\*[^(**)]+\*\*", s)

    for i in xrange(len(m)):
        inner = m[i][2:len(m[i])-2]
        s = s.replace(m[i], "<b>" + inner + "</b>")

    return s

def musify(readPath, writePath):

    HTML_TEMPLATE = readFile(MUSICNB_HOME + "html/template.html")
    content = readFile(readPath)
    content = re.sub("music\s*{","music {",content)

    x = re.findall("(?<=music {)[^;]+(?=;)", content)

    div = [ "<div id='music-ID'></div>".replace("ID",str(i)) \
            for i in xrange(len(x)) ]

    js = [ "ABCJS.renderAbc('music-" + str(i) + "',"  + repr(x[i])+ ");" \
           for i in xrange(len(x)) ]

    js_all = "".join(js)

    template = HTML_TEMPLATE.replace("%js_all", js_all)

    y = re.findall("music {[^;]+;", content)

    for i in xrange(len(y)):
        content = content.replace(y[i], div[i])

    html = template.replace("%content", content)

    # Substitute all #, ##, ###, #### for <h1>, <h2>, etc.
    headers = re.findall("\n\s*#+.+", html)

    for i in xrange(len(headers)):
        h = headers[i]
        h_level = h.count("#")
        h_open_tag = "\n<h" + str(h_level) + ">"
        h_close_tag = "</h" + str(h_level) + "><br>"
        html = html.replace(h, h_open_tag + h.replace("#","") + h_close_tag)

    html = subBold(html)
    html = re.sub("\n\n\n+", "\n<br><br>\n", html)

    writeFile(writePath, html)
