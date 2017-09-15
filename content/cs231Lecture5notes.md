Title: CS231n Lecture 5 Notes
Date: 2017-9-13 13:10
Category: CS231n 
tags: cs231n, python, notes, neural networks

The purpose of this lecture was to introduce neural networks, and it extends beyond linear classification and describes how the "wiggle" (non-linearity) of neural networks are generated. The calculation of a score formula s=Wx is extended to add a clamping function like max(0, W1x) where an arbitrary number of weight matrices W1, W2 etc can be learned with stochastic gradient descent by calculating local gradients through backpropagation and the chain rule. 

These weight parameters and matrices are learned through the training process. The sizes of these intermediate hidden vectors are hyperparameters that can be determined through grid searching. The lecture then discusses the concept of a forward-propagating neuron, in which each neuron performs a dot product of the input and its weights, adds a bias, and applies the non-linearity (like the sigmoid activation function). 

A single neuron can also be thought of as a linear classifier, either a binary softmax classifier or a binary support vector machine classifier if a max-margin hinge loss is added to the output.

### Activation Functions

#### Sigmoid

The sigmoid function has two major drawbacks. One is that the neuron's activation function saturates at 0 and 1, leading to a cradient at these regions that is almost zero. Therefore almost no signal will flow through the neuron to its weights. Therefore you must be careful when initializing weights. The other undesirable aspect is that sigmoid outputs are not zero centered. Neurons in later layers of the neural network will be receiving data that is not zero centered, and gradient
descent would be zig zagging. However, by using batches of data for updating the weights, this can be mitigated. 

#### Tanh

The tanh is usually preferred to the sigmoid nonlinearity, where the output is zero centered

#### ReLU

The rectified linear unit computes the max(0,x) function and is thresholded at zero. The advantages are that it has been found to greatly accelerate stochastic gradient descent. The ReLU can be implemented by just thresholding a matrix of activations at zero. However, ReLU units can be fragile and die. If the learning rate is set too high, a large gradient flowing through a ReLU neuron can cause the weights to update in such a way that the neuron will never activate on a datapoint
again. 

####Leaky ReLU 

This is an attempt to fix the dying ReLU problem, with mixed success.

Usually the ReLU is chosen, while monitoring the fraction of dead units in a network. 
Until next time,
#### Clayton Blythe | *Deep Python*
