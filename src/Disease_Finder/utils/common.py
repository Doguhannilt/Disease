import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


def WriteintoText(df):
    items = df["Disease"].unique()  # Get unique values from the "Disease" column

    with open('items.txt', 'w') as tfile:
        tfile.write('\n'.join(items))



def CleaningCSV(path_with_csv, column):

    df = pd.read_csv(path_with_csv)
    df[column] = df[column].str.replace("_", " ").str.replace("(", "").str.replace(")", "").str.strip().str.capitalize()
    return df

#####################################################CHATGPT############################################3
# -> PATH: "C:/Users/doguy/Desktop/Disease Finder (V2)/Data/regular_severity.csv"
def plotting(path, selected_symptoms):
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np

    # Load the data from the CSV file
    Symptom_weight_visualizer = pd.read_csv(path)

    # Filter the data based on selected symptoms
    filtered_data = Symptom_weight_visualizer[Symptom_weight_visualizer["Symptom"].isin(selected_symptoms)]

    if not filtered_data.empty:
        fig, ax = plt.subplots()
        colors = plt.cm.viridis(np.linspace(0, 1, len(filtered_data)))  # Use a color map for different colors
        bars = ax.bar(filtered_data["Symptom"], filtered_data["Symptom_severity"], color=colors)
        plt.xticks(rotation=45, ha="right")
        plt.xlabel("Symptom")
        plt.ylabel("Weight")
        plt.title("Symptom Weight Chart")

        # Add labels with values above each bar
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f"{height}",
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha="center", va="bottom")

        # Customize the color bar
        color_bar = plt.colorbar(plt.cm.ScalarMappable(cmap=plt.cm.viridis))
        color_bar.set_label("Color")

        return fig  # Return the figure object

    else:
        return None  # Return None if no data is available for the selected symptoms
######################################################################################################

def YesNo(df):
    df['Fever'] = df['Fever'].apply(lambda x: 1 if x == 'Yes' else (0 if x == 'No' else x))
    df['Cough'] = df['Cough'].apply(lambda x: 1 if x == 'Yes' else (0 if x == 'No' else x))
    df['Fatigue'] = df['Fatigue'].apply(lambda x: 1 if x == 'Yes' else (0 if x == 'No' else x))
    df['Difficulty_Breathing'] = df['Difficulty_Breathing'].apply(lambda x: 1 if x == 'Yes' else (0 if x == 'No' else x))
    df['Gender'] = df['Gender'].apply(lambda x: 1 if x == 'Yes' else (0 if x == 'No' else x))
    df['Blood_Pressure'] = df['Blood_Pressure'].apply(lambda x: 1 if x == 'High' else (2 if x == 'Normal' else (3 if x == 'Low' else x)))
    df['Cholesterol_Level'] = df['Cholesterol_Level'].apply(lambda x: 1 if x == 'High' else (2 if x == 'Normal' else (3 if x == 'Low' else x)))

    return df

def user_input_features():
    Fever = st.sidebar.select_slider('Fever', ('Yes','No'))
    Cough = st.sidebar.select_slider('Cough', ('Yes', 'No'))
    Fatigue = st.sidebar.select_slider('Fatigue', ('Yes', 'No'))
    Difficulty_Breathing = st.sidebar.select_slider('Difficulty Breathing', ('Yes', 'No'))
    Age = st.sidebar.slider('Age',0,50)
    Gender = st.sidebar.select_slider('Gender', ('Yes', 'No'))
    Blood_Pressure = st.sidebar.select_slider('Blood Pressure', ('High', 'Normal', 'Low'))
    Cholesterol_Level = st.sidebar.select_slider('Cholesterol Level', ('High', 'Normal', 'Low'))
    data = {'Fever': Fever,
            'Cough': Cough,
            'Fatigue': Fatigue,
            'Difficulty_Breathing': Difficulty_Breathing,
            'Age': Age,
            'Gender': Gender,
            'Blood_Pressure': Blood_Pressure,
            'Cholesterol_Level': Cholesterol_Level,}
    features = pd.DataFrame(data, index=[0])
    return features