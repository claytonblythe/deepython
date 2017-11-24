Title: a2dlearn Takeaways 
Date: 2017-11-18 13:10
Category: Deep Learning 
Status: draft





### Graham Neubig - Carenegie Mellon University


The last topic Graham talked about was efficiency tricks for speeding up GPU operations on GPU, specifically minibatching. In language processing, you group sentences into a mini batch. For all sentences, you take the first word from every sentence and feed those into your network one sentence at a time. 

Dynet was briefly introduced, a similar dynamic graph GPU tool for C++, Python, Scala/Java. Dynet is similar to Pytorch and chainer, allowing for more dynamic creation of graphs. He then showed an example of minibatched classification in the dynet framework. 
The automated minibatching that he demonstrated looked pretty slick. 




Until next time,
#### Clayton Blythe | *Deep Python*
