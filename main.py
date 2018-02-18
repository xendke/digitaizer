import tkinter as tk
import canvas  # canvas wrapper widget
import predictions_ui
from network import Network


class App(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.title("digitaizer")
        self.resizable(0, 0)  # prevent resizing

        self.net = Network([784, 30, 10])
        self.net.load_wb()  # load weights and biases for neural network form pkl file
        self.res = None  # results widget
        self.cnv = None  # canvas widget

        self.build_ui()
        self.bind_actions()

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
        self.cnv.center_drawing()
        image_data = self.cnv.grab()
        predictions = self.net.predict(image_data)
        self.res.update(predictions)

    def clear_all(self):
        self.cnv.clear()
        self.res.clear_results()

    def bind_actions(self):
        """ right click anywhere on the app clears canvas and results """
        self.bind("<Button-2>", lambda ev: self.clear_all())


if __name__ == "__main__":  # only run main() if python executes main.py as its starting point: python main.py
    master = App(None)
    master.mainloop()
