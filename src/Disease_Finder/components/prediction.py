import pandas as pd
import pickle
from data_ingestion import DataIngestion
from sklearn.tree import DecisionTreeClassifier

class TrainTestSplit():
    def TrainTest(self,X_train, Y_train, X_test, Y_test, path):
        dt = DecisionTreeClassifier(random_state = 42)
        dt.fit(X_train, Y_train)
        dt.predict(X_test)
        dt.score(X_test, Y_test)

        pickle.dump(dt, path)

    def PatientProfile(self, path):
        df = pd.read_csv(path)

        