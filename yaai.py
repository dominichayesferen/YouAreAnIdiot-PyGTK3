#! /usr/bin/python3

import gi
import subprocess
import os
import sys
import time
import math
import random

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, GdkPixbuf, GLib, Gdk
from threading import Thread

class YAAI(object):

    def __init__(self):

        # build window
        w = Gtk.Window()
        w.set_title("You are an idiot!")
        w.set_default_size(357, 310)
        w.set_resizable(False)
        
        w.set_icon_name("html")
        
        pixbufanim = GdkPixbuf.PixbufAnimation.new_from_file("yaai/an.gif")

        mainimg = Gtk.Image()
        mainimg.set_from_animation(pixbufanim)

        w.add(mainimg)
        self.closeactivating = False
        w.connect('delete-event', self.close)
        w.show_all()
        
        self.w = w
        
        self.xOff = 5
        self.yOff = 5
        self.xPos = 400
        self.yPos = -100
        
        self.screen = Gdk.Screen.get_default()

    def close(self, p1 = None, p2 = None):
        
        if self.closeactivating == True:
            return True
        else:
            self.closeactivating = True
        
        self.w.set_title("Idiot!")
        
        Thread(target=self._close).start()
                
        return True
    
    def _close(self):
        time.sleep(0.1)
        GLib.idle_add(self.__close)
    
    def __close(self):
        
        if os.path.isfile("/usr/bin/zenity"):
            subprocess.Popen(["/usr/bin/zenity", "--warning", "--title=Microsoft Internet Explorer", "--text=You are an idiot!                    ", "--no-wrap"])
        
        subprocess.Popen([sys.executable, sys.argv[0]])
        time.sleep(0.01)
        subprocess.Popen([sys.executable, sys.argv[0]])
        time.sleep(0.02)
        subprocess.Popen([sys.executable, sys.argv[0]])
        time.sleep(2.3)
        
        self.w.set_title("You are an idiot!")
        
        self.closeactivating = False
        
    def _moosic(self):
        while True:
            while self.closeactivating == True:
                pass
            subprocess.Popen(["/usr/bin/ogg123", "yaai/you.ogg"]).wait()
        
    #moving code
    def newXlt(self):
        self.xOff = math.ceil(-6 * random.uniform(0, 1)) * 5 - 10
        GLib.idle_add(self.w.present)
    
    def newXrt(self):
        self.xOff = math.ceil(7 * random.uniform(0, 1)) * 5 - 10
    
    def newYup(self):
        self.yOff = math.ceil(-6 * random.uniform(0, 1)) * 5 - 10
    
    def newYdn(self):
        self.yOff = math.ceil(7 * random.uniform(0, 1)) * 5 - 10
    
    def playBall(self):
        time.sleep(0.1)
        if os.path.isfile("/usr/bin/ogg123"): #vorbis-tools
            Thread(target=self._moosic).start()
        
        
        while True:
            self.xPos += self.xOff
            self.yPos += self.yOff
            
            if self.xPos > (self.screen.get_width() - 357):
                self.newXlt()
                
            if self.xPos < 0:
                self.newXrt()
                
            if self.yPos > (self.screen.get_height() - 330):
                self.newYup()
                
            if self.yPos < 0:
                self.newYdn()
                
            GLib.idle_add(self.w.move, self.xPos, self.yPos)
            time.sleep(0.02)


    def run(self):
        Thread(target=self.playBall).start()
        Gtk.main()




if __name__ == "__main__":

    app = YAAI()
    app.run()
