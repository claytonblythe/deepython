Title: Single-Shot Detector Prototype
Date: 2017-8-29 13:10
Category: Deep Learning 

I have wanted to experiment with multibox object detection and semantic segmentation in urban environments, so I started this very rough prototyping project for implementing SSD (Single-Shot Detector) in an urban environment, to detect things like pedestrians, bikes, cars, and buses. The SSD model is known for being fast at inference time and it performs object localization and classification in one pass. Also, I could readily find examples written in PyTorch on github [here](https://github.com/amdegroot/ssd.pytorch). I used this repository heavily, and
started my own project to run an SSD network on a [4k video](https://www.youtube.com/watch?v=Kk26RfjhFz0) of someone walking through Times Square in New York. I figured that it would be a good opportunity to experiment with these types of networks in a real-world environment. 

Here is an example of an image in Times Square to classify. You can see there are pictures of various people walking around, including a couple people in Elmo costumes! 
![Alt Test](http://deepython.com/images/elmo.png)

Here is the downsampled images preprocessed with subracted mean for SSD. This type of preprocessing is typical for these types of image processing tasks.
![Alt Test](http://deepython.com/images/condensed_rgb_elmo.png)

Here is the final result with bounding boxes and entity classification! I think it does a pretty darn good job at classification, even on the people in Elmo costumes.  
![Alt Test](http://deepython.com/images/elmo_boxed.png)

I think this was a fun prototype for me to get my feet wet a little bit. It is pretty slow even on GPU, as I am using a pretty verbose PyTorch script and using the PIL image library which adds a fair amount of overhead. 

Next, I plan on writing a python script to pipe frames from ffmpeg to create classification bounding boxes. I also plan on experimenting with more compact model architectures like SqueezeNet. [Here](https://github.com/claytonblythe/citywatch) is my Github repo if you want to take a look. 

Until next time,
#### Clayton Blythe | *Deep Python*
