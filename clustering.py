import pymongo
import nltk
from nltk.corpus import stopwords
from nltk.cluster import KMeansClusterer
from gensim.models import Word2Vec
import regex
import spacy
import os

# NLP setup
nlp = spacy.load("en_core_web_sm")
nltk.download("stopwords")
nltk.download("corpus")
nltk.download('words')
nltk.download('punkt')

# DB connection setup
client = pymongo.MongoClient('127.0.0.1',27017) 
db = client.twitterCrawl
collection = db["tweets"]

stopwords = set(stopwords.words('english'))
#@title Defines spacy tokenization functions
#@Tokenize
def spacy_tokenize(string):
  tokens = list()
  doc = nlp(string)
  for token in doc:
    tokens.append(token)
  return tokens

#@Normalize
def normalize(tokens):
  normalized_tokens = list()
  for token in tokens:
    if not token.is_stop:
        if token.is_alpha and "RT" not in token.text and len(token) > 2:            
            normalized_tokens.append(token.text.lower())
  return normalized_tokens

#@Tokenize and normalize
def tokenize_normalize(string):
  return normalize(spacy_tokenize(string))

# construct the corpus of tokenized tweets.
tokenized_tweets = []
m = 0
for document in collection.find({}):
    tokenized = tokenize_normalize(document["text"])
    tokenized_tweets.append(tokenized)
    if m > 1000:
        break
    m += 1
    # print(tokenized)

print(tokenized_tweets)

# Clustering
model = Word2Vec(tokenized_tweets, min_count=1)
X = model[model.wv.vocab]
print(tokenized_tweets[0])
print(model.wv["coronavirus"])
print(len(X))

NUM_CLUSTERS=3
kclusterer = KMeansClusterer(NUM_CLUSTERS, distance=nltk.cluster.util.cosine_distance, repeats=25)
assigned_clusters = kclusterer.cluster(X, assign_clusters=True)
print (len(assigned_clusters))

words = list(model.wv.vocab)
for i, word in enumerate(words):  
    print (word + ":" + str(assigned_clusters[i]))
