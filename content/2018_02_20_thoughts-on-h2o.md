Title: Thoughts on H2O (The Machine Learning Platform)
Date: 2017-8-17 19:56
Category: Misc
tags: python, machine learning

## Thoughts on H2O Machine Learning Platform

This is a short write-up of my  experiences and thoughts using the H2O machine learning platform, 
made by H2O.ai. 

H2O is an in-memory platform for distributed, scalable machine learning. H2O uses familiar interfaces like R, Python, Scala, Java, JSON and the Flow 
notebook/web interface, and works seamlessly with big data technologies like Hadoop and Spark. H2O provides implementations of many popular algorithms such as GBM, Random Forest, 
Deep Neural Networks, Word2Vec and Stacked Ensembles.  H2O is extensible so that developers can add data transformations and custom algorithms of their choice and access them through all of those clients.  

Overall, I think that H2O is a great tool for quick prototyping and 
experimentation with different datasets and model families, particularly for the task of binary classification on relational data. 

### Usability
In my experience, the ramp-up time, usability, and minimal boilerplate code needed to run
machine learning experiments and test a variety of model types on varying relational datasets is where H2O's primary use lies. 
With the H2O Flow interface, those without specific knowledge of machine learning 
skills in Python, R, or SAS can easily ingest datasets from csv or parquet, and train from various model family types. 

### Cababilities
A dataset can easily be sampled, split, 
or have k-fold cross validation performed, all the while providing in-depth performance statistics like AUROC, F1, and other standard measures at various 
probability thresholds. 

Use of the distributed H2O machine learning capabilities can scale to large datasets with millions of rows, and can be used through API's for Python, R, and Scala. 
Models can be exported as Plain Old Java Objects (POJO's) for use in production, though I haven't experimented with this. 

H20.ai is also a member of the [GPU Open Analytics Initiative](http://gpuopenanalytics.com/#/), with a growing community of members like 
Apache Arrow, Anaconda, MapD, working to integrate all portions of the data science stack on GPU. 
From my research, it appears that MapD, Nvidia, Anaconda, and H2O.ai are working on creating a standardized GPU Dataframe 
as seen in [this PyGDF github repo.](https://github.com/gpuopenanalytics/pygdf)
This should alllow for faster training of machine learning models where possible, providing a NumPy-like Python API, all 
while using familiar environment management like conda. 
 
### Final Thoughts

I think that overall the H2O machine learning platform and API especially is a very useful tool to quickly experiment 
with different datasets and model families, particularly for the task of binary classification. I'm not convinced that it is mature yet for computer vision tasks like object detection or semantic segmentation. 

The primary use case would be quickly making a prototype gradient boosting or random forest model on large relational datasets that might not fit in memory. 
If one needs to quickly iterate and learn about the information value of the data, or quickly produce a result for a presentation, H2O fits that niche nicely. 


In addition 
 

Until next time,
