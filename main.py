import tkinter as tk
from tkinter import messagebox
import canvas

def main():
    master = tk.Tk()
    master.title("digitaizer")

    cnv = canvas.Canvas(master)
    cnv.grid(row=0, column=0, columnspan=2)

    bl = tk.Button(master, text="Clear Canvas", command=cnv.clear)
    bl.grid(row=1, column=0)

    br = tk.Button(master, text="Predict It", command=cnv.save)
    br.grid(row=1, column=1)

    while True:
        try:
            master.update_idletasks()
            master.update()
        except tk.TclError:
            print("done")
            break

if(__name__=="__main__"):
    main()
