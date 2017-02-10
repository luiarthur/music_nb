#!/usr/bin/env python

import time 
import sys, os, shutil

# Watchdog for tracking file changes
from watchdog.observers import Observer  
from watchdog.events import PatternMatchingEventHandler

# SimpleHTTPServer
import SimpleHTTPServer
import SocketServer

# Musify
import Musify

MUSICNB_HOME = os.environ["MUSICNB_HOME"]
HTML_DIR = ".html/"

# SimpleHTTPServer
PORT = 2357
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)

class MusicNBHandler(PatternMatchingEventHandler):
    patterns = ["*.mnb"]

    def process(self, event):
        """
        event.event_type 
            'modified' | 'created' | 'moved' | 'deleted'
        event.is_directory
            True | False
        event.src_path
            path/to/observed/file
        """
        print event.src_path, event.event_type

    #def on_modified(self, event):
    #    self.process(event)

    def on_created(self, event):
        f = os.path.basename(event.src_path)
        f_base = os.path.splitext(f)[0]
        Musify.musify(event.src_path, HTML_DIR + f_base + ".html")
        self.process(event)

    def on_deleted(self, event):
        f = os.path.basename(event.src_path)
        f_base = os.path.splitext(f)[0]
        os.remove(HTML_DIR + f_base + ".html")
        self.process(event)


if __name__ == '__main__':
    args = sys.argv[1:]
    
    # Create html
    if os.path.exists(HTML_DIR):
        print "Found '.html/'"

    else:
        os.mkdir(HTML_DIR)

        for d in ["css/","js/"]:
            os.mkdir(HTML_DIR + d)

            for f in os.listdir(MUSICNB_HOME + d):
                shutil.copyfile(MUSICNB_HOME + d + f, HTML_DIR + d + f)

        if os.path.exists("_notes/"):

            for nb in os.listdir("_notes/"):
                f = os.path.basename(nb)
                f_base = os.path.splitext(f)[0]
                Musify.musify("_notes/" + nb, HTML_DIR + f_base + ".html")

        else:
            os.mkdir("_notes/")
            shutil.copyfile(MUSICNB_HOME + "_notes/sample_abc.mnb", \
                            HTML_DIR + "_notes/sample_abc.mnb")


        print "Created '.html/'"

    # Start Observer
    observer = Observer()
    observer.schedule(MusicNBHandler(), path=args[0] if args else '.', recursive=True)
    observer.start()

    # Start server
    print "serving at port", PORT
    httpd.serve_forever()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
