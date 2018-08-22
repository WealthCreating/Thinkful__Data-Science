'''
For this challenge, you will need to choose a corpus of data from nltk or another source that
includes categories you can predict and create an analysis pipeline that includes the following steps:

    * Data cleaning / processing / language parsing
    * Create features using two different NLP methods: For example, BoW vs tf-idf.
    * Use the features to fit supervised learning models for each feature set to predict the category outcomes.
    * Assess your models using cross-validation and determine whether one model performed better.
    * Pick one of the models and try to increase accuracy by at least 5 percentage points.

'''
import numpy as np
import pandas as pd
import scipy
import sklearn
import spacy
import matplotlib.pyplot as pyplot
import seaborn as sns
import re
from nltk.corpus import gutenberg, stopwords
from collections import Counter
%matplotlib inline


def text_cleaner(text):
    text = re.sub(r'--',' ',text)
    text = re.sub("[\[].*?[\]]", "", text)
    text = ' '.join(text.split())
    return text

book = gutenberg.raw('austen-sense.txt')
book = re.sub(r'Chapter \d+', '', book)
book = text_cleaner(book)

nlp = spacy.load('en')
book_doc = nlp(book)

sentences = [sentence for sentence in book_doc.sentences]

# Get the 2,000 most common words
def bag_of_words(text):

    # Filter out punctuation and stop words
    allwords = [token.lemma_ for token in text if not token.is_punct and not token.is_stop]

    # Return the most 2,000 words
    return [item[0] for item in Counter(allwords).most_common(2000)]

# What does this function do?
def bag_of_words_features(sentences, common_words):

    data = pd.DataFrame(columns=common_words)
    data['text_sentence'] = sentences[0]
    data['text_source'] = sentences[1]
    df.loc[:, common_words] = 0

    for i, sentence in enumerate(data['text_sentence']):

        words = [token.lemma_
                 for token in sentence
                 if (
                         not token.is_punct
                         and not token.is_stop
                         and token.lemma_ in common_words
                 )]

        # Populate the row with word counts
        [df.loc[i, word] += 1 for word in words]

# Set up the bag_of_words
common_words = bag_of_words(book_doc)
# create our dataframe with features
word_counts = bag_of_words_features(sentences, common_words)

from sklearn import ensemble
from sklearn.model_selection import train_test_split
from skearn.model_selection import cross_val_score
from sklearn.linear_regression import LogisticRegression


Y = word_counts['text_source']
X = np.array(word_counts.drop(['text_sentence', 'text_source'], 1))

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.4,random_state=42)

lr = LogisticRegression()
train = lr.fit(X_train, Y_train)
print('Training set score:', lr.score(X_train, Y_train))

# ------------------------------------------------------------------------------
# tfidf

paragraphs = gutenberg.paras('austen-sense.txt')
paragraphs_clean = []
for paragraph in paragraphs:
    paragraph = paragraph[0]
    paragraph = [re.sub(r'--', '', word) for word in paragraph]
    paragraphs_clean.append(' '.join(paragraph))

from sklearn.feature_extraction.text import TfidfVectorizer

X_train, X_test = train_test_split(paragraphs_clean, test_size=0.4, random_state=0)

vectorizer = TfidfVectorizer(max_df=0.5,
                             min_df=2,
                             stop_words='english',
                             lowercase=True,
                             use_idf=True,
                             smooth_idf=True
                             )

# Apply the vectorizer
paragraphs_clean_tfidf = vectorizer.fit_transform(paragraphs_clean)

# Split into train/test sets
X_train_tfidf, X_test_tfidf, Y_train_tfidf, Y_test_tfidf = train_test_split(
    paragraphs_clean_tfidf, test_size=0.4, random_state=0)

from sklearn.decomposition import TruncatedSVD
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import Normalizer

svd = TruncatedSVD()
lsa = make_pipeline(svd, Normalizer(copy=False))

X_train_lsa = lsa.fit_transform(X_train_tfidf)






print(a)
