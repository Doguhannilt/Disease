import pandas as pd
import numpy as np




class NumericalSystem:
    def System(self):
    
    
        """
        X_test suchlike list -> Diseases_list
        """
        diseases_list = ['inflammatory_nails','sunken_eyes','cramps', 'passage_of_gases','muscle_pain','bruising','weakness_in_limbs','watering_from_eyes','receiving_unsterile_injections','fast_heart_rate','skin_peeling','fluid_overload','puffy_face_and_eyes','weight_loss','itching','toxic_look_(typhos)', 'polyuria','pain_during_bowel_movements','stomach_pain','irritation_in_anus', 'restlessness','altered_sensorium','yellow_urine','joint_pain','mucoid_sputum', 'fatigue','ulcers_on_tongue','obesity','bloody_stool','red_spots_over_body','distention_of_abdomen','hip_joint_pain','dizziness','dehydration','extra_marital_contacts','receiving_blood_transfusion','mild_fever','swelling_of_stomach','redness_of_eyes','pain_in_anal_region']

        """
        Selected Diseases is your chooses
        """

        with open('selected_disease.txt', 'r') as file:
            text = file.read().splitlines()
            
        # Create a dictionary with each disease as key and a list of binary values (0 or 1) as value
        data = {disease: [] for disease in diseases_list}

        """
        Loop through each item in 'text' and check if each disease in 'diseases_list' exists in the item
        """
        for item in text:
            for disease in diseases_list:
                if disease in item:
                    data[disease].append(1)
                else:
                    data[disease].append(0)

        # Create a DataFrame from the dictionary
        df = pd.DataFrame(data)
        return df
