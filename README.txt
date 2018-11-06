一. 项目用到的软件和库的获取步骤

本项目使用基于tensorflow后端的keras搭建神经网络模型。需要用到的软件和库及其获取步骤如下：
1.tensorflow
安装请参考：https://tensorflow.google.cn/install/
2.numpy、scipy、matplotlib：
安装请参考：https://www.scipy.org/install.html
3.keras
安装请参考：https://keras.io/#installation
4.h5py： necessary for saving keras model
安装请参考：http://docs.h5py.org/en/latest/build.html
6.sklearn
安装请参考：http://scikit-learn.org/stable/install.html
7.nltk：
安装请参考：http://www.nltk.org/install.html
8.wordnet：
通过以下命令下载wordnet：nltk.download('wordnet')
9.gensim：
安装请参考：https://radimrehurek.com/gensim/install.html


二. 项目用到的原始数据获取步骤

1. Text8：用于训练word2vec词向量
获取链接：http://mattmahoney.net/dc/text8.zip
2. glove词向量:里面有多个可供选择的预训练词向量，本项目初始使用的是glove.6B.100d，最终模型使用的是glove.840B.300d。
获取链接：http://nlp.stanford.edu/data/glove.6B.zip, https://nlp.stanford.edu/data/glove.840B.300d.zip
3. 20newsgroups dataset
参考以下链接获取：http://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html

三. 本报告文件夹所包含文件说明

1. Proposal:项目报告
2. w2v vectors.txt:自己用gensim训练出来的word2vec词向量
3. Train word2vec.ipynb:用gensim训练word2vec词向量及词向量可视化
4. Stoplist:文本预处理用到的停用词列表。来源：https://www.cnblogs.com/pinard/p/6756534.html
5. Preprocessed data for CNN-update.txt:TextCNN模型用到的预处理好的数据，通过Data Visualization and Preprocessing.ipynb获得。
6. Data Preprocessing and Visualization.ipynb: TextCNN模型用到的文本预处理及数据可视化。
7. load_20newsgroups.py:从sklearn上获取新闻组数据的程序；调用使模型获取数据更加方便。
8. Model_1- Tf-idf & SGDClassifier-submit.ipynb:Tf-idf & SGDClassifier模型，基准模型。
9. Model_2-TextCNN-Glove.6B-submit-update.ipynb:用预训练的glove 6B 100d词向量训练TextCNN模型
10.Model_3-TextCNN-Glove.840B.300d-submit.ipynb
11. Model_4-TextCNN-word2vec-submit.ipynb:用自己通过gensim训练的word2vec词向量训练TextCNN模型
12. glove 100d visualization:glove.6B.100d词向量的可视化

四. 程序运行所需时间说明：
1. Model_1- Tf-idf & SGDClassifier-submit.ipynb:Tf-idf & SGDClassifier:涉及网格搜索，参数空间较大，训练时间3.5小时。
2. Model_2-TextCNN-Glove-submit.ipynb:70s/epoch左右，训练400轮，耗时8小时。
3. Model_3-TextCNN-word2vec-submit.ipynb:70s/epoch左右，训练400轮，耗时8.5小时。
4. 其它程序运行时间较短，几分钟即可。

test
