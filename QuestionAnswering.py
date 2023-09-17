from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Sample documents for medical conditions

documents = [
    # Fungal Infection
    [
        "Fungal infections, also known as mycoses, are caused by various types of fungi, including yeast, molds, and dermatophytes. These infections can affect different parts of the body, such as the skin, nails, genitals, throat, and lungs.",
        "Symptoms range from mild itching and redness to severe complications, depending on the type and location of the infection. Common fungal infections include athlete's foot, ringworm, candidiasis, and fungal pneumonia.",
        "Treatment involves antifungal medications, which may be topical creams, oral drugs, or intravenous therapy, depending on the severity of the infection.",
        "Preventive measures include maintaining good hygiene and avoiding risk factors such as excessive moisture and weakened immunity."
    ],

    # Allergy
    [
        "Allergies are immune system responses to allergens, substances that are typically harmless but trigger an exaggerated immune reaction. Common allergens include pollen, dust mites, pet dander, certain foods, and insect stings.",
        "Allergic reactions can manifest as sneezing, runny nose, itching, swelling, hives, or even life-threatening anaphylaxis. Diagnosis is often done by allergists through skin tests or blood tests.",
        "Types of Allergic Reactions: Allergic reactions can be categorized into immediate hypersensitivity (IgE-mediated) and delayed hypersensitivity (T-cell-mediated) reactions. Immediate hypersensitivity reactions, such as hay fever and food allergies, typically occur within minutes to hours after exposure to an allergen. Delayed hypersensitivity reactions, such as contact dermatitis from poison ivy, develop over a period of days.",
        "Management and Treatment: Managing allergies involves allergen avoidance, which may include lifestyle modifications like keeping a pet-free home for animal allergies or avoiding certain foods for food allergies.",
        "Antihistamines can help relieve mild symptoms, while corticosteroids are used for more severe reactions. In cases of severe anaphylaxis, epinephrine injections may be required.",
        "Allergen immunotherapy, often called allergy shots, is a long-term treatment option that can desensitize the immune system to specific allergens."
    ],

    # GERD (Gastroesophageal Reflux Disease)
    [
        "GERD is a digestive disorder characterized by the backflow of stomach acid into the esophagus. Symptoms include heartburn, regurgitation, and chest pain.",
        "Lifestyle changes, such as diet modification and elevation of the head during sleep, can help manage GERD. Medications like proton pump inhibitors (PPIs) and antacids are also used for treatment."
    ],

    # Chronic Cholestasis
    [
        "Chronic cholestasis is a condition characterized by the reduced flow of bile from the liver. It can lead to the accumulation of bile acids in the liver and can cause jaundice, itching, and fatigue.",
        "Treatment aims to manage the underlying cause and may include medications to relieve symptoms and improve bile flow. In severe cases, liver transplantation may be necessary."
    ],

    # Drug Reaction
    [
        "Drug reactions refer to adverse reactions or side effects caused by medications. These reactions can range from mild rashes and nausea to severe allergic reactions.",
        "Treatment involves discontinuing the offending medication and managing symptoms. In severe cases, medical intervention may be needed."
    ],

    # Peptic Ulcer Disease
    [
        "Peptic ulcer disease involves the development of open sores in the lining of the stomach, small intestine, or esophagus. It can result from factors like infection with H. pylori bacteria, long-term use of nonsteroidal anti-inflammatory drugs (NSAIDs), and excessive acid production.",
        "Treatment includes antibiotics to eradicate H. pylori, medications to reduce stomach acid, and lifestyle modifications to promote healing and prevent recurrence."
    ],

    # AIDS (Acquired Immunodeficiency Syndrome)
    [
        "AIDS is a late stage of HIV infection where the immune system is severely damaged, making the individual susceptible to opportunistic infections and certain cancers.",
        "Treatment involves antiretroviral therapy (ART) to suppress the HIV virus and support the immune system. Preventive measures include safe sex practices and needle exchange programs."
    ],

    # Diabetes
    [
        "Diabetes is a chronic condition characterized by high blood sugar levels. There are two main types: Type 1 (autoimmune) and Type 2 (lifestyle-related).",
        "Management includes blood sugar monitoring, medication or insulin therapy, dietary changes, and regular physical activity. Complications can include heart disease, kidney problems, and nerve damage."
    ],

    # Gastroenteritis
    [
        "Gastroenteritis, often referred to as stomach flu, is an inflammation of the stomach and intestines. It can result from viral or bacterial infections and causes symptoms like diarrhea, vomiting, and abdominal pain.",
        "Treatment focuses on rehydration and symptom relief. In severe cases, medical attention may be required to address dehydration."
    ],

    # Bronchial Asthma
    [
        "Bronchial asthma is a chronic respiratory condition characterized by airway inflammation and hypersensitivity. It leads to recurrent episodes of wheezing, shortness of breath, and coughing.",
        "Treatment includes bronchodilator medications to relieve symptoms and anti-inflammatory drugs for long-term control. Asthma action plans help individuals manage their condition."
    ],

    # Hypertension (High Blood Pressure)
    [
        "Hypertension is a condition where blood pressure in the arteries is consistently too high. It can lead to serious health issues, including heart disease and stroke.",
        "Management involves lifestyle changes such as a heart-healthy diet, exercise, and medication if necessary. Regular blood pressure monitoring is crucial for control."
    ],

    # Migraine
    [
        "Migraine is a neurological disorder characterized by recurrent, severe headaches that often include nausea, vomiting, and sensitivity to light and sound.",
        "Treatment includes pain-relief medications, preventive medications, and lifestyle changes. Identifying and avoiding migraine triggers is an important part of management."
    ],

    # Cervical Spondylosis
    [
        "Cervical spondylosis is a degenerative condition of the cervical spine (neck). It involves the wear and tear of spinal disks and joints, leading to neck pain, stiffness, and sometimes radiating arm pain.",
        "Treatment includes pain management, physical therapy, and in some cases, surgery to relieve pressure on nerve roots."
    ],

    # Paralysis (Brain Hemorrhage)
    [
        "Paralysis can result from a brain hemorrhage, which is bleeding in the brain. It can lead to loss of movement or function in parts of the body depending on the affected area of the brain.",
        "Treatment depends on the cause and extent of brain damage. Rehabilitation and physical therapy are often necessary to regain function."
    ],

    # Jaundice
    [
        "Jaundice is a yellowing of the skin and eyes due to elevated levels of bilirubin in the blood. It can be a symptom of various underlying medical conditions, including liver disease, hemolysis, or biliary obstruction.",
        "Treatment involves addressing the underlying cause. For example, liver disease may require medications or lifestyle changes, while biliary obstruction may need surgical intervention."
    ],

    # Malaria
    [
        "Malaria is a mosquito-borne infectious disease caused by the Plasmodium parasite. It leads to recurring fevers, chills, and flu-like symptoms.",
        "Prevention includes the use of insecticide-treated bed nets and antimalarial medications when traveling to endemic areas. Treatment involves antimalarial drugs."
    ],

    # Chickenpox
    [
        "Chickenpox, caused by the varicella-zoster virus, results in an itchy rash, fever, and flu-like symptoms. It is highly contagious.",
        "Treatment focuses on symptom relief, including antiviral medications in some cases. Vaccination has significantly reduced the incidence of chickenpox."
    ],

    # Dengue
    [
        "Dengue is a mosquito-borne viral infection that can cause high fever, severe joint and muscle pain, bleeding, and potentially life-threatening dengue hemorrhagic fever or dengue shock syndrome.",
        "There is no specific antiviral treatment for dengue. Supportive care and fluid replacement are crucial for management."
    ],

    # Typhoid
    [
        "Typhoid fever is a bacterial infection caused by Salmonella Typhi. It leads to high fever, abdominal pain, and gastrointestinal symptoms.",
        "Treatment involves antibiotics, and preventive measures include vaccination and safe food and water practices."
    ],

    # Hepatitis A, B, C, D, E
    [

        "Hepatitis refers to inflammation of the liver, and it can be caused by various viruses, including hepatitis A, B, C, D, and E. Each type has its own mode of transmission and potential complications.",
        "Treatment and management vary depending on the type of hepatitis. Vaccination is available for hepatitis A and B. Antiviral medications are used for hepatitis B and C, and supportive care is provided for hepatitis A, D, and E."
    ],

    # Alcoholic Hepatitis
    [
        "Alcoholic hepatitis is a liver inflammation caused by excessive alcohol consumption. It can lead to liver damage, jaundice, and ascites.",
        "Treatment involves abstinence from alcohol, nutritional support, and medications to manage symptoms and prevent complications."
    ],

    # Tuberculosis (TB)
    [
        "Tuberculosis is a bacterial infection caused by Mycobacterium tuberculosis. It primarily affects the lungs (pulmonary TB) but can also involve other organs (extrapulmonary TB).",
        "Treatment includes a combination of antibiotics taken for several months. TB control measures are essential to prevent its spread."
    ],

    # Common Cold
    [
        "The common cold is a viral respiratory infection characterized by symptoms like runny nose, sore throat, coughing, and sneezing. It is usually mild and self-limiting.",
        "Treatment involves rest, hydration, and over-the-counter cold medications to relieve symptoms. There is no cure for the common cold."
    ],

    # Pneumonia
    [
        "Pneumonia is a lung infection that can be caused by bacteria, viruses, or fungi. It leads to symptoms such as fever, cough, and difficulty breathing.",
        "Treatment depends on the cause and severity and may involve antibiotics for bacterial pneumonia, antivirals for viral pneumonia, and supportive care to manage symptoms."
    ],

    # Dimorphic Hemorrhoids (Piles)
    [
        "Hemorrhoids, also known as piles, are swollen blood vessels in the rectum or anus. They can cause pain, bleeding, and itching.",
        "Treatment includes dietary changes, topical creams, and in some cases, surgical procedures to remove or shrink hemorrhoids."
    ],

    # Heart Attack
    [
        "A heart attack, or myocardial infarction, occurs when blood flow to the heart muscle is blocked, usually by a blood clot. It results in chest pain, shortness of breath, and potential heart muscle damage.",
        "Immediate medical attention is crucial for heart attack treatment. Treatments may include medications, angioplasty, and lifestyle changes to reduce the risk of future heart attacks."
    ],

    # Varicose Veins
    [
        "Varicose veins are swollen, twisted veins that usually occur in the legs. They can cause pain, discomfort, and cosmetic concerns.",
        "Treatment options range from lifestyle changes and compression stockings to minimally invasive procedures or surgery for severe cases."
    ],

    # Hypothyroidism
    [
        "Hypothyroidism is a condition where the thyroid gland doesn't produce enough thyroid hormones. It can lead to symptoms like fatigue, weight gain, and cold intolerance.",
        "Treatment involves thyroid hormone replacement therapy to normalize hormone levels and relieve symptoms."
    ],

    # Hyperthyroidism
    [
        "Hyperthyroidism is a condition where the thyroid gland produces too many thyroid hormones. It can result in symptoms like weight loss, anxiety, and rapid heartbeat.",
        "Treatment aims to reduce thyroid hormone production and may include medications, radioactive iodine therapy, or surgery."
    ],

    # Hypoglycemia
    [
        "Hypoglycemia, or low blood sugar, occurs when blood glucose levels drop too low. It can lead to symptoms such as dizziness, sweating, and confusion.",
        "Treatment involves consuming glucose or carbohydrates to raise blood sugar levels. Managing the underlying cause, such as adjusting diabetes medications, is important."
    ],

    # Osteoarthritis
    [
        "Osteoarthritis is a degenerative joint disease that causes pain, stiffness, and reduced joint mobility. It commonly affects weight-bearing joints like the knees and hips.",
        "Treatment includes pain management, physical therapy, lifestyle modifications, and, in severe cases, joint replacement surgery."
    ],

    # Arthritis
    [
        "Arthritis refers to inflammation of the joints and encompasses various types, including osteoarthritis, rheumatoid arthritis, and psoriatic arthritis.",
        "Treatment depends on the specific type of arthritis and may include medications, physical therapy, lifestyle changes, and joint protection strategies."
    ],

    # (Vertigo) Paroxysmal Positional Vertigo
    [
        "Paroxysmal positional vertigo (BPPV) is a type of vertigo characterized by brief episodes of spinning dizziness triggered by changes in head position.",
        "Treatment involves maneuvers to reposition displaced inner ear crystals. These maneuvers can resolve BPPV and alleviate symptoms."
    ],

    # Acne
    [
        "Acne is a skin condition that causes pimples, blackheads, and whiteheads. It can affect the face, chest, and back and is often associated with hormonal changes.",
        "Treatment includes topical and oral medications, lifestyle modifications, and skincare routines tailored to the severity of acne."
    ],

    # Urinary Tract Infection
    [
        "A urinary tract infection (UTI) is an infection in any part of the urinary system, including the bladder, urethra, and kidneys. It leads to symptoms such as frequent urination, pain, and discomfort.",
        "Treatment typically involves antibiotics to clear the infection. Drinking plenty of water and maintaining good hygiene can help prevent UTIs."
    ],

    # Psoriasis
    [
        "Psoriasis is a chronic skin condition characterized by the rapid growth of skin cells, leading to thick, red, scaly patches. It can affect various parts of the body.",
        "Treatment options include topical creams, phototherapy, systemic medications, and lifestyle modifications to manage symptoms and prevent flare-ups."
    ],

    # Impetigo
    [
        "Impetigo is a highly contagious bacterial skin infection that primarily affects children. It results in red sores and blisters that can burst and form a honey-colored crust.",
        "Treatment involves topical or oral antibiotics to clear the infection. Good hygiene practices are essential to prevent the spread of impetigo."
    ],
    
    # Continue adding descriptions for other medical conditions here...
]


def QuestionAnswer(user_question):
    flattened_documents = ["\n".join(condition) for condition in documents]
    # Create a TF-IDF vectorizer
    vectorizer = TfidfVectorizer()

    # Vectorize the documents
    tfidf_matrix = vectorizer.fit_transform(flattened_documents)

    # Vectorize the user question
    question_vector = vectorizer.transform([user_question])

    # Compute cosine similarities between the user question and the documents
    similarities = cosine_similarity(question_vector, tfidf_matrix)

    # Find the most similar document
    most_similar_idx = np.argmax(similarities)
    answer = documents[most_similar_idx]

    return answer

# Call the function with a user question
user_question = "What is the treatment for Acne ?"
answer = QuestionAnswer(user_question)
print("Answer:", answer)





