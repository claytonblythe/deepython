Title: Spark MLlib Overview
Date: 2017-8-30 13:10
Category: Spark

This is an overview of the Spark MLlib framework, Spark's scalable machine learning library consisting of common machine learning algorithms and utilities that include tools for classification, regression, clustering, collaborative filtering, dimensionality reduction, as well as providing underlying basic summary statistics. It also contains various utilities for doing linear algrebra, statistics, and general handling of data. MLlib uses the linear algebra package called Breeze, which depends on the netlib-java for optimized numerical processing. Spark MLlib is distinct from Spark ML, as it deals with RDD (Resilient Distributed Datasets) instead of DataFrames. RDD's are fundamental data structures of Spark, which are divided into logical partitions and distributed across different nodes of a cluster. Spark makes use of the concept of RDD to achieve faster and more efficient MapReduce operations. It is also fault tolerant as well as in-memory data processing, which is 10 to 100 times faster than network and Disk.

Here is a broad overview of the capabilities of Spark MLlib:

## Basic Statistics
*Correlation* computes the correlation matrix for the input Dataset of vectors, and the output will be a DataFrame that contains the correlation matrix of the column of vectors.

*Hypothesis Testing* is possible thorugh a ChiSquare test to conduct a Pearson independence test for every feature against the label or target. For each feature, the feature label pairs are converted into a contingency matrix for which the Chi-squared statistic is computed.


## ML Pipelines
Inspired by the scikit-learn project, MLlib standardizes APIs for machine learning algorithms to make it easier to combine multiple algorithms into a single pipeline or workflow.

*DataFrame* ML API uses DataFrame form Spark SQL as an ML dataset, which can hold a variety of data types.

*Transformer* is an algorithm that can transform one DataFrame into another DataFrame (e.g. an ML model is a Transformer which transforms a DataFrame into a DataFrame with predictions).

*Estimator* is an algorithm which can be fit on a DataFrame to produce a Transformer (this would be a learning algorithm which produces a model)

*Pipeline* chains multiple Transformers and Estimators together for a ML workflow.

## Feature Selection & Transformation

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

*MinMaxScaler* is often used to rescale a feature to a specific range like [0,1].

*MaxAbsScaler* transforms a dataset of Vector rows to a range of [-1,1].

*Bucketizer* transforms a column of continous features to a column of feature buckets.

*Imputer* is a transformer that completes missing values in a dataset, either using the mean or the median.

## Feature Selectors
*VectorSlicer* is a transformer that takes a feature vecotr and outputs a new feature vector with a sub-array of the original features. It is useful for extracting features from a vector column.

*RFormula* selects columns specified by an R model formula, (~, ., +, etc.)

*ChiSqSelector* uses Chi-Squared tests of independence to decide which features to use, from a fixed number of top features.

*LSH Algorithms* like Bucketed Random Projection for Euclidian distance and MinHash for Jaccard Distance.

## Classification and Regression
*Logistic Regression* is supported with summary statistics, as well as multinomial logistic regression.

*DecisionTreeClassifier* is a tree based calssification and regression model and so is *RandomForestClassificationModel* and *GBTClassificationModel*

*MultilayerPerceptronClassifier* is a classifier based on feedforward artificial neural networks, and it consists of fully connected layers that itulize a simoid logistic function and the output layer uses a softmax function. The number of nodes in the output layer corresponds to the number of classes to be classified.

*LinearSVC* is a support vector machine that represents a hyperplane or set of hyperplanes in a high or infinite dimensional space that can be used for classification, regression, or other tasks.

*NaiveBayes* allows for simple probabilistic classifiers on applying Bayes' theorem with strong (naive) independence assumptions between the features.

For regression problems, *LinearRegression* and *GeneralizedLinearRegression* are supported.

*AFTSurvivalRegression* employs an Accelerated failure time (AFT) model, which is a parametric survival regression model for censored data. It is a log-linear model for survival analysis and is easier to parallelize.

Other methods like ensembles of decision trees, random forest, and gradient-boosted trees are supported.

## Clustering
*K-Means* is a popular used clustering algorithm that clusters the data points into a predefined number of clusters. The MLlib implementation includes a parallelized variant of the k-means++ method.

*Latent Dirichlet Allocation*, *Bisecting k-means*, and *Gaussian Mixture Model (GMM)* are all supported as well.

## Collaborative Filtering
Spark MLlib supports collaborative filtering, which are techniques that aim to filll in the missing entries in a user-item association matrix. It currently supports model-based collaborative filtering, in which users and products are described by a small set of latent factors that can be used to predict missing entries. Spark.ml uses the alternating least squares algorithm to learn these latent factors.

## Frequent Pattern Mining
Spark MLlib has capabilities for mining frequent items, itemsets, subsequences, or other substructures that are cmomonly the first steps for analyzing a large-scale dataset. Given a dataset of transactions, the first step is to calculate item frequencies and identify frequent items. The second step uses a suffix tree structure to encode transactions without generating candidate sets explicitly.

## Model Selection
MLlib supports model selection using tools like *CrossValidator* and *TrainValidationSplit* which provide useful tools for hyperparameter tuning and parameter grids to search over.


Until next time,
#### Clayton Blythe | *Deep Python*


