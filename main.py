import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle


filename = 'reviews.pkl'
model = pickle.load(open(filename, 'rb'))
vectorizer = pickle.load(open('transform.pkl', 'rb'))

def create_similarity():
    data = pd.read_csv('final_df.csv')
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(data['all'])
    similiarity = cosine_similarity(count_matrix)
    return data, similiarity

def recommendation(title):
    title = title.lower()
    try:
        data.head()
        similarity.shape
    except:
        data, similarity = create_similarity()
    if title not in data['movie_title']:
        return ('Sorry! The movie you requested is not in our database.')
    else:
        i = data.loc[data['movie_title']==title].index[0]
        lst = list(enumerate(similarity[i]))
        lst = lst[1:11] 
        r = []
        for i in range(lst):
            a = lst[i][0]
            r.append(data['movie_title'][a])
        return r
    
def to_list(x):
    x = x.split('","')
    x[0] = x[0].replace('["','')
    x[-1] = x[-1].replace('"]','')
    return x

def get_suggestions():
    data = pd.read_csv('final_df.csv')
    return list(data['movie_title'].str.capitalize())