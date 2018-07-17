# get the dataset
from sklearn.datasets import fetch_20newsgroups

ng_train = fetch_20newsgroups(subset = 'train')# default shuffle = True, random_state = 42
ng_test = fetch_20newsgroups(subset = 'test')

texts_train = ng_train.data
texts_test = ng_test.data
labels_train = ng_train.target
labels_test = ng_test.target

target_names = ng_train.target_names
file_names = ng_train.filenames