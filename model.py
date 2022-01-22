from io import StringIO

from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
df = pd.read_csv("/Users/shellyschwartz/Downloads/boilermakeData2.csv")
print(df['difficulty'].value_counts())



df["features"] = df["features"].apply(lambda x: np.str_(x))
print(len(df['features']), len(df["difficulty"]))


X_train, X_test, y_train, y_test = train_test_split(df["features"], df["difficulty"], random_state=4)

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(strip_accents='ascii', token_pattern=u'(?ui)\\b\\w*[a-z]+\\w*\\b', lowercase=True, stop_words='english')


X_train_cv = cv.fit_transform(X_train)
X_test_cv = cv.transform(X_test)

from sklearn.naive_bayes import MultinomialNB
naive_bayes = MultinomialNB()
naive_bayes.fit(X_train_cv, y_train)
predictions = naive_bayes.predict(X_test_cv).tolist()


from sklearn.metrics import accuracy_score, precision_score, recall_score as score
# print('Accuracy score: ', accuracy_score(y_test, predictions))
# print('Precision score: ', precision_score(y_test, predictions, average = "weighted"))
# print('Recall score: ', recall_score(y_test, predictions, average = "weighted"))
y_test = y_test.tolist()

import pandas as pd
from sklearn.metrics import precision_recall_fscore_support

report = pd.DataFrame(list(precision_recall_fscore_support(y_test, predictions)),
            index=['Precision', 'Recall', 'F1-score', 'Support']).T

# Now add the 'Avg/Total' row
report.loc['Avg/Total', :] = precision_recall_fscore_support(y_test,  predictions,
    average='weighted')
report.loc['Avg/Total', 'Support'] = report['Support'].sum()
print(report)
# print(type(predictions))
# print("_____________________SFadsfdsfasdfsdfasdff_____________")
# #print(predictions)
# precision, recall, fscore, support = score(y_test, predictions, average = "weighted")
#
# print('precision: {}'.format(precision))
# print('recall: {}'.format(recall))
# print('fscore: {}'.format(fscore))
# print('support: {}'.format(support))

