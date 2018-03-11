# this will be happening when the user asks for classification of a given article
from textblob import TextBlob
import pandas as pd
import numpy as np
import itertools
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, HashingVectorizer
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt
from sklearn.externals import joblib
import time
# pip install yandex-translater requests
from yandex_translate import YandexTranslate

# setup stuff for translations
translate = YandexTranslate('api-key-here')



def train_nn():
    start = time.time()
    df = pd.read_csv("nlp_dataset/raw/fake_or_real_news.csv")
    X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.1, random_state=53)
    count_vectorizer = CountVectorizer(stop_words='english')
    count_vectorizer.fit(X_train)
    joblib.dump(count_vectorizer, 'count_vectorizer.pkl')

    count_train = count_vectorizer.transform(X_train)
    count_test = count_vectorizer.transform(X_test)

    clf = MLPClassifier(alpha=1)
    clf.fit(count_train, y_train)

    #store the model somewhere
    joblib.dump(clf, 'nn_model.pkl')
    end = time.time()
    print('Training has taken {} seconds'.format(end-start))

def classify_text(text):
    """text: string.
    """
    # there is a limit - we can translate 1,000,000 characters.
    print('Classify text.')
    start = time.time()
    translate.translate(text, 'en')
    # en_text = TextBlob(text).translate(to='en')

    # load the model from some file
    clf = joblib.load('nn_model.pkl')
    count_vectorizer = joblib.load('count_vectorizer.pkl')

    test_item = [text]
    count_test = count_vectorizer.transform(test_item)

    # classify the article
    predicted_class = clf.predict(count_test)
    prediction_proba = clf.predict_proba(count_test)
    print(predicted_class)
    print(prediction_proba)
    end = time.time()
    print('Predicting has taken {} seconds'.format(end-start))
    return predicted_class, prediction_proba

# train_nn()

df = pd.read_csv("nlp_dataset/raw/fake_or_real_news.csv")
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.3, random_state=53)
text = X_test.iloc[3]
prediction, prediction_proba = classify_text(X_test.iloc[3])
