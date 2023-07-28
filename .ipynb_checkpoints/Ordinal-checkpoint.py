{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 386,
   "id": "76cb7295",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "class Ordinal():\n",
    "    def System(self):\n",
    "        \"\"\"\n",
    "        X_test suchlike list -> Diseases_list\n",
    "        \"\"\"\n",
    "        diseases_list = ['enlarged_thyroid', 'cramps', 'stomach_pain', 'movement_stiffness', 'passage_of_gases', 'family_history', 'nausea', 'headache', 'dischromic_patches', 'altered_sensorium', 'back_pain', 'irregular_sugar_level', 'lack_of_concentration', 'brittle_nails', 'watering_from_eyes', 'abnormal_menstruation', 'pus_filled_pimples', 'spinning_movements', 'anxiety', 'slurred_speech', 'weakness_of_one_body_side', 'stiff_neck', 'palpitations', 'irritability', 'throat_irritation', 'runny_nose', 'phlegm', 'inflammatory_nails', 'belly_pain', 'receiving_unsterile_injections', 'neck_pain', 'patches_in_throat', 'prominent_veins_on_calf', 'lethargy', 'internal_itching', 'shivering', 'dark_urine', 'swelling_of_stomach', 'loss_of_smell', 'swelling_joints', 'small_dents_in_nails', 'weakness_in_limbs', 'ulcers_on_tongue', 'bruising', 'dizziness', 'sinus_pressure', 'skin_peeling', 'cough', 'muscle_wasting', 'silver_like_dusting', 'swollen_legs', 'cold_hands_and_feets', 'fluid_overload', 'painful_walking', 'chills', 'mucoid_sputum', 'scurring', 'visual_disturbances', 'joint_pain', 'yellow_crust_ooze', 'nodal_skin_eruptions', 'red_sore_around_nose', 'muscle_weakness', 'burning_micturition', 'abdominal_pain', 'indigestion', 'muscle_pain', 'coma', 'loss_of_balance', 'swollen_blood_vessels', 'swelled_lymph_nodes', 'increased_appetite', 'sweating', 'mild_fever', 'hip_joint_pain', 'chest_pain', 'continuous_sneezing', 'congestion', 'spotting_urination', 'fatigue', 'pain_behind_the_eyes', 'distention_of_abdomen', 'pain_in_anal_region', 'red_spots_over_body', 'weight_gain', 'mood_swings', 'acidity', 'breathlessness', 'redness_of_eyes', 'blackheads', 'loss_of_appetite', 'history_of_alcohol_consumption', 'dehydration', 'diarrhoea', 'rusty_sputum', 'depression', 'acute_liver_failure', 'bladder_discomfort', 'high_fever', 'polyuria', 'vomiting', 'drying_and_tingling_lips', 'weight_loss', 'malaise', 'blister', 'yellowish_skin', 'restlessness', 'foul_smell_of_urine', 'blurred_and_distorted_vision', 'extra_marital_contacts', 'obesity', 'pain_during_bowel_movements', 'irritation_in_anus', 'yellow_urine', 'constipation', 'skin_rash', 'swollen_extremeties', 'itching', 'toxic_look_(typhos)', 'excessive_hunger', 'unsteadiness', 'stomach_bleeding', 'continuous_feel_of_urine', 'sunken_eyes', 'blood_in_sputum', 'fast_heart_rate', 'knee_pain', 'yellowing_of_eyes', 'puffy_face_and_eyes', 'bloody_stool', 'receiving_blood_transfusion', 'Fungal infection', 'Hepatitis C', 'Hepatitis E', 'Alcoholic hepatitis', 'Tuberculosis', 'Common Cold', 'Pneumonia', 'Dimorphic hemmorhoids(piles)', 'Heart attack', 'Varicose veins', 'Hypothyroidism', 'Hyperthyroidism', 'Hypoglycemia', 'Osteoarthristis', 'Arthritis', '(vertigo) Paroymsal  Positional Vertigo', 'Acne', 'Urinary tract infection', 'Psoriasis', 'Hepatitis D', 'Hepatitis B', 'Allergy', 'hepatitis A', 'GERD', 'Chronic cholestasis', 'Drug Reaction', 'Peptic ulcer diseae', 'AIDS', 'Diabetes ', 'Gastroenteritis', 'Bronchial Asthma', 'Hypertension ', 'Migraine', 'Cervical spondylosis', 'Paralysis (brain hemorrhage)', 'Jaundice', 'Malaria', 'Chicken pox', 'Dengue', 'Typhoid', 'Impetigo']        \n",
    "\n",
    "        \"\"\"\n",
    "        Selected Diseases is your chooses\n",
    "        \"\"\"\n",
    "        \n",
    "        sys = ['Fungal infection', 'Hepatitis C', 'Hepatitis E', 'Alcoholic hepatitis',\n",
    "                'Tuberculosis', 'Common Cold', 'Pneumonia',\n",
    "                'Dimorphic hemmorhoids(piles)', 'Heart attack', 'Varicose veins',\n",
    "                'Hypothyroidism', 'Hyperthyroidism', 'Hypoglycemia', 'Osteoarthristis',\n",
    "                'Arthritis', '(vertigo) Paroymsal  Positional Vertigo', 'Acne',\n",
    "                'Urinary tract infection', 'Psoriasis', 'Hepatitis D', 'Hepatitis B',\n",
    "                'Allergy', 'hepatitis A', 'GERD', 'Chronic cholestasis',\n",
    "                'Drug Reaction', 'Peptic ulcer diseae', 'AIDS', 'Diabetes ',\n",
    "                'Gastroenteritis', 'Bronchial Asthma', 'Hypertension ', 'Migraine',\n",
    "                'Cervical spondylosis', 'Paralysis (brain hemorrhage)', 'Jaundice',\n",
    "                'Malaria', 'Chicken pox', 'Dengue', 'Typhoid', 'Impetigo']\n",
    "        \n",
    "        for s in sys:\n",
    "            if s not in diseases_list:\n",
    "                diseases_list.append(s)\n",
    "\n",
    "        with open('selected_diseases.txt', 'r') as file:\n",
    "            text = file.read().splitlines()\n",
    "            \n",
    "        # Create a dictionary with each disease as key and a list of binary values (0 or 1) as value\n",
    "        data = {disease: [] for disease in diseases_list}\n",
    "\n",
    "        \"\"\"\n",
    "        Loop through each item in 'text' and check if each disease in 'diseases_list' exists in the item\n",
    "        \"\"\"\n",
    "        for item in text:\n",
    "            for disease in diseases_list:\n",
    "                if disease in item:\n",
    "                    data[disease].append(1)\n",
    "                else:\n",
    "                    data[disease].append(0)\n",
    "\n",
    "        # Create a DataFrame from the dictionary\n",
    "        df = pd.DataFrame(data)\n",
    "        \n",
    "        # Print the DataFrame\n",
    "        return df.head(5)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "93270dfe",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
