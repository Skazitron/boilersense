
from sklearn.feature_extraction.text import CountVectorizer
from imblearn.over_sampling import RandomOverSampler
from sklearn.metrics import precision_recall_fscore_support
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import numpy as np
training_data = pd.read_csv("/Users/shellyschwartz/Downloads/boilermakeData2.csv")
training_data2 = pd.read_csv("/Users/shellyschwartz/Downloads/boilermakeData3.csv")
training_data["comment"] = training_data2["comment"]
print(training_data)
#comments_df = pd.read_csv("./ScrapersAndDataJosh/PSAWcomments.csv")

gen_eds = pd.read_csv("/Users/shellyschwartz/Downloads/red_courses_new3.csv")
others = pd.read_csv("./ScrapersAndDataJosh/reddit_comments.csv")
#target can be comment, quality, or difficulty
def train_model_and_get_pred(df, target, df_test, col):
    #cleaning
    df['quality'] = df['quality'].replace([3.0, 2.0], ["2", "1"])
    df['comment'] = df['comment'].replace(['😎awesome', '😖awful', '😐average'], ["1", "0", "0"])
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
    predictions = []
    for index, row in df_test.iterrows():
        test_data = cv.transform([row[col]])
        predictions.append(naive_bayes.predict(test_data)[0])
    # predictions = naive_bayes.predict(X_test_cv).tolist()
    #
    # y_test = y_test.tolist()

    #testing
    # report = pd.DataFrame(list(precision_recall_fscore_support(y_test, predictions)),
    #                       index=['Precision', 'Recall', 'F1-score', 'Support']).T
    #
    # # Now add the 'Avg/Total' row
    # report.loc['Avg/Total', :] = precision_recall_fscore_support(y_test, predictions,
    #                                                              average='weighted')
    # report.loc['Avg/Total', 'Support'] = report['Support'].sum()

    return predictions
comments_df = pd.concat([others, gen_eds])
comments_df = comments_df.drop_duplicates()
qual_preds = train_model_and_get_pred(training_data, "quality", comments_df, "review")
diff_preds = train_model_and_get_pred(training_data, "difficulty", comments_df, "review")
comments_preds = train_model_and_get_pred(training_data, "difficulty", comments_df, "review")
comments_df["quality"] = qual_preds
comments_df["difficulty"] = diff_preds
comments_df["ratings"] = comments_preds
print(comments_df)
grouped = comments_df.groupby('course')
fin_json = []
for name, group in grouped:
    qual = str(group['quality'].mode()[0].item())
    difficulty_v = (group['difficulty'].mode()[0].item())
    ratings_v = (group['ratings'].mode()[0].item())

    confidence_q  = float(len(group[group['quality']==qual])/(len(group['quality'])))
    confidence_d = float(len(group[group['difficulty']==difficulty_v])/(len(group['difficulty'])))
    confidence_r = float(len(group[group['ratings']==ratings_v])/(len(group['ratings'])))
    dict_val = {name: [qual, confidence_q, difficulty_v, confidence_d, ratings_v, confidence_r]}
    fin_json.append(dict_val)
print(fin_json)
# def get_prediction(df, col, target):
#     for index, row in df.iterrows():
#         x_test = tokenize_text(row[col])
#         prediction = train_model(training_data, target).predict(x_test)
#     return prediction
#
# get_prediction(comments_df, "comments", "quality")

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







