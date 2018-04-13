# Digit*ai*zer
Numerical Digit Recognition Demo App (Using Neural Networks and Machine Learning)

![screenshot](https://i.imgur.com/7Kx7Sp3.png "Digitaizer 1.0")

## Prerequisites

* python v3
* numpy
* Pillow [link](https://github.com/python-pillow/Pillow)
* python-mnist [link](https://github.com/sorki/python-mnist) (needed only for re-training network)

## Installing Prerequisites
make sure python v3 is installed.  
make sure pip for python v3 is installed.  
(the command below might be pip3 or pip)
```
pip3 install Pillow
pip3 install numpy
```
### Linux Only Prerequisites
* pyscreenshot (PIL's ImageGrab support for Linux)
* scrot (backend to pyscreenshot)
```
pip3 install pyscreenshot
sudo apt-get install scrot
```

## Run
```
python3 main.py
```

## Todo
* option to not center image after live prediction
* ~~live predictions~~
* ~~center drawing before sending to network~~
* ~~show prediction results in the GUI~~
* ~~process canvas screenshot to match MNIST data format~~
* ~~implement NN~~
