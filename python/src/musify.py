#!/usr/bin/env python

import re
import sys

def readFile(path):
    f = open(path)
    fileContents = f.read()
    f.close()
    #
    return fileContents

def writeFile(path, contents):
    f = open(path, 'w')
    f.write(r'' + contents)
    f.close()

def html_template():
    return """ <!DOCTYPE HTML>
<html>

<head>
    <script src="/js/jquery.min.js" type="text/javascript"></script>
    <link href="/css/bootstrap.min.css" rel="stylesheet" type="text/css">
    <script src="/js/bootstrap.min.js" type="text/javascript"></script>
    <script src="/js/abcjs_basic_3.0-min.js" type="text/javascript"></script>
</head>

<body>
<header class="intro-header" style="background-color:grey; height:60px; margin:0; padding: 50;">
</header>

<div class="container">
    <div class="row">
        <div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">
            <br>
            %content
            <br>
        </div>
    </div>
</div>
</body>

<script type="text/javascript"> 
    %js_all 
</script>
</html>"""

# Test:

def musify(readPath, writePath):
    content = readFile(readPath)
    content = re.sub("music\s*{","music {",content)
    template = html_template()
    x = re.findall("(?<=music {)[^;]+(?=;)", content)
    #          
    div = [ "<div id='music-ID'></div>".replace("ID",str(i)) \
            for i in xrange(len(x)) ]
    #
    js = [ "ABCJS.renderAbc('music-" + str(i) + "',"  + repr(x[i])+ ");" \
           for i in xrange(len(x)) ]
    #
    js_all = "".join(js)
    #
    template = template.replace("%js_all", js_all)
    #
    y = re.findall("music {[^;]+;", content)
    #
    for i in xrange(len(y)):
        content = content.replace(y[i], div[i])
    #
    html = template.replace("%content", content)
    #
    # Substitute all #, ##, ###, #### for <h1>, <h2>, etc.
    headers = re.findall("\n\s*#+.+", html)
    for i in xrange(len(headers)):
        h = headers[i]
        h_level = h.count("#")
        h_open_tag = "\n<h" + str(h_level) + ">"
        h_close_tag = "</h" + str(h_level) + ">"
        html = html.replace(h, h_open_tag +h.replace("#","")+ h_close_tag)
    #
    writeFile(writePath, html)


musify(sys.argv[1], sys.argv[2])

# usage: ./musify ../../template/sample_abc.txt ../../template/out.html
