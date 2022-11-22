from gensim.models import KeyedVectors
from flask import abort

""" model = KeyedVectors.load_word2vec_format('wiki-50d-word2vec.txt'
, binary=False) """

def findKeywords(likedKeywords, dislikedKeywords):
    """ result = model.most_similar(positive=likedKeywords, negative=dislikedKeywords, topn=2)
    return result """
    return likedKeywords