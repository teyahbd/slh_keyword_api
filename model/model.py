import gensim.downloader as api

model = api.load("glove-wiki-gigaword-50")

def find_keywords(liked_keywords, disliked_keywords):
    result = model.most_similar(positive=liked_keywords, negative=disliked_keywords, topn=2)
    return result
