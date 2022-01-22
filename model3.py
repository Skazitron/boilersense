import pandas as pd
import numpy as np
from imblearn.over_sampling import RandomOverSampler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import FeatureUnion

df = pd.read_csv("/Users/shellyschwartz/Downloads/boilermakeData3.csv")

#cleaning and filtering
df = df[df["features"]!="No Comments"]
df["features"] = df["features"].apply(lambda x: np.str_(x))
print(df["comment"].value_counts())

df['comment'] = df['comment'].replace(['😎awesome', '😖awful', '😐average'], ["1", "1", "0"])
# X = df[["features", "quality"]]
# y = df["difficulty"]
# #splitting data
# X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.3, random_state=4)


from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(strip_accents='ascii', token_pattern=u'(?ui)\\b\\w*[a-z]+\\w*\\b', lowercase=True, stop_words='english')
# n = np.array(X_train["quality"])
#
# import scipy.sparse
# X_train_cv = scipy.sparse.hstack(cv.fit_transform(X_train["features"]), n)
#
# print(X_train_cv)



import scipy.sparse as sp





idx_train, idx_test = train_test_split(df.index, random_state=0)
X_train, y_train = df.loc[idx_train, 'features'],  df.loc[idx_train, 'quality']
X_test, y_test = df.loc[idx_test, 'features'],  df.loc[idx_test, 'quality']
doc_m_train = cv.fit_transform(X_train)
doc_m_test = cv.transform(X_test)

# print(doc_m_train)
print(doc_m_test)

X_train_all_features = pd.concat([pd.DataFrame(doc_m_train), df.loc[idx_train, 'difficulty']], axis = 1)
X_test_all_features = pd.concat([pd.DataFrame(doc_m_test), df.loc[idx_test, 'difficulty']], axis = 1)


from scipy.sparse import hstack
X_train_fin= hstack([doc_m_train, df.loc[idx_train, 'quality'].values.reshape(-1, 1)])
X_test_fin= hstack([doc_m_test, df.loc[idx_test, 'quality'].values.reshape(-1, 1)])

from sklearn.naive_bayes import MultinomialNB
naive_bayes = MultinomialNB()

ros = RandomOverSampler(random_state=42)
X_resampled, y_resampled = ros.fit_resample(X_train_fin, y_train)
naive_bayes.fit(X_resampled, y_resampled)

predictions = naive_bayes.predict(X_test_fin).tolist()




from sklearn.metrics import precision_recall_fscore_support

report = pd.DataFrame(list(precision_recall_fscore_support(y_test, predictions)),
            index=['Precision', 'Recall', 'F1-score', 'Support']).T

# Now add the 'Avg/Total' row
report.loc['Avg/Total', :] = precision_recall_fscore_support(y_test,  predictions,
    average='weighted')
report.loc['Avg/Total', 'Support'] = report['Support'].sum()
print(report)