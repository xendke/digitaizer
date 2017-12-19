import numpy as np # mathematical functions and vectors/matrices

class Network():
    def __init__(self, layer_sizes):
        self.layer_sizes = layer_sizes # an array of integers. eg: [3, 4, 2] 3 Input Neurons, 4 Hidden Neurons, 2 Output Neurons
        self.num_layers = len(layer_sizes)

        self.biases = [np.random.randn(y, 1) for y in layer_sizes[1:]] # TODO: find better random function to ease learning
        """ example representation of biases for layer_sizes = [3,4,2]
        [np.random.randn(y, 1) for y in [4,2]]
        [
            [ # first hidden layer biases
                [b],
                [b],
                [b],
                [b]
            ],
            [[b], [b]] # output layer biases
        ] # b = different random numbers (std. normal distr.)
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
        ] # w = different random numbers (std. normal distr.)
        """

    def predict(self, io):
        """ io is a numpy array of dimension (n,1) : [[x1], [x2], ..., [xn]]"""
        for b, w in zip(self.biases, self.weights):
            io = sigmoid(np.dot(w,io)+b)
        return io

def sigmoid(v):
    """ v is a Numpy array. the sigma function will be applied to each element in v. """
    return 1.0/(1.0+np.exp(-v))


if __name__ == '__main__':
    net = Network([3,4,2])
    print(net.predict([[0.00023],[0.22312],[0.763]]))
