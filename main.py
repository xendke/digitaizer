try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

class Canvas(tk.Canvas):
    def __init__(self, master, w=400, h=400):
        super().__init__(master,width=w, height=h)
        self.width = w
        self.height = h
        self.file_name = "canvas.ps"

    def clear(self, event):
        print("clearing")
        self.create_rectangle(0,0,400,400, fill="white", outline="white", width=5);

    def save(self, event):
        print("saving")
        self.postscript(file=self.file_name, colormode="gray")


class Pen():
    def __init__(self, canvas):
        self.previous_x = 0
        self.previous_y = 0
        self.canvas = canvas
        self.color = "black"
        self.width = 20
        self.bind_actions()

    def set_previous(self, x, y):
        self.previous_x = x
        self.previous_y = y

    def getPencil(self):
        return self

    def hovering(self, event):
        print("hovr", event.x)
        self.set_previous(event.x, event.y)

    def draw(self, event):
        """ """
        offset = self.width/2
        self.canvas.create_line(event.x, event.y, self.previous_x, self.previous_y, fill=self.color, width=self.width+1)
        self.canvas.create_oval(event.x-offset, event.y-offset, event.x+offset, event.y+offset, fill=self.color)
        # processing rounded corners mimic
        self.set_previous(event.x, event.y)

    def bind_actions(self):
        cnv.bind("<Motion>", self.hovering)
        cnv.bind("<FocusIn>", self.hovering)
        cnv.bind("<B1-Motion>", self.draw)
        # cnv.bind("<Button-1>", pn.draw)
        cnv.bind("<Button-2>", self.canvas.save)
        cnv.bind("<Leave>", self.canvas.clear)


master = tk.Tk()
cnv = Canvas(master)
cnv.pack()
pn = Pen(cnv)

while True:
    try:
        # x = master.winfo_pointerx()
        # y = master.winfo_pointery()
        pass
    except tk.TclError:
        print("done")
        break

    master.update_idletasks()
    master.update()
