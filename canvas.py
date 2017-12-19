""" Canvas Widget """
import tkinter as tk

class Canvas(tk.Canvas):
    def __init__(self, master, w=400, h=400):
        super().__init__(master,width=w, height=h, cursor="circle", bd=5, relief="ridge")
        self.width = w
        self.height = h
        self.file_name = "canvas.ps" # name of the screenshot file that self.save uses
        self.pn = Pen(self) # used draw on canvas
        # self.create_text(self.width/2, self.height/2, text="Write Here", anchor="center")

    def clear(self, event=None):
        print("clearing")
        self.delete(tk.ALL) # deletes all items on the canvas

    def save(self, event=None):
        """ save screenshot of the canvas stored as postscript file """
        print("saving")
        self.postscript(file=self.file_name, colormode="gray")

class Pen():
    def __init__(self, canvas):
        self.previous_x = 0
        self.previous_y = 0
        self.canvas = canvas
        self.color = "black"
        self.width = 50
        self.bind_actions()

    def set_previous(self, x, y):
        """ store old mouse coordinates, used for drawing straight lines """
        self.previous_x = x
        self.previous_y = y

    def hovered(self, event):
        self.set_previous(event.x, event.y)

    def draw(self, event):
        """ draw a line for straight brush strokes and a circle for rounded corners """
        offset = self.width/2
        self.canvas.create_line(event.x, event.y, self.previous_x, self.previous_y, fill=self.color, width=self.width+1)
        self.canvas.create_oval(event.x-offset, event.y-offset, event.x+offset, event.y+offset, fill=self.color)
        self.set_previous(event.x, event.y)

    def bind_actions(self):
        cnv = self.canvas
        cnv.bind("<B1-Motion>", self.draw) # left click drag

        cnv.bind("<Motion>", self.hovered) # hover
        cnv.bind("<Button-1>", self.hovered) # single left click, this helps reset coordinates when having left canvas
        cnv.bind("<Enter>", self.hovered) # mouse Entered the canvas
