Title: CS231n Lecture 4 Notes
Date: 2017-9-3 13:10
Category: CS231n 

The purpose of this lecture was to introduce the imporatance and basic functioning of an fundamental concept in neural networks, backprogation. In short, backpropagation is a method for computing the gradients of weights and biases through recursive application of the chain rule in multivariable calculus. 

Most of this section can be understood by reviewing the concept of computing derivatives through the chain rule. The name "backpropagation" is referring to how the chain rule is applied recursively backwards through the circuit and can be thought of as gates communicating to each other whether they want their outputs to increase or decrease, so as to make the final output value higher. 

The *forward pass* computes values from input to output, and the *backward pass* starts at the end and recursively applies the chain rule to compute the gradients. So the gradients can be thought of as flowing backwards through the circuit. 

So understanding backpropagation is mainly local, in that you only need the output value of the gate and the local gradient of its inputs with respect to its output value. Backpropagation can also be thought of as gates communicating with each other, whether they want their outputs to increase or decrease so as to make the final output value higher. 

The lecture then uses an example with the [sigmoid activation function](https://en.wikipedia.org/wiki/Activation_function)

Patterns in backward flow:
1. Add
2. Multiply
3. Maximum

The *add gate* always takes the gradient on its output and distributes it equally to all of its inputs, regardless of what thier values were during the forward pass. 

The *multiply gate* has local gradients as input values, and this is multiplied on its output during the chain rule.

The *max gate* routes the gradient, distributing the gradient to exactly one of its inputs. 

Summary: This section provided intuition for what the gradients mean, and how they flow backwards through the circuit, determining which parts of the circuit (weights and biases) shoudl increase or decrease to force the final output higher. It also discussed *staged computation* for implementing backpropagation. The idea is to break up your function into modules to derive local gradients and then chain them. The key is to decompose expressions into stages such that you can
differentiate each stage independently one step at a time. 

The next section will start discussion neural networks and how backpropagation allows for efficiently computing the gradients of the connections with respect to a loss function. 

Until next time,
#### Clayton Blythe | *Deep Python*
