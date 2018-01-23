import tkinter as tk
import canvas # canvas wrapper widget
import predictions_ui
from network import Network
import numpy as np

def begin_prediction(net, canvas, res):
    canvas.center_drawing()
    image_data = canvas.grab()
    predictions = net.predict(image_data)
    res.update(predictions)

def clear_all(cnv, res):
    cnv.clear()
    res.default_text()

def main():
    net = Network([784, 30, 10])
    net.load_wb()

    master = tk.Tk() # window application
    master.title("digitaizer")

    # using grid system to set the widgets in the window
    cnv = canvas.Canvas(master)
    cnv.grid(row=0, column=0, columnspan=2, rowspan=2)

    res = predictions_ui.Results(master)

    bl = tk.Button(master, text="Clear Canvas", command=lambda: clear_all(cnv, res))
    bl.grid(row=2, column=0)

    br = tk.Button(master, text="Predict It", command=lambda: begin_prediction(net, cnv, res))
    br.grid(row=2, column=1)

    master.mainloop() # this does the same as below and it runs the app constantly refreshes it
    # while True:
    #     try:
    #         master.update_idletasks()
    #         master.update()
    #     except tk.TclError:
    #         print("done")
    #         break

if(__name__=="__main__"): # only run main() if python executes main.py as its starting point: python main.py
    main()
