try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

class Pencil():
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
        self.previous_x = event.x
        self.previous_y = event.y

    def draw(self, event):
        """ """
        offset = self.width/2
        self.canvas.create_line(event.x, event.y, self.previous_x, self.previous_y, fill=self.color, width=self.width+self.width/5)
        self.canvas.create_oval(event.x-offset, event.y-offset, event.x+offset, event.y+offset, fill=self.color)
        # processing rounded corners mimic
        self.set_previous(event.x, event.y)



def save(event):
    print("saving")
    w.postscript(file="file_name.ps", colormode="gray")



master = tk.Tk()

w = tk.Canvas(master, width=400, height=400)
w.pack()

pn = Pencil(w)
oldx = 0
oldy = 0

# w.create_oval(0, 0, 10, 10)
# w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

# w.create_rectangle(50, 25, 150, 75, fill="blue")
w.bind("<Motion>", pn.hovering)
w.bind("<B1-Motion>", pn.draw)
w.bind("<Button-2>", save)

while True:
    try:
        x = master.winfo_pointerx()
        y = master.winfo_pointery()
    except tk.TclError:
        print("done")
        break

    master.update_idletasks()
    master.update()
