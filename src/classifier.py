from sklearn import metrics

from src.support import getDataFrame, splitData, trainModel


def loadModel():
    df = getDataFrame()
    X_train, X_test, y_train, y_test = splitData(df)
    text_clf_nb, text_clf_lsvc = trainModel(X_train, X_test, y_train, y_test)
    predictions_lsvc = text_clf_lsvc.predict(X_test)
    predictions_nb = text_clf_nb.predict(X_test)
    if metrics.accuracy_score(y_test, predictions_lsvc) > metrics.accuracy_score(y_test, predictions_nb):
        return predictions_lsvc
    else:
        return predictions_nb
