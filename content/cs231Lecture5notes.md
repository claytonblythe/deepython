Title: CS231n Lecture 5 Notes
Date: 2017-9-13 13:10
Category: CS231n 
tags: cs231n, python, notes, neural networks

The purpose of this lecture was to introduce neural networks, and it extends beyond linear classification and describes how the "wiggle" (non-linearity) of neural networks are generated. The calculation of a score formula s=Wx is extended to add a clamping function like max(0, W1x) where an arbitrary number of weight matrices W1, W2 etc can be learned with stochastic gradient descent by calculating local gradients through backpropagation and the chain rule. 

These weight parameters and matrices are learned through the training process. The sizes of these intermediate hidden vectors are hyperparameters that can be determined through grid searching. The lecture then discusses the concept of a forward-propagating neuron, in which each neuron performs a dot product of the input and its weights, adds a bias, and applies the non-linearity (like the sigmoid activation function). 

A single neuron can also be thought of as a linear classifier, either a binary softmax classifier or a binary support vector machine classifier if a max-margin hinge loss is added to the output.

### Activation Functions

#### **Sigmoid**

The sigmoid function has two major drawbacks. One is that the neuron's activation function saturates at 0 and 1, leading to a cradient at these regions that is almost zero. Therefore almost no signal will flow through the neuron to its weights. Therefore you must be careful when initializing weights. The other undesirable aspect is that sigmoid outputs are not zero centered. Neurons in later layers of the neural network will be receiving data that is not zero centered, and gradient
descent would be zig zagging. However, by using batches of data for updating the weights, this can be mitigated. 

#### **Tanh**

The tanh is usually preferred to the sigmoid nonlinearity, where the output is zero centered

#### **ReLU**

The rectified linear unit computes the max(0,x) function and is thresholded at zero. The advantages are that it has been found to greatly accelerate stochastic gradient descent. The ReLU can be implemented by just thresholding a matrix of activations at zero. However, ReLU units can be fragile and die. If the learning rate is set too high, a large gradient flowing through a ReLU neuron can cause the weights to update in such a way that the neuron will never activate on a datapoint
again. 

#### **Leaky ReLU** 

This is an attempt to fix the dying ReLU problem, with mixed success.

Usually the ReLU is chosen, while monitoring the fraction of dead units in a network. 

### Neural Network Architecture

Neural networks can be modeled as collections of neurons that are connected in a acyclic graph, where the outputs of some neurons become the inputs of other neurons. No cycles are allowed, and the neurons are organized into layers, commonly fully connected ones. The output layer is often the number of categories for the desired prediction, two for binary classifcation or ten for the ten categories in the CIFAR-10 dataset for example. They also usually do not have an activation
function, as the values are mean to be interpreted as scores for classification or some value for regression. The input layer is usually not counted, so logistic regression or support vector machines can be thought of as a single-layer neural network, where the inputs map directly to the outputs. Overall, these networks are interchangeably referred to as
*Artificial Neural Networks* and *Multi-Layer Perceptrons*, and besides being inspired by biological neurons, they don't have much in common. 

Two common metrics for describing neural network architecture are the size (number of neurons) or the number of parameters. Modern Convolutional Networks contain hundreds of millions of parameters and are often ten to twenty layers deep. 

This allows for nicely organized architectures, where each layer's weights and biases can be stored in matrixes, and the activations of all neurons in a particular layer can be calculated by using the dot product. A full forward pass of a three layer network is three matrix multiplications, with an activation function being used. All three weight matrices and all three bias matrices are then learnable parameters of the network. Entire batches of training data can be evaluated in
parallel then as well, by expanding the the dot product to use multiple input column vectors. The forward pass of a fully-connected layer uses one matrix multiplication followed with a bias offset and activation function. 

It can be mathematically shown that any continuous function can be modeled in this way with a neural network of at least one hidden layer. Neural networks work well because they can describe complicated functions in a compact and efficient manner, through the use of linear algebra, optimization through gradient descent, and hyperparameter tuning.

Despite the fact that adding more layers allows for approximating higher dimension functions more accurately, it also leads to a greater chance of overfitting and lower generalization accuracy. Overall, the regularization strength parameter is the preferred way to control this overfitting. 

### Summary
* Different activation functions were described, with ReLU being the most common choice
* Neural Networks with fully connected layers were described, with outputs from one layer mapping to the next layer
* This architecture enables efficient evaluation of neural networks through matrix multiplicaiton, stochastic gradient descent, and using an activation function.
* Neural networks are universal function approximaters, though can be prone to overfitting if proper precautions (some form of regularization) are not considered


Until next time,
#### Clayton Blythe | *Deep Python*

