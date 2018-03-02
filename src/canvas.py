""" Canvas Widget """
import tkinter as tk
import numpy as np
from utils import project_path
from PIL import ImageGrab, ImageFilter


class Canvas(tk.Canvas):
    def __init__(self, master, w=400, h=400):
        self.border_w = 5
        super().__init__(master,
                         width=w,
                         height=h,
                         background="white",
                         cursor="circle",
                         bd=self.border_w,
                         relief="ridge",
                         highlightthickness=0)
        self.width = w
        self.height = h
        self.file_name = "in.gif"  # name of the screenshot file that self.save uses
        self.create_text(self.width/2, self.height/2, text="Write Your Digit Here", anchor="center")
        self.is_new = True
        self.is_empty = True
        self.has_been_predicted = False  # True when the canvas drawing has been sent through the Neural Network
        self.delay_id = None  # holds the id of the delay started since the pen has been lifted from canvas
        Pen(self)  # used draw on canvas

    def clear(self):
        self.delete(tk.ALL)  # deletes all items on the canvas
        self.is_empty = True

    def grab(self):
        """ get current pixel data from canvas and save image to file"""
        if not self.is_empty:
            x = self.winfo_rootx()
            y = self.winfo_rooty()
            offset = self.border_w  # needed because of the canvas' border
            canvas_image = (ImageGrab.grab((x+offset, y+offset, x+self.width+offset, y+self.height+offset))
                            .filter(ImageFilter.GaussianBlur(radius=2))
                            .convert('L')  # greyscale
                            .resize((28, 28)))
            path = project_path("data", self.file_name)
            canvas_image.save(path)  # save canvas to a file (used by prediction UI)
            pixel_data = list(canvas_image.getdata())  # pixel_data is a list of the shade of each pixel: 255-white, 0-black
            # ready data for network eg: reverse pixel value, transform to float {0..1}, and transpose
            pixel_data = np.absolute(np.array(pixel_data)-255)/255
            pixel_data = pixel_data[np.newaxis].T
        else:
            raise ValueError('Canvas is empty.')

        return pixel_data

    def center_drawing(self):
        """ center drawing by calculating the center of mass https://stackoverflow.com/questions/37519238/"""
        if not self.is_empty:
            x = self.winfo_rootx()
            y = self.winfo_rooty()
            offset = self.border_w # needed because of the canvas' border
            canvas_image = ImageGrab.grab((x+offset,y+offset,x+self.width+offset,y+self.height+offset)).convert('L')
            immat = canvas_image.load()
            m = np.zeros((self.width, self.height))
            # calculate center of mass (cx, cy)
            for x in range(0, self.width):
                for y in range(0, self.height):
                    m[x, y] = immat[(x, y)] != 255
            m = m / np.sum(np.sum(m))
            # marginal distributions
            dx = np.sum(m, 1)
            dy = np.sum(m, 0)
            # expected values
            cx = np.sum(dx * np.arange(self.width))
            cy = np.sum(dy * np.arange(self.height))

            self.move(tk.ALL, (self.width/2)-cx, (self.height/2)-cy)  # use center of mass to center
            self.update()  # force the canvas to update immediately
        else:
            raise ValueError('Canvas is empty.')

    def predict_timeout(self):
        """ cancel old and set a new single timeout until prediction begins """
        if self.delay_id is not None:
            self.after_cancel(self.delay_id)
        self.delay_id = self.after(750, self.master.predict)  # 1.5 seconds


class Pen(object):
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
        self.canvas.predict_timeout()  # reset timeout

    def draw(self, event):
        """ draw a line for straight brush strokes and a circle for rounded corners """
        self.canvas.predict_timeout()  # reset timeout
        self.canvas.is_empty = False
        offset = self.width/2
        if self.canvas.is_new:  # clear the initial text prompt
            self.canvas.clear()
            self.canvas.is_new = False
        elif self.canvas.has_been_predicted:
            self.canvas.clear()
            self.canvas.has_been_predicted = False
        self.canvas.create_line(event.x, event.y, self.previous_x, self.previous_y, fill=self.color, width=self.width+1)
        self.canvas.create_oval(event.x-offset, event.y-offset, event.x+offset, event.y+offset, fill=self.color)
        self.set_previous(event.x, event.y)

    def bind_actions(self):
        cnv = self.canvas
        cnv.bind("<B1-Motion>", self.draw)  # left click drag

        cnv.bind("<Motion>", self.hovered)  # hover
        cnv.bind("<Button-1>", self.hovered)  # single left click, this helps reset coordinates when having left canvas
        cnv.bind("<Enter>", self.hovered)  # mouse Entered the canvas

        cnv.bind("<ButtonRelease-1>", lambda ev: cnv.predict_timeout())  # begin prediction process when mouse is lifted
