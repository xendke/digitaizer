try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

class Pen():
    def __init__(self, canvas):
        self.previous_x = 0
        self.previous_y = 0
        self.canvas = canvas
        self.color = "black"
        self.width = 20

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
        self.canvas.create_line(event.x, event.y, self.previous_x, self.previous_y, fill=self.color, width=self.width+self.width/5)
        self.canvas.create_oval(event.x-offset, event.y-offset, event.x+offset, event.y+offset, fill=self.color)
        # processing rounded corners mimic
        self.set_previous(event.x, event.y)

def clear(event):
    print("s")
    cnv.create_rectangle(0,0,400,400, fill="white", outline="white", width=5);

def save(event):
    print("saving")
    cnv.postscript(file="file_name.ps", colormode="gray")



master = tk.Tk()

cnv = tk.Canvas(master, width=400, height=400)
cnv.pack()
pn = Pen(cnv)

cnv.bind("<Motion>", pn.hovering)
cnv.bind("<FocusIn>", pn.hovering)
cnv.bind("<B1-Motion>", pn.draw)
# cnv.bind("<Button-1>", pn.draw)
cnv.bind("<Button-2>", save)
cnv.bind("<Leave>", clear)


while True:
    try:
        x = master.winfo_pointerx()
        y = master.winfo_pointery()
    except tk.TclError:
        print("done")
        break

    master.update_idletasks()
    master.update()
