import tkinter as tk
import numpy as np

class Results():
    def __init__(self, master):
        self.primary_text = tk.StringVar() # placeholders
        self.secondary_text = tk.StringVar()
        self.default_text()

        self.primary = tk.Message(master, textvariable=self.primary_text, width=200, justify='left', font=("Helvetica", 20))
        self.primary.grid(row=0, column=2, rowspan=1, sticky=tk.N+tk.S)

        self.secondary = tk.Message(master, textvariable=self.secondary_text, justify='left')
        self.secondary.grid(row=1, column=2, rowspan=1, sticky=tk.W+tk.E+tk.N+tk.S)

    def default_text(self):
        """ set placeholder values to the label widgets """
        self.primary_text.set("Prediction: N/A")
        self.secondary_text.set("Confidence: \n0 : N/A \n1 : N/A \n2 : N/A \n3 : N/A \n4 : N/A \n5 : N/A \n6 : N/A \n7 : N/A \n8 : N/A \n9 : N/A")

    def update(self, predictions):
        """ replace placeholders with results from prediction"""
        predictions = predictions.T[0]  # transpose
        prediction = np.argmax(predictions)  # get index of max value of all predictions is the network response
        self.primary_text.set("Prediction: " + str(prediction))

        # construct dictionary where indexes are keys and the confidence results are values and then sort them as pairs
        predictions_unsorted = {index : value for index, value in zip( range(0, len(predictions)) , predictions )}
        predictions_sorted = sorted(predictions_unsorted.items(), key=lambda x: x[1], reverse=True)

        t = "Confidence: \n"
        i = 0
        spacer = "\n\n"
        for pair in predictions_sorted:  # pair is tuple where pair[0] is label and pair[1] is value
            if(i==9):
                spacer="\n"
            t += str(pair[0]) + " : " + str(round(pair[1] * 100, 4)) + "%" + spacer  # convert to percent and round
            # the rounding will show some results to be 0% even though they are just really small floats
            i+=1
        self.secondary_text.set(t)
