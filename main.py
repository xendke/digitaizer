try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

def draw(event):
    global oldx, oldy
    print("drawing", event.x, event.y)
    w.create_line(event.x, event.y, oldx, oldy, fill="black", width=10)
    w.create_oval(event.x-5, event.y-5, event.x+5, event.y+5, fill="black")
    # processing rounded corners mimic
    oldx = event.x
    oldy = event.y


def save(event):
    print("saving")
    w.postscript(file="file_name.ps", colormode="gray")

def old(event):
    global oldx, oldy
    oldx = event.x
    oldy = event.y

master = tk.Tk()

w = tk.Canvas(master, width=400, height=400)
w.pack()

oldx = 0
oldy = 0

# w.create_oval(0, 0, 10, 10)
# w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

# w.create_rectangle(50, 25, 150, 75, fill="blue")
w.bind("<Motion>", old)
w.bind("<B1-Motion>", draw)
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
