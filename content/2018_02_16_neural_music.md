Title: Music Genre Classification Using Deep Learning 
Date: 2018-01-15 13:10
Category: Deep Learning 

A few months ago I worked on a project to apply convolutional neural networks and deep learning for the task of music genre classification. Similar to how Shazam can precisely determine genre class membership of songs from [Free Music Archive](http://freemusicarchive.org/).  

The dataset can be found [in this github repository](https://github.com/mdeff/fma) which provides 30 second samples of thousands of tracks. With my initial experimentation with 8,000 tracks of 8 different genres, I was able to classify songs correctly with ~50% accuracy using a very simple convolutional neural network based off the VGG network, a series of 3x3 convolutions with stride of 1, padding of 1, batch normalization, ReLU, and 2x2 max pooling, taking an image from 512x512 to a
softmax prediction of eight genres. Preprocessing of the 8,000 tracks was done to convert audio into melspectrograms using the librosa package in python. 

![Alt Test](https://deepython.com/images/lose_yourself_to_dance.png)

A spectrogram decomposes audio from the amplitude/time domain into the frequency domain, allowing for a pictoral and visual representation of a song! I extracted random samples of 5.94 seconds for each song, so it is a very short time to be able to determine music genre. Overall, I think that these are very promising results using such a simple architecture and training from scratch on a small portion of data.

Next steps would be to work with the larger datasets to improve learning ability, or try to use the first layers of a larger pretrained network and fine tune from there. 

If you're interested, take a look at [my code here](https://github.com/claytonblythe/neuralMusic/blob/master/notebooks/vgg.py) or look at [the github repo here.](https://github.com/claytonblythe/neuralMusic)

Until next time,
#### Clayton Blythe | *Deep Python*
