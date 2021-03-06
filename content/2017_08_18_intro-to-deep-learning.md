Title: Deep Learning 101: A Brief Introduction
Date: 2017-8-18 22:19
Category: Deep Learning
tags: python, neural networks, intro

So you want to learn about Deep Learning huh?

Well I'm not sure I'm quite qualified yet, as I just started learning about this myself. But the best way to learn something is to try to teach it to other people, so here I am. I hope you find this post and blog useful.

To begin our understanding of this field, we need to introduce the topic of machine learning. [Machine Learning](https://www.wikiwand.com/en/Machine_learning) is the ability of a computer to aquire knowledge and make predictions through extracting latent patterns and information from data. Machine Learning can almost be thought of as a form of applied statistics, in which computers statistically estimate some function. Within machine learning, problems can usually be broken down into [supervised learning](https://www.wikiwand.com/en/Supervised_learning) and [unsupervised learning](https://www.wikiwand.com/en/Unsupervised_learning). The former infers or approximates some function from labeled training data, where the function represents a relationship between input variables (often called features) and a labeled or known output value. In unsupervised learning, the task is to describe the hidden structure and properties of input data without explicitly being given labeled training data. Within machine learning there is a subdomain called [Deep Learning](https://www.wikiwand.com/en/Deep_learning), and this area will be the primary focus of this blog, [*Deep Python*](https://deepython.com) @ [*deepython.com*](http://deepython.com).

A couple fundamental concepts in deep learning are Artificial Neural Networks and Convolutional Neural Networks.


## Key concepts:
### 1. Artificial Neural Networks
### 2. Convolutional Recurrent Neural Networks (CNNs)



[Artificial Neural Networks](https://www.wikiwand.com/en/Artificial_neural_network) are systems created by modern computing systems created to complete complex tasks such as image and sound recognition. They were inspired by traditional biological networks, which are adept at completing complex tasks like recognizing faces, understanding audible speech, or translating one written language into another. The important thing is that these tasks are extremely difficult to formalize into traditional rule-based systems, and hence these problems have seen large progress through the development of neural networks.  

This is the most promising and conceptually difficult area of machine learning, as it requires employing linear algebra along with modern GPU architecture to create a complex network of connected neurons which allow computers to learn complex patterns from experiences, and to solve problems through breaking tasks down into simpler, more manageable components. This is done by stacking several "layers" of mathematical operations and transformations on top of one another, hence the field's buzzword
*Deep Learning* and the name of my blog *Deep Python* @ [*deepython.com*](http://deepython.com)

[Convolutional Neural Networks](https://www.wikiwand.com/en/Convolutional_neural_network) then are an extension of Artificial Neural Networks, which use a variation of [multi-layer perceptrons](https://www.wikiwand.com/en/Multilayer_perceptron) and require minimal preprocessing of the data. [Multi-layer perceptrons](https://www.wikiwand.com/en/Multilayer_perceptron) are mathematical expressions that map some set of input values to output values. As a whole, Convolutional Neural Networks usually have an input layer, several hidden layers, and an output layer. These layers can be convolutional, pooling, or fully connected as a traditional multi-layer perceptron network would be. As is standard, these networks employ [backpropagation](https://www.wikiwand.com/en/Backpropagation) to calculate the error each neuron contributes to the network's discriminatory ability, through calculating the [gradient](https://www.wikiwand.com/en/Gradient) of the loss function. A gradient can be though of as a mathematical operation that finds the direction of maximal increase (consequently the opposite direction is  used for minimization). Throughout these layers, there are parameters called biases and weights that represent the underlying mathematical operations of matrix multiplication. Then, these weights and biases are used to calculate some set of final values, often scores for different classes. These cores are then mapped to a loss function that represent's error in the network's discriminatory ability. 

The most commonly used loss function is the [cross entropy loss function](https://www.wikiwand.com/en/Loss_functions_for_classification#/Cross_entropy_loss). Then, an optimization algorithm such as [gradient descent](https://www.wikiwand.com/en/Gradient_descent) is used to modify weights and biases to iteratively move toward the minimum of the loss function at some previously defined learning rate.

## *Convolutional Neural Networks* (CNN's)

Convolutional Neural Networks have been found to greatly improve classification accuracy for [complex tasks](https://www.wikiwand.com/en/Convolutional_neural_network#/Applications) such as image classification, facial recognition, natural language processing, drug discovery, and are even beating humans at complex games such as Go. In fact, competing against humans in video games such as Starcraft and Dota2 is an active area of research in deep learning, as it requires a high number of dimensions to represent a game at a given instant.  

So the *deepness* in [*Deep Learning*](https://www.wikiwand.com/en/Deep_learning)  is a term that typically refers to neural networks that employ many layers of neurons like multi-layer peceptrons or [sigmoid neurons](https://www.wikiwand.com/en/Sigmoid_function) for feature extraction and learning. They take raw, base level information such as the brightness of individual pixels in an image, and add layers that progressively accumulate more complex information like edges, shapes, groups of shapes, and faces. Neural Networks employ these techniques to solve difficult and nebulous problems by breaking them down into a hierarchy of components that gradually increase in complexity. As mentioned previously, these networks are particularly useful in  [unsupervised learning](https://www.wikiwand.com/en/Unsupervised_learning), in which the representation of the data is learned from scratch by the network itself. This is an important emerging area of research, as the vast majority of data being produced in the world is unlabeled, such as the sentiment of reddit comments, or audio that does not have transcription available.

Overall, this is an exciting area that I am looking forward to learning more about, and this is just a high-level overview of the basics.

Until next time,
#### Clayton Blythe | *Deep Python*
