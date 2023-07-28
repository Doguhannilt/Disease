import tensorflow as tf
import pandas as pd

class Prediction:
    def __init__(self):
        self.model_path = None
        self.loaded_model = None

    def load_model(self, model_path):
        self.model_path = model_path
        self.loaded_model = tf.saved_model.load(self.model_path)

    def prediction(self, input_df):
        if self.loaded_model is None:
            raise ValueError("The model has not been loaded. Please call 'load_model()' before making predictions.")

        input_data = input_df.to_numpy()
        result = self.loaded_model.signatures['serving_default'](dense_12_input=tf.constant(input_data))
        return result