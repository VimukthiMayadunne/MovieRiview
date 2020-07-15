import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC


def getDataFrame():
    df = pd.read_csv('../data/moviereviews2.tsv', sep='\t')
    df.dropna(inplace=True)
    blanks = []
    for i, lb, rv in df.itertuples():
        if type(rv) == str:
            if rv.isspace():
                blanks.append(i)
    df.drop(blanks, inplace=True)
    return df


def splitData(df):
    X = df['review']
    y = df['label']
    return train_test_split(X, y, test_size=0.33, random_state=42)


def trainModel(X_train, X_test, y_train, y_test):
    # Naïve Bayes Model:
    text_clf_nb = Pipeline([('tfidf', TfidfVectorizer()),
                            ('clf', MultinomialNB()),
                            ])
    # Linear SVC Model:
    text_clf_lsvc = Pipeline([('tfidf', TfidfVectorizer()),
                              ('clf', LinearSVC()),
                              ])

    # Train both models on the moviereviews.tsv training set:
    return text_clf_nb.fit(X_train, y_train), text_clf_lsvc.fit(X_train, y_train)
