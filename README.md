# Doc-classification--20-newsgroups
This is a document classification task using the classific 20 newsgroups corpus. Tensorflow, keras, numpy, scipy, matplotlib, h5py, sklearn, nltk, wordnet, gensim are needed.

Explanation of each file:

1. Proposal: a detailed description of the project.
2. Train word2vec.ipynb: code to train word embeddings with gensim; visualize the embeddings.
3. Stoplist:for data preprocess. I got it from https://www.cnblogs.com/pinard/p/6756534.html
4. Preprocessed data for CNN-update.txt: Preprocessed data for the TextCNN model; acquired by Data Visualization and Preprocessing.ipynb. Saved for convinience for training.
5. Data Preprocessing and Visualization.ipynb: code for data visualizatioin and preprocess for the TextCNN model.
6. load_20newsgroups.py: code for fetching the dataset from sklearn；calling it in each model is a bit more convinient than having to fetch the data from sklearn each time.
7. Model_1- Tf-idf & SGDClassifier-submit.ipynb: code to train a Tf-idf & SGDClassifier，the base model.
8. Model_2-TextCNN-Glove.6B-submit-update.ipynb: code to train and improve a TextCNN model using the pretrained glove 6B 100d word embeddings.
9. Model_3-TextCNN-Glove.840B.300d-submit.ipynb: the final solution. Code to train a TextCNN model using the pretrained glove 840B 300d word embeddings, based on the work done in Model_2-TextCNN-Glove.6B-submit-update.ipynb.
10. Model_4-TextCNN-word2vec-submit.ipynb: code to train a TextCNN model using the word2vec word embeddings got by Train word2vec.ipynb.
11. glove 100d visualization: visulization of glove.6B.100d.

How to get the data used in the project?

1. Text8：to train word2vec embeddings
hyperlink：http://mattmahoney.net/dc/text8.zip
2. glove embeddings: multiple choices; I settled on the glove.840B.300d for final solution.
hyperlink：http://nlp.stanford.edu/data/glove.6B.zip, https://nlp.stanford.edu/data/glove.840B.300d.zip
3. 20newsgroups dataset
hyperlink：http://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html
