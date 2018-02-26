import tkinter as tk
import numpy as np
from utils import project_path


class Results(object):
    def __init__(self, master):
        self.primary_text = tk.StringVar()
        self.secondary_text = tk.StringVar()
        self.default_text()  # placeholders

        self.primary = tk.Message(master, textvariable=self.primary_text, width=200, justify='left', font=("Helvetica", 20))
        self.primary.grid(row=0, column=2, rowspan=1, sticky=tk.N+tk.S)

        self.secondary = tk.Message(master, textvariable=self.secondary_text, justify='left')
        self.secondary.grid(row=1, column=2, rowspan=1, sticky=tk.W+tk.E+tk.N+tk.S)

        # setting up label where  screenshot of input canvas will be placed
        input_img_file = tk.PhotoImage()
        self.input_img = tk.Label(master, image=input_img_file, width=50, height=50, bd=2, relief="groove")
        self.input_img.grid(row=2, column=2, rowspan=1, columnspan=1, ipadx=2, ipady=2)

    def default_text(self):
        """ set placeholder values to the label widgets """
        self.primary_text.set("Prediction: N/A")
        sec = "Confidence: "
        for i in range(0, 10):
            sec += "\n\n" + str(i) + " : N/A"
        self.secondary_text.set(sec)

    def clear_results(self):
        self.default_text()
        try:
            self.input_img.image.blank()
            self.input_img.image = None
        except AttributeError:
            # input_img was already clear, and image does not exist
            pass

    def update(self, predictions):
        """ replace placeholders with results from prediction"""
        # use latest image from screenshot and display it
        path = project_path()
        input_img_file = tk.PhotoImage(file=path+"in.gif")
        input_img_file = input_img_file.zoom(2, 2)  # resize image 2x
        self.input_img.configure(image=input_img_file)
        self.input_img.image = input_img_file

        # find top prediction
        predictions = predictions.T[0]  # transpose
        prediction = np.argmax(predictions)  # get index of max value of all predictions is the network response
        self.primary_text.set("Prediction: " + str(prediction))

        # construct dictionary where indexes are keys and the confidence results are values and then sort them as pairs
        predictions_unsorted = {index : value for index, value in zip( range(0, len(predictions)) , predictions )}
        predictions_sorted = sorted(predictions_unsorted.items(), key=lambda x: x[1], reverse=True)

        t = "Confidence:"
        spacer = "\n\n"
        for pair in predictions_sorted:  # pair is tuple where pair[0] is label and pair[1] is value
            t += spacer + str(pair[0]) + " : " + str(round(pair[1] * 100, 4)) + "%"  # convert to percent and round
            # the rounding will show some results to be 0% even though they are just really small floats
        self.secondary_text.set(t)
