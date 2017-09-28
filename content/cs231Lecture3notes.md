Title: CS231n Lecture 3 Notes
Date: 2017-8-29 13:10
Category: CS231n
tags: cs231n, notes, python, neural networks


I have recently been making my way through the Stanford Master's in Computer Science 231n course. This particular lecture
was about defining a loss function for how a simple Linear Classifier performs at classifying categories during training time,
and this metric in a sense quantifies how "unhappy" our scores are across the training data.

The task then is to find a way to efficiently find parameters (Weights and Biases) that minimize and optimize the loss function, useually via some optimization algorithm like Gradient Descent.

### Loss Functions
1. Multiclass SVM Loss
2. Softmax Classifier (Cross-Entropy Loss / Multinomial Logistic Regression)


### *Multiclass SVM Loss*

 The average across all the differences of the scores between the correct class and incorrect classes with a constant of one added. 1/N * Sigma { ((Incorrect class score  - Correct class score) + 1)} . Using a value of one here is
arbitrary and really just determines what magnitude the weights can be.

Here when we initialize the weights, they are chosen to be small numbers, so in this case the initial value for the loss will be 2. Weight values can be multiplied in the same way, and they could be twice as large and achieve the same Loss (ignoring bias).

### *Softmax Loss*
Softmax Loss is a different functional form for how loss is specified across scores. This assumes that the scores are unormalized log probabilities for each class. To get probabilities for each class,
we take the exponentiated scores for each element divided by the sum of all exponentiated elements. So here we want to maximize the log likelihood, or for a loss function we want to
minimize the negative log likelihood of the correct class. It turns out that maximizing this is more mathematically conducive than maximizing the negative probabilities themselves.
For the example of classifying a cat, if the normalized probability of a cat class is .13 then the loss would be -log(.13)= .89, and we are trying to maximize this, where zero is the minimum and there is no bounded maximum.

When we initialize weights we typically choose them to be very small, so there should be an initial loss of -log( 1 / number of classes), as the initial scores would be zero, then unormalized probabilities of 1 for every class, then
the loss should be -log( 1 / # of classes ). As the model trains, the loss should move toward zero.

Optimization occurs by finding the gradient of the loss function with respect to certain parameters, usually the weights for each class. In practice an analytic gradient is used, which is an exact, fast, but error-prone method.
You often then do a gradient check, where you compare the numerical gradient which is usually approximate, slow, but easy to write compared to your analytic gradient.

### *Weight Regularization*

Weight regularization is a set of techniques to add objectives to the loss function, such that there exists a tradeoff between training error and generalization error. 
The most common form of regularization in neural networks is L2 regularization, also known as weight decay. This push$
Therefore regularization loss is a new component that contributes to the overall loss, and it is only a function of 
Including this weight regularization in the overall loss function that you are trying to minimize leads to weights that are diffuse, making sure that the network does not overfit certain regions of the image. This leads to better generalization performance at testing time.

### *Stochastic Gradient Descent*
This process is usually composed of two steps:
  1. Find the weights gradient by evaluating the gradient of the loss function with respect to the parameters of your training data, the weights. 
  2. Set new weights by multiplying step size (a.k.a. learning rate) by the gradient of the loss function with respect to weights, most importantly in the direction of the negative gradient. The gradient points in the direction of maximal increase, so the negative gradient will modify the parameters of the network closer to minimizing the loss function, or at least moving toward some local minimum.

The learning rate/step size is an important hyperparameter for this.

### *Mini-batch Gradient Descent*
Instead of using all training samples for each iteration (finding the gradient of the loss function corresponding to all your training data), you can use a small *batch* comprised of a small subset of your training data. Then you can get a good approximation of the gradient and use smaller step sizes rather than using a full-batch size for each iteration or epoch.
Often this isn't a very significant hyperparameter to tune, but rather you choose this based on your GPU architecture and the constraints of your memory.
The key is finding the appropriate learning rate to converge over time across epochs (full cycles through your training data).

The loss function can be thought of as an optimization problem in high-dimensional space, in which we are trying to reach the bottom of some high-dimensional valley. We start with some random initialization of weights and through iterative differentiation and adjustment we can reach the bottom. The next important concept to cover will be backprogation, essentially how to compute the gradient analytically by using the chain rule. 


The advancements recently (since roughly 2012) of using these techniques for neural networks are that you do not have to hand-craft features regarding your images, but rather you can train your entire network and the network automatically learns feature
without explicitly being programmed the structure of features or objects, like most rule-based recognition systems of the past were. Here the networks can be trained all the way back to the raw pixels, which make them very powerful and flexible at solving a wide array of problems in sound, image, and pattern recognition.


Until next time,
#### Clayton Blythe | *Deep Python*
