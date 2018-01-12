import tkinter as tk
import canvas # canvas wrapper widget
from network import Network
import numpy as np

def begin_prediction(net, canvas):
    image_data = np.absolute(np.array(canvas.save())-255)/255
    image_data = image_data[np.newaxis].T
    # print(image_data)
    prediction = np.argmax(net.predict(image_data))
    print(prediction)

def main():
    net = Network([784, 30, 10])
    net.load_wb()

    master = tk.Tk() # window application
    master.title("digitaizer")

    # using grid system to set the widgets in the window
    cnv = canvas.Canvas(master)
    cnv.grid(row=0, column=0, columnspan=2)

    bl = tk.Button(master, text="Clear Canvas", command=cnv.clear)
    bl.grid(row=1, column=0)

    br = tk.Button(master, text="Predict It", command=lambda: begin_prediction(net, cnv))
    br.grid(row=1, column=1)

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
