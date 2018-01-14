""" Canvas Widget """
import tkinter as tk
from PIL import ImageGrab, ImageFilter

class Canvas(tk.Canvas):
    def __init__(self, master, w=400, h=400):
        self.border_w = 5
        super().__init__(master,width=w, height=h, background="white", cursor="circle", bd=self.border_w, relief="ridge",highlightthickness=0)
        self.width = w
        self.height = h
        self.file_name = "canvas.ps" # name of the screenshot file that self.save uses
        self.create_text(self.width/2, self.height/2, text="Write Your Digit Here", anchor="center")
        self.isNew = True
        Pen(self) # used draw on canvas

    def clear(self, event=None):
        print("clearing")
        self.delete(tk.ALL) # deletes all items on the canvas

    def grab(self):
        """ get current pixel data from canvas and save image to file"""
        x = self.winfo_rootx()
        y = self.winfo_rooty()
        offset = self.border_w # needed because of the canvas' border
        canvas_image = (ImageGrab.grab((x+offset,y+offset,x+self.width+offset,y+self.height+offset))
                        .filter(ImageFilter.GaussianBlur(radius=2))
                        .convert('L') # grayscale
                        .resize((28,28)))
        canvas_image.save('in.png')
        pixel_data = canvas_image.getdata()
        return list(pixel_data)

    def center_drawing(self):
        """ TODO: find center of mass and center drawing """
        pass

class Pen():
    def __init__(self, canvas):
        self.previous_x = 0
        self.previous_y = 0
        self.canvas = canvas
        self.color = "black"
        self.width = 25
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
        if(self.canvas.isNew): # clear the initial text prompt
            self.canvas.clear()
            self.canvas.isNew = False
        self.canvas.create_line(event.x, event.y, self.previous_x, self.previous_y, fill=self.color, width=self.width+1)
        self.canvas.create_oval(event.x-offset, event.y-offset, event.x+offset, event.y+offset, fill=self.color)
        self.set_previous(event.x, event.y)

    def bind_actions(self):
        cnv = self.canvas
        cnv.bind("<B1-Motion>", self.draw) # left click drag

        cnv.bind("<Motion>", self.hovered) # hover
        cnv.bind("<Button-1>", self.hovered) # single left click, this helps reset coordinates when having left canvas
        cnv.bind("<Enter>", self.hovered) # mouse Entered the canvas
