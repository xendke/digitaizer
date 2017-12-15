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
        self.width = 50
        self.bind_actions()

    def set_previous(self, x, y):
        self.previous_x = x
        self.previous_y = y

    def getPencil(self):
        return self

    def hovered(self, event):
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
        cnv = self.canvas

        cnv.bind("<B1-Motion>", self.draw) # Left Click Drag

        cnv.bind("<Motion>", self.hovered) # Hover
        cnv.bind("<Button-1>", self.hovered) # Left Click
        cnv.bind("<Enter>", self.hovered) # Mouse Entered

        cnv.bind("<Button-2>", cnv.save) # Right Click
        cnv.bind("<Leave>", cnv.clear) # Mouse Left

def main():
    master = tk.Tk()
    master.title("digitaizer")
    cnv = Canvas(master)
    cnv.pack()
    pn = Pen(cnv)

    while True:
        try:
            master.update_idletasks()
            master.update()
        except tk.TclError:
            print("done")
            break

if(__name__=="__main__"):
    main()
