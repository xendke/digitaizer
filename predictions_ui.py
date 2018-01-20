import tkinter as tk
import numpy as np

class Results():
    def __init__(self, master):
        self.primary_text = tk.StringVar() # placeholders
        self.secondary_text = tk.StringVar()
        self.default_text()

        self.primary = tk.Message(master, textvariable=self.primary_text, width=200, justify='left', font=("Helvetica", 20))
        self.primary.grid(row=0, column=2, rowspan=1)

        self.secondary = tk.Message(master, textvariable=self.secondary_text, justify='left')
        self.secondary.grid(row=1, column=2, rowspan=1)

    def default_text(self):
        self.primary_text.set("Prediction: N/A")
        self.secondary_text.set("Confidence: \n0 : N/A \n1 : N/A \n2 : N/A \n3 : N/A \n4 : N/A \n5 : N/A \n6 : N/A \n7 : N/A \n8 : N/A \n9 : N/A")

    def update(self, predictions):
        """ replace placeholders with results from prediction"""
        prediction = np.argmax(predictions) # max index of all predictions is the prediction
        self.primary_text.set("Prediction: " + str(prediction))

        t = "Confidence: \n"
        for i in range(0,10):
            t+=str(i) + " : " + str(round(predictions[i][0]*100, 4)) + "%" + "\n" # convert to percent and round
            # the rounding will show some results to be 0% even though they are just really small floats
        self.secondary_text.set(t)
