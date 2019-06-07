import data
import tweepy
import nltk
import gensim
from gensim.models import Word2Vec
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from gensim import corpora
from nltk.corpus import stopwords 
from nltk.stem.wordnet import WordNetLemmatizer
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation
import mtranslate
from hatesonar import Sonar
from textblob import TextBlob
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
import glob, os
import re

def clean(text):
	#review
	stop = set(stopwords.words('portuguese'))
	exclude = set(string.punctuation) 
	lemma = WordNetLemmatizer()
	doc = re.sub(r'\bhttp\b', '', text)
	stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
	punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
	normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
	return normalized

def tfidf(file):
	f = open(file, "r")
	corpus = f.read()
	corpus = [corpus]
	vectorizer = CountVectorizer()
	X = vectorizer.fit_transform(corpus)
	x = X.toarray()
	y = vectorizer.get_feature_names()
	a = 0
	for i in x[0]:
		print("{} = {}".format(i,y[a]))
		a = a + 1


def word2vec(filename):
	f = open(filename, "r")
	corpus = f.read()
	corpus = [corpus]
	
	model = Word2Vec(corpus_file=filename, size=100, window=5, min_count=1, workers=4, sg=0)
	return model

def display_topics(model, feature_names, no_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print("Topic %d:" % (topic_idx))
        print(" ".join([feature_names[i]
                        for i in topic.argsort()[:-no_top_words - 1:-1]]))


def read_documents():
	documents = []
	for file in glob.glob("files/tweets_*"):
		f = open(file, "r")
		corpus = f.read()
		documents.append(clean(corpus))

	return documents

def lda():
	documents = read_documents()
	no_features = 10000

	# NMF is able to use tf-idf
	tfidf_vectorizer = TfidfVectorizer(max_features=no_features)
	tfidf = tfidf_vectorizer.fit_transform(documents)
	tfidf_feature_names = tfidf_vectorizer.get_feature_names()

	# LDA can only use raw term counts for LDA because it is a probabilistic graphical model
	tf_vectorizer = CountVectorizer(max_features=no_features)
	tf = tf_vectorizer.fit_transform(documents)
	tf_feature_names = tf_vectorizer.get_feature_names()


	no_topics = 10

	# Run LDA
	lda = LatentDirichletAllocation(n_topics=no_topics, max_iter=100, learning_method='online', learning_offset=100.,random_state=1).fit(tf)
	no_top_words = 10
	display_topics(lda, tf_feature_names, no_top_words)	    

def kmeans():
	documents = read_documents()

	vectorizer = TfidfVectorizer()
	X = vectorizer.fit_transform(documents)
	true_k = 2
	model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
	model.fit(X)
	print("Top terms per cluster:")
	order_centroids = model.cluster_centers_.argsort()[:, ::-1]
	terms = vectorizer.get_feature_names()
	for i in range(true_k):
	    print ("Cluster %d:" % i)
	    for ind in order_centroids[i, :10]:
	        print(' %s' % terms[ind])

	pipeline = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
	])          

	X = pipeline.fit_transform(documents).todense()        
	pca = PCA(n_components=2).fit(X)
	data2D = pca.transform(X)    
	plt.scatter(data2D[:,0], data2D[:,1])
	plt.show()

	centers2D = pca.transform(model.cluster_centers_)    
	plt.scatter(centers2D[:,0], centers2D[:,1], 
            marker='x', s=200, linewidths=3, c='r')

	plt.show()              

def sentiment_analysis():
	documents = read_documents()
	sonar = Sonar()
	print(sonar.ping(text=mtranslate.translate(documents[1])))
	analysis_tb = TextBlob(mtranslate.translate(documents[1]))
	print(analysis_tb.sentiment.polarity)


def main():
	lda()
	print("\n\n")
	kmeans()
	print("\n\n")
	sentiment_analysis()

if __name__ == '__main__':
	main()