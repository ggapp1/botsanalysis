import data
import tweepy
import nltk
import gensim
from gensim.models import Word2Vec

#api = data.generate_API()

from sklearn.feature_extraction.text import CountVectorizer


def tfidf_simples():
	f = open("fsteinicial", "r")
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


def wordvec():
	f = open("fsteinicial", "r")
	corpus = f.read()
	corpus = [corpus]
	
	model = Word2Vec(corpus_file="fsteinicial", size=100, window=5, min_count=1, workers=4, sg=0)
	return model

wordvec()