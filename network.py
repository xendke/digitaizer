import numpy as np

class Network():
    def __init__(self, layer_sizes):
        self.layer_sizes = layer_sizes # an array of integers. eg: [3, 4, 2] 3 Input Neurons, 4 Hidden Neurons, 2 Output Neurons
        self.num_layers = len(layer_sizes)

        self.biases = [np.random.randn(y, 1) for y in layer_sizes[1:]]
        """ example representation of biases for layer_sizes = [3,4,2]
        [np.random.randn(y, 1) for y in [4,2]]
        [
            [b, b, b, b], # first hidden layer biases
            [b, b] # output layer biases
        ] # b = different random numbers (normal distr.)
        """
        
        self.weights = [np.random.randn(y, x) for x, y in zip(layer_sizes[:-1], layer_sizes[1:])]
        """ example representation of weights for layer_sizes = [3,4,2]
        [np.random.randn(y, x) for x, y in zip([3,4], [4,2])]
        [
            [ # first hidden layer
                [w,w,w], # top most neuron's "incoming" weights
                [w,w,w], # etc
                [w,w,w],
                [w,w,w]
            ],
            [ # output layer
                [w,w,w,w],
                [w,w,w,w]
            ]
        ] # w = different random numbers (normal distr.)
        """
