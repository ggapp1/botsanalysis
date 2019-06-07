import data
import tweepy
import nltk
import gensim
from gensim.models import Word2Vec

#api = data.generate_API()

from sklearn.feature_extraction.text import CountVectorizer


def tfidf_simples():
	f = open("tweets_1037466257833041920", "r")
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

def teste():
	from sklearn.feature_extraction.text import TfidfVectorizer
	from sklearn.cluster import KMeans
	from sklearn.metrics import adjusted_rand_score
	documents = []
	with open("fsteinicial") as f:
		for line in f:
			documents.append(line)

	vectorizer = TfidfVectorizer(stop_words='english')
	X = vectorizer.fit_transform(documents)

	true_k = 2
	model = KMeans(n_clusters=true_k, init='k-means', max_iter=100, n_init=1)
	model.fit(X)

	print("Top terms per cluster:")
	order_centroids = model.cluster_centers_.argsort()[:, ::-1]
	terms = vectorizer.get_feature_names()
	for i in range(true_k):
	    print("Cluster %d:" % i),
	    for ind in order_centroids[i, :10]:
	        print(' %s' % terms[ind]),
	    print

	print("\n")
	print("Prediction")

	Y = vectorizer.transform(["chrome browser to open."])
	prediction = model.predict(Y)
	print(prediction)

	Y = vectorizer.transform(["My cat is hungry."])
	prediction = model.predict(Y)
	print(prediction)