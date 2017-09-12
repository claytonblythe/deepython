Title: CS231n Lecture 4 Notes
Date: 2017-9-3 13:10
Category: CS231n 
tags: cs231n, python, notes, neural networks

The purpose of this lecture was to introduce the imporatance and basic functioning of an fundamental concept in neural networks, backprogation. In short, backpropagation is a method for computing the gradient of a loss function with respect to the weights and biases of a neural network. This is done through recursive application of the chain rule, that you might be familiar with from multivariable calculus. 

Most of this section can be understood by reviewing the concept of how local derivatives can be calculated through the chain rule by using the output at that point and nearby gradients. The name "backpropagation" refers to how the chain rule is applied recursively backwards (i.e. backpropagating) through the circuit and can be thought of as gates communicating to each other, telling each other whether they want their outputs to increase or decrease in the aim of making the final output value higher. 

So to reiterate, the *forward pass* computes values from input to output, and the *backward pass* starts at the end and recursively applies the chain rule to sequentially compute the gradients. As a result, the gradients can be thought of as flowing backwards through the circuit. 

The interesting behavior is that to understand and calculate backpropagation, you only need local characteristics of the circuit such as output value of the gate and the local gradient of the inputs of a node with respect to the output value of that node. 

The lecture then uses an example with the [sigmoid activation function](https://en.wikipedia.org/wiki/Activation_function)

Patterns in backward flow:
1. Add
2. Multiply
3. Maximum

The *add gate* always takes the gradient on its output and distributes it equally to all of its inputs, regardless of what the values were during the forward pass. 

The *multiply gate* has local gradients as input values, and this is multiplied on its output during the chain rule.

The *max gate* routes the gradient, distributing the gradient to exactly one of its inputs. 

Summary: This section provided intuition for what role gradients play in neural networks and how they relate to backpropagation. The section also how these gradients flow backwards through the "circuit", determining which parts components (weights and biases) should increase or decrease to force the final output higher. It also discussed the idea of *staged computation* for implementing backpropagation in an iterative fashion. The idea is to break up your function into modules to derive local gradients and then chain them. The key is to decompose expressions into stages such that you can
differentiate each stage independently, working through the circuit one step at a time. 

The next section will start discussion neural networks and how backpropagation allows for efficiently computing the gradients of the connections with respect to a loss function. 

Until next time,
#### Clayton Blythe | *Deep Python*
