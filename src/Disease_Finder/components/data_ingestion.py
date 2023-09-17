import pandas as pd
from sklearn.preprocessing import LabelEncoder
import os 
from logging import Logger
class DataIngestion:

    def Data(self,path_testing, path_training, main_path):
        training = pd.read_csv(path_testing)
        testing = pd.read_csv(path_training)
        training.drop("Unnamed: 133", axis = 1, inplace = True)
        x_train, y_train = training.loc[:,training.columns != "prognosis"], training.loc[:,"prognosis"]
        x_test, y_test = testing.loc[:,training.columns != "prognosis"], testing.loc[:,"prognosis"]

        X_train = pd.DataFrame(x_train)
        Y_train = pd.DataFrame(y_train)
        X_test = pd.DataFrame(x_test)
        Y_test = pd.DataFrame(y_test)
        return {
             X_train.to_csv(main_path,+"/X_train.csv"),
             Y_train.to_csv(main_path,+"/Y_train.csv"),
             X_test.to_csv(main_path,+"/X_test.csv"),
             Y_test.to_csv(main_path,+"/Y_test.csv")}
    

