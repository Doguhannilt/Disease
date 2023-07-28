from flask import Flask, request, render_template
from flask_cors import CORS
import pandas as pd
import numpy as np
import joblib
import sklearn
from imblearn.over_sampling import SMOTENC
from flask import Flask, request, jsonify
from collections import Counter
import matplotlib.pyplot as plt
import ast






import pandas as pd




diseases_list = ['Drying and tingling lips', 'Slurred speech', 'Swollen legs', 'Blurred and distorted vision',
                 'Abdominal pain', 'Dizziness', 'Lethargy', 'Swollen blood vessels', 'Hip joint pain',
                 'Swelling joints', 'Foul smell of urine', 'Stiff neck', 'Swelling of stomach', 'Obesity',
                 'Nodal skin eruptions', 'Receiving blood transfusion', 'Passage of gases', 'Muscle wasting',
                 'Brittle nails', 'Ulcers on tongue', 'Watering from eyes', 'Cramps', 'Yellowish skin', 'Malaise',
                 'Lack of concentration', 'Scurring', 'Spotting urination', 'Nausea', 'Fluid overload',
                 'Pain during bowel movements', 'Irritability', 'Coma', 'Patches in throat', 'Blister',
                 'Irregular sugar level', 'Itching', 'Fatigue', 'Constipation', 'Palpitations', 'Toxic look (typhos)']


with open('selected_disease.txt', 'r') as file:
    text = [disease.strip() for disease in file.read().split(',')]

selected_diseases_list = [disease.strip() for disease in text if disease.strip()]

print("Selected diseases from the file:", selected_diseases_list)

        # Create a dictionary with each disease as key and a list of binary values (0 or 1) as value
data = {disease: 1 if disease in selected_diseases_list else 0 for disease in diseases_list}

        # Create a DataFrame from a list of dictionaries with a single row
df = pd.DataFrame([data])
df = df.iloc[:,:40]

print(df.shape)
        # Count the number of 1s and 0s
num_ones = df.sum(axis=1)[0]
num_zeros = len(df.columns) - num_ones
print("1 Number is {}, 0 number is {}".format(num_ones, num_zeros))


print("df, isnull->:",df.isnull().sum())


regular = pd.read_csv("Original_Dataset.csv")

columns_to_check = []
for col in regular.columns:
    if col != 'Disease':
        columns_to_check.append(col)
symptoms = regular.iloc[:, 1:].values.flatten()
symptoms = list(set(symptoms))

for symptom in symptoms:
    regular[symptom] = regular.iloc[:, 1:].apply(lambda row: int(symptom in row.values), axis=1)

regular_1 = regular.drop(columns=columns_to_check)
regular_1 = regular_1.loc[:, regular_1.columns.notna()]

regular_1.columns = regular_1.columns.str.strip()

regular.drop( ["Symptom_1","Symptom_2","Symptom_3","Symptom_4","Symptom_5","Symptom_6","Symptom_7","Symptom_8","Symptom_9","Symptom_10","Symptom_11","Symptom_12","Symptom_13","Symptom_14","Symptom_15",], axis = 1, inplace = True)
regular.drop(["Symptom_16","Symptom_17"], axis = 1 , inplace = True)

from sklearn.preprocessing import LabelEncoder

#create instance of label encoder
lab = LabelEncoder()

#perform label encoding on 'team' column
regular_1['Disease'] = lab.fit_transform(regular_1['Disease'])


from sklearn.model_selection import train_test_split
X = regular_1.drop("Disease", axis = 1)
y = regular_1["Disease"]
X = X = X.iloc[:, :40]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size = 0.2)

from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, ConfusionMatrixDisplay
import numpy as np

X_train = np.array(X_train)  # Convert X_train to a NumPy array if it's not already one
y_train = np.array(y_train)  # Convert y_train to a NumPy array if it's not already one
X_test = np.array(X_test)    # Convert X_test to a NumPy array if it's not already one

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
df=df.to_numpy()
df = df.reshape(1, -1)[:, :40]  # Use only the first 131 columns
print("Shape of df:", df.shape)
print("Shape of y_test:", y_test.shape)

y_preds = knn.predict(df)
print(y_preds)

# First prediction is 31 (Gastroenteritis)
# Second prediction is 2 (Hepatitis E)
# Third prediction is 32 (Bronchial Asthma)
# 4.prediction is 2 (Hepatitis E)
# 5.prediction is 7 (Common Cold)
# 6.prediction is 40 (Dengue)

dict = {"1.Exp: ", 31,
        "2.Exp: ", 2,
        "3.Exp: ", 32,
        "4.Exp: ", 2,
        "5.Exp: ", 7,
        "6.Exp: ", 40}