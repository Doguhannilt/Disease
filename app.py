# Required libraries
import streamlit as st
import pandas as pd
import pickle
import numpy as np
from QuestionAnswering import QuestionAnswer
import wikipedia as wp
import matplotlib.pyplot as plt
from src.Disease_Finder.utils.common import plotting, YesNo,user_input_features


#Disclaimer
st.error("""
         Disclaimer: This webpage is not intended as a substitute for professional medical advice or diagnosis. If you have a serious health concern or medical condition, it is imperative that you seek the guidance and care of a qualified healthcare professional. The information provided here is for informational purposes only and should not be used as a basis for medical decisions. 
         
         Your health is of paramount importance, and only a healthcare provider can provide you with the personalized advice and treatment you may require.""")


#Video 
video_file = open('Images_Videos/doctorlooking.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)
st.write("Made it by AI")

# Disease/Symptom list
diseases_list = ["itching", "skin_rash", "nodal_skin_eruptions", "continuous_sneezing", "shivering","chills", "joint_pain", "stomach_pain", "acidity", "ulcers_on_tongue","muscle_wasting", "vomiting", "burning_micturition", "spotting_ urination", "fatigue","weight_gain", "anxiety", "cold_hands_and_feets", "mood_swings", "weight_loss","restlessness", "lethargy", "patches_in_throat", "irregular_sugar_level", "cough","high_fever", "sunken_eyes", "breathlessness", "sweating", "dehydration", "indigestion","headache", "yellowish_skin", "dark_urine", "nausea", "loss_of_appetite","pain_behind_the_eyes", "back_pain", "constipation", "abdominal_pain", "diarrhoea","mild_fever", "yellow_urine", "yellowing_of_eyes", "acute_liver_failure","fluid_overload", "swelling_of_stomach", "swelled_lymph_nodes", "malaise","blurred_and_distorted_vision", "phlegm", "throat_irritation", "redness_of_eyes","sinus_pressure", "runny_nose", "congestion", "chest_pain", "weakness_in_limbs","fast_heart_rate", "pain_during_bowel_movements", "pain_in_anal_region", "bloody_stool","irritation_in_anus", "neck_pain", "dizziness", "cramps", "bruising", "obesity","swollen_legs", "swollen_blood_vessels", "puffy_face_and_eyes", "enlarged_thyroid","brittle_nails", "swollen_extremeties", "excessive_hunger", "extra_marital_contacts","drying_and_tingling_lips", "slurred_speech", "knee_pain", "hip_joint_pain","muscle_weakness", "stiff_neck", "swelling_joints", "movement_stiffness","spinning_movements", "loss_of_balance", "unsteadiness", "weakness_of_one_body_side","loss_of_smell", "bladder_discomfort", "foul_smell_of urine", "continuous_feel_of_urine","passage_of_gases", "internal_itching", "toxic_look_(typhos)", "depression", "irritability","muscle_pain", "altered_sensorium", "red_spots_over_body", "belly_pain","abnormal_menstruation", "dischromic _patches", "watering_from_eyes", "increased_appetite","polyuria", "family_history", "mucoid_sputum", "rusty_sputum", "lack_of_concentration","visual_disturbances", "receiving_blood_transfusion", "receiving_unsterile_injections","coma", "stomach_bleeding", "distention_of_abdomen", "history_of_alcohol_consumption","fluid_overload.1", "blood_in_sputum", "prominent_veins_on_calf", "palpitations","painful_walking", "pus_filled_pimples", "blackheads", "scurring", "skin_peeling","silver_like_dusting", "small_dents_in_nails", "inflammatory_nails", "blister","red_sore_around_nose", "yellow_crust_ooze"]

# Sidebar - Position selection
symptoms = ["itching", "skin_rash", "nodal_skin_eruptions", "continuous_sneezing", "shivering","chills", "joint_pain", "stomach_pain", "acidity", "ulcers_on_tongue","muscle_wasting", "vomiting", "burning_micturition", "spotting_ urination", "fatigue","weight_gain", "anxiety", "cold_hands_and_feets", "mood_swings", "weight_loss","restlessness", "lethargy", "patches_in_throat", "irregular_sugar_level", "cough","high_fever", "sunken_eyes", "breathlessness", "sweating", "dehydration", "indigestion","headache", "yellowish_skin", "dark_urine", "nausea", "loss_of_appetite","pain_behind_the_eyes", "back_pain", "constipation", "abdominal_pain", "diarrhoea","mild_fever", "yellow_urine", "yellowing_of_eyes", "acute_liver_failure","fluid_overload", "swelling_of_stomach", "swelled_lymph_nodes", "malaise","blurred_and_distorted_vision", "phlegm", "throat_irritation", "redness_of_eyes","sinus_pressure", "runny_nose", "congestion", "chest_pain", "weakness_in_limbs","fast_heart_rate", "pain_during_bowel_movements", "pain_in_anal_region", "bloody_stool","irritation_in_anus", "neck_pain", "dizziness", "cramps", "bruising", "obesity","swollen_legs", "swollen_blood_vessels", "puffy_face_and_eyes", "enlarged_thyroid","brittle_nails", "swollen_extremeties", "excessive_hunger", "extra_marital_contacts","drying_and_tingling_lips", "slurred_speech", "knee_pain", "hip_joint_pain","muscle_weakness", "stiff_neck", "swelling_joints", "movement_stiffness","spinning_movements", "loss_of_balance", "unsteadiness", "weakness_of_one_body_side","loss_of_smell", "bladder_discomfort", "foul_smell_of urine", "continuous_feel_of_urine","passage_of_gases", "internal_itching", "toxic_look_(typhos)", "depression", "irritability","muscle_pain", "altered_sensorium", "red_spots_over_body", "belly_pain","abnormal_menstruation", "dischromic _patches", "watering_from_eyes", "increased_appetite","polyuria", "family_history", "mucoid_sputum", "rusty_sputum", "lack_of_concentration","visual_disturbances", "receiving_blood_transfusion", "receiving_unsterile_injections","coma", "stomach_bleeding", "distention_of_abdomen", "history_of_alcohol_consumption","fluid_overload.1", "blood_in_sputum", "prominent_veins_on_calf", "palpitations","painful_walking", "pus_filled_pimples", "blackheads", "scurring", "skin_peeling","silver_like_dusting", "small_dents_in_nails", "inflammatory_nails", "blister","red_sore_around_nose", "yellow_crust_ooze"]

selected_symptoms = st.multiselect("Select Symptoms", symptoms)
selected_symptoms_variable = selected_symptoms

# Display the selected symptoms
st.text("At least you should select 5 symptoms")
st.write("Selected Symptoms:", selected_symptoms)

#The selected symptoms will be 1, the others will be 0 as a DataFrame
data = {disease: 1 if disease in selected_symptoms else 0 for disease in diseases_list}
df = pd.DataFrame([data.values()], columns=data.keys())

# Load the model (model.pkl)
pickled_model = pickle.load(open('model.pkl', 'rb'))

# Make predictions using the loaded model
prediction = pickled_model.predict(df)

st.subheader("Disease Result")

#Even if all features are zero, it will display heart attack
st.write("'Heart Attack' as default ") 

styled_message = f"""
<div style="background-color:#f0f0f0; padding:20px; border-radius:10px;">
    <p style="font-size:18px; color:#333; text-align:center; margin-bottom:10px;">Your disease may be:</p>
    <h1 style="font-size:24px; color:#0071E3; text-align:center;">{prediction[0]}</h1>
    <p style="font-size:16px; color:#555; text-align:center;">For more details, keep scrolling!</p>
</div>
"""
# Display the styled message
st.markdown(styled_message, unsafe_allow_html=True)


#Note: HuggingFace-Question Answering is already in process but it is not available to save the memory.
################################## QUESTION ANSWERING - HUGGINGFACE (GPT-2) ############################

# Example conversation
# user_input = "What is {prediction[0]}"
# response = generate_response(user_input)
# st.write(response)

# We are going to use TF-IDF because our disease list is not longer enough to run the HuggingFace.
################################### QUESTION ANSWERING - TFIDF ##########################################

Question = prediction[0]
print(Question)
answer = QuestionAnswer("What is" + Question)
styled_message = f"""<br>
<div style="background-color:#D7DBDD  ; padding:20px; border-radius:10px;">
    <p style="font-size:18px; color:#533; text-align:center; margin-bottom:10px;">{answer}</p> <br>
</div>
"""
# Display the styled message
st.markdown(styled_message, unsafe_allow_html=True)
st.text("TF-IDF System.")

# We will get the most similar topics based on the disease that he/she has.
################################### WIKIPEDIA API #####################################################

query = prediction
st.write(" ")
st.subheader("Most Similar Topics Based On")
search_results = wp.search(query, results = 5)

for idx, result in enumerate(search_results, start=1):
    st.markdown(f"**{idx}. {result}**", unsafe_allow_html=True)
st.text("With Wikipedia.")


########################################## WEIGHT VISUALIZER ##########################################

st.title("Symptom Weight Visualizer")
st.info("""        Symptom weight is a numerical value assigned to individual symptoms that 
        signifies their relative importance or significance in a specific context. 
        It is used to rank symptoms,assess their influence on decision-making, 
        and prioritize them based on their relevance.Symptom weights are 
        particularly valuable in healthcare, data analysis, and predictive modeling 
        to improve diagnosis, decision-making, and risk assessment.""")

# Informational message with improved styling
st.markdown(
    """
    <div style="background-color:#f0f0f0; padding:20px; border-radius:10px;">
    <p style="font-size:18px; color:#333; text-align:center; margin-bottom:10px;">Welcome to the Symptom Weight Visualizer!</p>
    <p style="font-size:16px; color:#555; text-align:center;">Explore how your selected symptoms may affect your body within 2 days.</p>
    </div>
   <br> """,
    unsafe_allow_html=True
)

fig = plotting("C:/Users/doguy/Desktop/Disease Finder (V2)/Data/symptom_severity.csv", selected_symptoms)

# Display the single plot if it exists
if fig:
    st.pyplot(fig)
else:
    st.warning("No data available for the selected symptoms.")


# "Patient Profile" is going to tell your disease based on your characteristic profile.
######################################  PATIENT PROFILE ###############################################

st.sidebar.header("Patient Profile")
st.sidebar.write("This sidebar is going to tell you what is your disease based on your patient profile.")
st.sidebar.text("Default is 'Influenza' as a disease.")

take_input = user_input_features()
predict_user = YesNo(take_input)
pickled_model_user_input = pickle.load(open('knn_model.pkl', 'rb'))
predicted = pickled_model_user_input.predict(np.array(predict_user))

st.sidebar.code(predicted[0]+" is might be your disease")
st.sidebar.image("Images_Videos/doctor.png",width=300)

