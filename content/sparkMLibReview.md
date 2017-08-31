Title: Spark MLlib Overview
Date: 2017-8-30 13:10
Category: Spark 

## *Spark MLib*: An Overview

This is an overview of the Spark MLlib framework, Spark's scalable machine learning library consisting of cmomon learning algorithms and utilities that include tools for classification, regression, clustering, collaborative filtering, dimensionality reduction, as well as underlying basic summary statistics. It also contains various utilities for doing linear algrebra, statistics, and general handling of data. MLlib uses the linear algebra package called Breeze, which depends on the netlib-java for optimized numerical processing. 

So in each area we have:

### Basic Statistics 
*Correlation* computes the correlation matrix for the input Dataset of vectors, and the output will be a DataFrame that contains the correlation matrix of the column of vectors. 

*Hypothesis Testing* is possible thorugh a ChiSquaretest to conduct a Pearson independence test for every feature against the label. For each feature, the feature label pairs are converted into a contingency matrix for which the Chi-squared statistic is computed. 


### ML Pipelines
Inspired by the scikit-learn project, MLlib standardizes APIs for machine learning algorithms to make it easier to combine multiple algorithms into a single pipeline or workflow. 

*DataFrame* ML API uses DataFrame form Spark SQL as an ML dataset, which can hold a variety of data types.

*Transformer* is an algorithm that can transform one DataFrame into another DataFrame (e.g. an ML model is a Transformer which transforms a DataFrame into a DataFrame with predictions). 

*Estimator* is an algorithm which can be fit on a DataFrame to produce a Transformer (this would be a learning algorithm which produces a model)

*Pipeline* chains multiple Transformers and Estimators together for a ML workflow.

### Feature Selection & Transformation

*TF-IDF* (Term frequency-inverse document frequency) is a feature vectorization method used in text mining to reflec thte importance of a term to a document in the corpus.

*Word2Vec* is an Estimator which takes sequences of words representing documents and trains a Word2VecModel, which maps each word to a unique fixed-size vector. 

*CountVectorizer* aim to convert a collection of text documents to vectors of token counts.

*Tokenizer* is a simple class providing functionality for taking text and breaking it into individual terms (usually words), there is also RegexTokenizer which allows more advanced tokenization based on regex matching. 

*StopWordsRemover* takes an input of a sequence of strings and drops all the stop words from the input sequences.

*NGram* takes an input of a sequence of strings and the parameter n is used to determine the number of terms in each n-gram. The output will be a sequence of n-grams where each n-gram is represented by a space-delimited string of n consecutive words. 

*PCA* is a statistical procedure that uses orthogonal transformation to convert a set of observations of possibly correlated variables into a set of values of linearly uncorrelated variables called principal components. 

*Polynomial Expansion* is the process of expanding your features into a polynomial space, which is formulated by an n-degree combination of original dimensions. 

*OneHotEncoder* allows for mapping a column of label indices to a column of binary vectors. This enables algorithms such as logistic regression to utilize categorical variables. 

*VectorIndexer* helps index categorical features in datasets of Vectors. It can allow algorithms such as Decision Trees and Tree Ensembles to treat categorical features appropriately, improving performance. 

*Interaction* is a Transformer which takes vector or double-valued columns and can generate their interactions.

*Normalizer* is a Transformer which transforms a dataset of Vector rows, normalizing each Vector to have unit norm. It takes some parameter p, which uses the p-norm used for normalization. 

*StandardScaler* transforms a dataset of Vector rows, normalizing each feature to have unit standard deviation and/or zero mean. 

Until next time,
#### Clayton Blythe | *Deep Python*


