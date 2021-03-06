import tkinter as tk
import canvas  # canvas wrapper widget
import predictions_ui
import network
import os
if os.name == 'nt':
    # if on Windows, disable highDPI scaling which ruins Pillow's ScreenGrab
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)


class App(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.title("digitaizer")
        try:
            self.iconbitmap(default="icon.ico")
        except tk.TclError:
            print("icon.ico not found")
        self.resizable(0, 0)  # prevent resizing
        self.after(250, self.center)  # center window after window has become visible

        self.net = network.Network([784, 30, 10])
        self.net.load_wb()  # load weights and biases for neural network form pkl file
        self.res = None  # results widget
        self.cnv = None  # canvas widget

        self.build_ui()
        # self.bind_actions()

    def build_ui(self):
        # using grid system to set the widgets in the window
        self.cnv = canvas.Canvas(self)
        self.cnv.grid(row=0, column=0, columnspan=2, rowspan=2)

        self.res = predictions_ui.Results(self)

        bl = tk.Button(self, text="Clear Canvas", command=self.clear_all)
        bl.grid(row=2, column=0)

        br = tk.Button(self, text="Predict Drawing", command=self.predict)
        br.grid(row=2, column=1)

    def predict(self):
        """ go through process of predicting the digit drawn """
        try:
            self.cnv.center_drawing()
            image_data = self.cnv.grab()
            self.cnv.has_been_predicted = True
        except ValueError:
            print("Empty canvas. Will not predict.")
            return
        predictions = self.net.predict(image_data)
        self.res.update(predictions)

    def center(self):
        """ center the window to the center of the screen """
        # for this to work correctly, reqwidth/height must have been set by tkinter, so we call this function after(250)
        x = (self.winfo_screenwidth() - self.winfo_reqwidth()) / 2
        y = (self.winfo_screenheight() - self.winfo_reqheight()) / 2
        self.geometry("+%d+%d" % (x, y))

    def clear_all(self):
        self.cnv.clear()
        self.res.clear_results()

    def bind_actions(self):
        """ right click anywhere on the app clears canvas and results """
        self.bind("<Button-2>", lambda ev: self.clear_all())


if __name__ == "__main__":  # only run main() if python executes main.py as its starting point: python main.py
    master = App(None)
    master.mainloop()
