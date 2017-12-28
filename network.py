# network based on Michael Nielsen's http://neuralnetworksanddeeplearning.com/
import numpy as np # mathematical functions and vectors/matrices

class Network():
    def __init__(self, layer_sizes, learning_config=[3.0, 10, 30]):
        self.layer_sizes = layer_sizes # an array of integers. eg: [3, 4, 2] 3 Input Neurons, 4 Hidden Neurons, 2 Output Neurons
        self.num_layers = len(layer_sizes)

        self.learning_rate, self.mini_batch_size, self.epochs = learning_config # Network hyperparameters

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
        """ feed input through network. io is a numpy array of dimension (self.layer_sizes[0],1) : [[x1], [x2], ...]"""
        for b, w in zip(self.biases, self.weights):
            io = sigmoid(np.dot(w,io)+b)
        return io

    def fit(self, training_data):
        """ train the network - training_data is set of tuples (x, y) where x is input(pixel data) and y is true output(label)"""
        size = len(training_data)
        for i in range(0, self.epochs):
            np.random.shuffle(training_data)
            mini_batches = [training_data[j:j+self.mini_batch_size] for j in range(0, size, self.mini_batch_size)]
            for mb in mini_batches:
                # gradients for C_x (cost function)
                nabla_b = [np.zeros(b.shape) for b in self.biases]
                nabla_w = [np.zeros(w.shape) for w in self.weights]
                for x, y in mb: # apply gradient descent using backpropagation to each mini batch
                    dnabla_b, dnabla_w = self.backprop(x, y) # TODO
                    nabla_b = [nb+dnb for nb, dnb in zip(nabla_b, dnabla_b)]
                    nabla_w = [nw+dnw for nw, dnw in zip(nabla_w, dnabla_w)]
                self.weights = [w-(self.learning_rate/len(mb))*nw for w, nw in zip(self.weights, nabla_w)]
                self.biases = [b-(self.learning_rate/len(mb))*nb for b, nb in zip(self.biases, nabla_b)]
            print("epoch end")
        return

def sigmoid(v):
    """ v is a Numpy array. the sigmoid function will be applied to each element in v. """
    return 1.0/(1.0+np.exp(-v))

def sigmoid_prime(v):
    """ derivative of the sigmoid function above."""
    return sigmoid(v)*(1-sigmoid(v))

if __name__ == '__main__':
    net = Network([784, 30, 10])
