Title: CS231n: Lecture 3 Cliff Notes
Date: 2017-8-29 13:10
Category: CS231n Notes

## *CS231n*: Lecture 3 Notes


I have recently been making my way through the Stanford Computer Science 231n course. This particular lecture
was about defining a loss function for how the Linear Classifier performs across all of the training data,
and this in a sense quantifies how "unhappy" our scores are across the training data.

The task then is to find a way to efficiently find the parameters (Weights and Biases) that minimize and optimize the loss function via some optimization algorithm like Gradient Descent.

### Loss Functions
1. Multiclass SVM Loss
2. Softmax Classifier: (Cross-Entropy Loss / Multinomial Logistic Regression)


#### *Multiclass SVM Loss*:

 The average across all the differences of the scores between the correct class and incorrect classes with a constant of one added. 1/N * Sigma { ((Incorrect class score  - Correct class score) + 1)} . Using a value of one here is
arbitrary and really just determines what magnitude the weights can be.

Here when we initialize the weights, they are chosen to be small numbers, so in this case the initial value for the loss will be 2. W values can be multiplied and they could be twice as large and achieve the same Loss (ignoring bias).

#### *Weight Regularization*:

 A set of techniques to add objectives to the loss, to tradeoff between training error and generalization error. i.e. a trade off between bias and variance 
The most common form of regularization is L2 regularization, also known as weight decay. This pushes the weights to being smaller and more diffused across all pixels and features, which prevents overfitting, leading to better generalization performance.
Therefore regularization loss is a new component that contributes to the overall loss, and is only a function of the weights, not your dataset.
Including this weight regularization in the loss function that you are trying to minimize leads to weights that not only classify correctly but prefer diffuse weights, taking into account as much of the image as possible.

Why would we want more evenly spread weights? This allows for taking in more parts and features of the input image into account.

#### *Softmax Loss*:
Softmax Loss is a different functional form for how loss is specified across scores. This assumes that the scores are unormalized log probabilities for each class. To get probabilities for each class,
we take the exponentiated scores for each element divided by the sum of all exponentiated elements. So here we want to maximize the log likelihood, or for a loss function we want to
minimize the negative log likelihood of the correct class. It turns out that maximizing this is more mathematically conducive than maximizing the negative probabilities themselves.
For the example of classifying a cat, if the normalized probability of a cat class is .13 then the loss would be -log(.13)= .89, and we are trying to maximize this, where zero is the minimum and there is no bounded maximum.

When we initialize weights we typically choose them to be very small, so there should be an initial loss of -log( 1 / number of classes), as the initial scores would be zero, then unormalized probabilities of 1 for every class, then
the loss should be -log( 1 / # of classes ). As the model trains, the loss should move toward zero.

Optimization occurs by finding the gradient of the loss function with respect to certain parameters, usually the weights for each class. In practice an analytic gradient is used, which is an exact, fast, but error-prone method.
You often then do a gradient check, where you compare the numerical gradient which is usually approximate, slow, but easy to write compared to your analytic gradient.

#### *Stochastic Gradient Descent*:
This process is usually composed of two steps:
  1. Find the weights gradient by evaluating the gradient of the loss function with respect to data, weights
  2. Set new weights by multiplying step size (a.k.a. learning rate) by the gradient of the loss function with respect to weights, in the direction of the negative gradient. The gradient points in the direction of maximal increase, so the negative gradient will lead to minimizing the loss function, or at least moving toward some local or global minimum.

Your learning rate / step size are an important hyperparameter for this.

#### *Mini-batch Gradient Descent*:
Instead of using all training samples for each iteration (finding the gradient of the loss function corresponding to all your training data), you can use a small *batch* size comprised of a small subset of your training data. Then you can get a good approximation of the gradient and use smaller step sizes rather than using a full-batch size for each iteration or epoch.
Often this isn't a very significant hyperparameter to tune, but rather you choose this based on your GPU architecture and the constraints of your memory.
The key is finding the appropriate learning rate to converge over time across epochs (iterations).

Different optimization algorithms perform differently on different problems.

The advancements recently (since roughly 2012) of using neural networks are that you do not have to hand-craft features regarding your images, but rather you can train your entire network and feature
extraction without explicitly programming the structure of different features or objects into some rule-based recognition system. Here the networks can be trained all the way back to the raw pixels, which make them very powerful and flexible.

Until next time,
#### Clayton Blythe | *Deep Python*
