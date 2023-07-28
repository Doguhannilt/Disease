# -*- coding: utf-8 -*-
"""Disease Using Deep Learning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14U6nsfz5tzv9-6fAfqmCstWY7cfJzQ5w
"""

import pandas as pd
df = pd.read_csv("/content/Original_Dataset.csv")

"""Exploring"""

df.head(10)

df.columns

df["Disease"].value_counts().sum()

df["Symptom_17"].value_counts().sum()

df.isnull().sum()

df["Symptom_1"].value_counts()

"""Make your row values a columns (as binary) in your dataset

# def Make(independent_variable, data_name):
    
    '''
    This method used to convert your row values into columns as binary.
    '''
    
    columns_to_check = [] # The columns which is our X
    for column in data_name.columns:
        if column != independent_variable:
            columns_to_check.append(column) #For each column, it checks whether the column name is not equal to the independent_variable
    
    Symptoms = data_name.iloc[:, 1:].values.flatten()
    '''
    The code snippet data_name.iloc[:, 1:] is used to select all rows and all columns starting from the second column (index 1) until the last column of the DataFrame data_name.
    '''
    Symptoms = list(set(Symptoms))

    '''
    Make everything simple list
    '''
    
    for symptom in Symptoms:
        data_name[symptom] = data_name.iloc[:, 1:].apply(lambda row: int(symptom in row.values), axis=1)
    
    data = data_name.loc[:, data_name.columns.notna()]
    data.columns = data.columns.str.strip()

    '''
    The code iterates through each symptom in the list Symptoms.
    For each symptom, it uses the apply method along with a lambda function to check whether that symptom is present in each row of the DataFrame data_name.
    The result of the apply operation is assigned to a new column with the name of the current symptom in the DataFrame data_name. This new column will contain 1 if the symptom is present in the row and 0 if it is not.
    The DataFrame data_name is then modified to remove any columns that have all missing values (NaN) using data_name.loc[:, data_name.columns.notna()]. This step drops any columns that were added for symptoms that were not present in the original data.
    Lastly, the code uses data.columns.str.strip() to remove any leading or trailing whitespace from the column names in the DataFrame data.
    
    Credit: I saw  some pieces of this code in Kaggle (Username: ARVINDH) THANKS!
    '''
"""

regular = pd.read_csv("/content/Original_Dataset.csv")

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

regular.head(5)

regular.drop(["Symptom_16","Symptom_17"], axis = 1 , inplace = True)

"""Get a list of the name of diseases"""

diseases_list = ['Fungal infection', 'Hepatitis C', 'Hepatitis E', 'Alcoholic hepatitis',
                'Tuberculosis', 'Common Cold', 'Pneumonia',
                'Dimorphic hemmorhoids(piles)', 'Heart attack', 'Varicose veins',
                'Hypothyroidism', 'Hyperthyroidism', 'Hypoglycemia', 'Osteoarthristis',
                'Arthritis', '(vertigo) Paroymsal  Positional Vertigo', 'Acne',
                'Urinary tract infection', 'Psoriasis', 'Hepatitis D', 'Hepatitis B',
                'Allergy', 'hepatitis A', 'GERD', 'Chronic cholestasis',
                'Drug Reaction', 'Peptic ulcer diseae', 'AIDS', 'Diabetes ',
                'Gastroenteritis', 'Bronchial Asthma', 'Hypertension ', 'Migraine',
                'Cervical spondylosis', 'Paralysis (brain hemorrhage)', 'Jaundice',
                'Malaria', 'Chicken pox', 'Dengue', 'Typhoid', 'Impetigo']

# Create a dictionary using dictionary comprehension
diseases_dict = {i + 1: disease for i, disease in enumerate(diseases_list)}

regular_1.head(5)

regular_1["Disease"].value_counts().keys()

# I'll make a list for understanding the labels in our dataset

dict = 41
Names = []
for i in range(dict):
  system = regular_1["Disease"].value_counts().keys()[i] , "--->" , df["Disease"].value_counts().keys()[i]
  Names.append(system)

Names[:4]

regular_1

regular_1["Disease"].value_counts().keys()

from sklearn.preprocessing import LabelEncoder

#create instance of label encoder
lab = LabelEncoder()

#perform label encoding on 'team' column
regular_1['Disease'] = lab.fit_transform(regular_1['Disease'])

df.Disease.head(6)

"""Splitting"""

from sklearn.model_selection import train_test_split
X = regular_1.drop("Disease", axis = 1)
y = regular_1["Disease"]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size = 0.2)

X.shape, y.shape

"""Modeling"""

import tensorflow as tf
import numpy as np

X

y_train

model_1 = tf.keras.Sequential([
    tf.keras.layers.Dense(4, activation = "relu"),
    tf.keras.layers.Dense(4, activation = "relu"),
    tf.keras.layers.Dense(150, activation = "softmax")
])

model_1.compile(
    loss = tf.keras.losses.SparseCategoricalCrossentropy(),
    optimizer = tf.keras.optimizers.Adam(lr = 0.01),
    metrics = ["accuracy"]
)

non_norm_history = model_1.fit(X_train, y_train, epochs = 50 )

"""Summary for Our Model"""

model_1.summary()

"""Check the Accuracy Of Our Model"""

# Check the accuracy of our model

loss, accuracy = model_1.evaluate(X_test, y_test)
print(f"Model loss on the test set: {loss}")
print(f"Model accuracy on the test set: {(accuracy*100):.0f}%")
# Make predictions
y_pred = model_1.predict(X_test)

"""#An algorithm for finding disease

* Get an input (cold_hands_and_feets, internal_itching. etc...)
* Check the inputs are exist in our dataset as a column
* Write "1" for the columns that we've got , else 0 for the other columns
* Predict with our model
* Get an output as numerical (13,52,36,75)
* Compare the output and disease_dict
* Return results
"""

X.columns.value_counts().sum()

model_1.save("/content/Model_1")



