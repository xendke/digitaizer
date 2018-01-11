from mnist import MNIST # loading mnist data https://github.com/sorki/python-mnist/
import numpy as np # mathematical functions and vectors/matrices

_mndata = None

def get_training():
    global _mndata
    if(_mndata == None):
        _mndata = MNIST('./mnist_data')
    images, labels = _mndata.load_training() # example data: image [0,156,255,..., 0], label 4
    training_data = []
    for i, j in zip(images, labels): # ready data for network.
        i = np.array(i, dtype='f')/255 # change pixel value range from ints {0-255} to floats {0..1}
        im = np.array(i)[np.newaxis].T # transpose from [0, 0, 0.24, ... 0] to [[0], [0], [0.24], .. [0]]

        lb = np.zeros(10) # change structure from single int to array. example:  5 to [0,0,0,0,0,1,0,0,0]
        lb[j] = 1
        lb = lb[np.newaxis].T

        training_data.append((im,lb))
    return training_data

def get_testing():
    global _mndata
    if(_mndata == None):
        _mndata = MNIST('./mnist_data')
    images, labels = _mndata.load_testing()
    test_data = []
    for i, j in zip(images, labels): # ready data for network. pixels: floats {0..1}
        i = np.array(i, dtype='f')/255
        im = np.array(i)[np.newaxis].T # transpose from [0, 0, 0.24, ... 0] to [[0], [0], [0.24], .. [0]]
        # since network predicting does not need labels, we keep the label as int{0-9} for use later
        test_data.append((im,j))
    return test_data
