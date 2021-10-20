import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

df = pd.read_csv("static/data/Iris.csv")
df = df.drop("Id",axis = 1)
X = df.loc[:, df.columns != 'Species']
y = df['Species']
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.25)

model = RandomForestClassifier()
model.fit(X_train, y_train)

# save the model to disk
pickle.dump(model, open('model.pkl', 'wb'))

# # some time later...
#
# # load the model from disk
# loaded_model = pickle.load(open(filename, 'rb'))
# result = loaded_model.score(X_test, y_test)
# print(result)
#
#
# ########## User input would go here:
# sepal_length = .5
# sepal_width = .5
# petal_length = .5
# petal_width = .5
# data = np.array([sepal_length, sepal_width, petal_length, petal_width])
# data = data.reshape(1, -1)
# # print(test_data)
# prediction = loaded_model.predict(data)