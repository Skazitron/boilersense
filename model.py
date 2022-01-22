
from sklearn.feature_extraction.text import CountVectorizer
from imblearn.over_sampling import RandomOverSampler
from sklearn.metrics import precision_recall_fscore_support
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import numpy as np
training_data = pd.read_csv("/Users/shellyschwartz/Downloads/boilermakeData3.csv")

def tokenize_text(text_data):
    cv = CountVectorizer(strip_accents='ascii', token_pattern=u'(?ui)\\b\\w*[a-z]+\\w*\\b', lowercase=True,
                         stop_words='english')
    test_data = cv.fit_transform(text_data)
    return test_data


#target can be comment, quality, or difficulty
def train_model(df, target):
    #cleaning
    df['comment'] = df['comment'].replace(['😎awesome', '😖awful', '😐average'], ["1", "1", "0"])
    df = df[df["features"] != "No Comments"]
    df["features"] = df["features"].apply(lambda x: np.str_(x))

    X_train, X_test, y_train, y_test = train_test_split(df["features"], df[target], random_state=4)

    #tokenizing
    cv = CountVectorizer(strip_accents='ascii', token_pattern=u'(?ui)\\b\\w*[a-z]+\\w*\\b', lowercase=True,
                         stop_words='english')


    X_train_cv = cv.fit_transform(X_train)
    X_test_cv = cv.transform(X_test)

    #model
    naive_bayes = MultinomialNB()

    #fitting
    ros = RandomOverSampler(random_state=42)
    X_resampled, y_resampled = ros.fit_resample(X_train_cv, y_train)
    naive_bayes.fit(X_resampled, y_resampled)



    #get preds
    predictions = naive_bayes.predict(X_test_cv).tolist()

    y_test = y_test.tolist()

    #testing
    report = pd.DataFrame(list(precision_recall_fscore_support(y_test, predictions)),
                          index=['Precision', 'Recall', 'F1-score', 'Support']).T

    # Now add the 'Avg/Total' row
    report.loc['Avg/Total', :] = precision_recall_fscore_support(y_test, predictions,
                                                                 average='weighted')
    report.loc['Avg/Total', 'Support'] = report['Support'].sum()

    return naive_bayes



def get_prediction(df, col, target):
    for row in range(df.iterrows()):
        x_test = tokenize_text(row[col])
        prediction = train_model(training_data, target).predict(x_test)
    return prediction



#
# df = pd.read_csv("/Users/shellyschwartz/Downloads/boilermakeData3.csv")
# df = df[df["features"]!="No Comments"]
# print(df['difficulty'].value_counts())
#
# df['comment'] = df['comment'].replace(['😎awesome', '😖awful', '😐average'], ["1", "1", "0"])
#
# df["features"] = df["features"].apply(lambda x: np.str_(x))
# print(len(df['features']), len(df["difficulty"]))
#
#
# X_train, X_test, y_train, y_test = train_test_split(df["features"], df["comment"], random_state=4)
#
#
# cv = CountVectorizer(strip_accents='ascii', token_pattern=u'(?ui)\\b\\w*[a-z]+\\w*\\b', lowercase=True, stop_words='english')
#
#
# X_train_cv = cv.fit_transform(X_train)
# X_test_cv = cv.transform(X_test)
#
#
# naive_bayes = MultinomialNB()
#
#
# ros = RandomOverSampler(random_state=42)
# X_resampled, y_resampled = ros.fit_resample(X_train_cv, y_train)
# naive_bayes.fit(X_resampled, y_resampled)
#
# naive_bayes.fit(X_resampled, y_resampled)
# predictions = naive_bayes.predict(X_test_cv).tolist()
#
#
#
# y_test = y_test.tolist()
#
# import pandas as pd
# from sklearn.metrics import precision_recall_fscore_support
#
# report = pd.DataFrame(list(precision_recall_fscore_support(y_test, predictions)),
#             index=['Precision', 'Recall', 'F1-score', 'Support']).T
#
# # Now add the 'Avg/Total' row
# report.loc['Avg/Total', :] = precision_recall_fscore_support(y_test,  predictions,
#     average='weighted')
# report.loc['Avg/Total', 'Support'] = report['Support'].sum()
# print(report)







