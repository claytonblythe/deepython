Title: Neural Style Transfer Selfies
Date: 2017-10-02 13:10
Category: Deep Learning

I recently have been trying to learn PyTorch, as it is becoming more popular for machine learning researchers because of its ability to represent complex neural network architectures in just a few lines of code. It also allows for dynamic definition of graphs, unlike its main competitor TensorFlow. This becomes very useful for working with Recurrent Neural Networks for example. 

For this post, I implement the Neural Style Transfer algorithm in [this paper](https://arxiv.org/abs/1508.06576) that takes a content image and a style image and returns a version of that content image with the appropriate "style". 

The main idea is that two distances are defined for the content and one for the style. The goal is to transform the image to minimize both the content distance with respect to the content image and vice versa for the style image. 

In the implementation described in the [PyTorch Documentation](http://pytorch.org/tutorials/advanced/neural_style_tutorial.html) a pretrained VGG convolutional neural network is used as a base starting point. The content distance is defined as the sum of all squared differences between the feature maps at each Lth layer of the content and produced images, for every ith element of that layer's feature map.

The style distance is more obscure, using a Gram produce of vectorized feature maps, representing the correlation between feature maps at some layer for both style and output images. The gradients for both distances/losses are calculated and summed together, and then backpropagation is done. 

For example, we can do style transfer of "Starry Night" onto a selfie of myself. 

![Alt Test]('http://deepython.com/images/starrynight.png')
![Alt Test]('http://deepython.com/images/headshot.png')
![Alt Test]('http://deepython/images/starryn_cw0.6.png')


Until next time,
#### Clayton Blythe | *Deep Python*
