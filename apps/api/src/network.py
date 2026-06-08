import numpy as np
import pickle as pkl
import os


def _weights_path():
    return os.path.join(os.path.dirname(__file__), "data", "wb_save.pkl")


def sigmoid(v):
    return 1.0 / (1.0 + np.exp(-v))


class Network:
    def __init__(self, layer_sizes):
        self.layer_sizes = layer_sizes
        self.num_layers = len(layer_sizes)
        self.biases = [np.random.randn(y, 1) for y in layer_sizes[1:]]
        self.weights = [np.random.randn(y, x) for x, y in zip(layer_sizes[:-1], layer_sizes[1:])]

    def predict(self, io):
        for b, w in zip(self.biases, self.weights):
            io = sigmoid(np.dot(w, io) + b)
        return io

    def load_wb(self):
        with open(_weights_path(), "rb") as f:
            self.weights, self.biases = pkl.load(f)
