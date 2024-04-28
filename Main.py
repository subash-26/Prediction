import streamlit as st
import pandas as pd
import pickle
from PIL import Image
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

# Ignore PyplotGlobalUseWarning
warnings.filterwarnings("ignore")
warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")
st.set_option('deprecation.showPyplotGlobalUse', False)

st.set_page_config(page_title="Vaccine Prediction",
                   page_icon= '	:money_with_wings:',
                   layout="wide",
                   initial_sidebar_state="expanded",
                   menu_items={'About': """Guvi Capstone Project"""})
st.markdown("<h1 style='text-align: center; color: #FFFFFF;'>Vaccine Prediction Using <i> Linear Regression Model </i></h1>",
            unsafe_allow_html=True)

st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

df_en=pd.read_csv(r'Vaccine_EDA.csv')

# Reading the Pickle file:
with open(r"C:\Users\subash\OneDrive\Guvi\Project\Prediction\LRG_model.pkl", 'rb') as f:
    LGR = pickle.load(f)

page_be_image = f"""
<style>
[data-testid="stAppViewContainer"]{{
background-color: #87CEFA;
background-size: cover
}}

[data-testid="stHeader"] {{
background-color: #87CEFA;
}}

[data-testid="stSidebarContent"] {{
background-color: #87CEFA;
}}
</style>
"""
st.markdown(page_be_image,unsafe_allow_html=True)

# Login and Logout Page:
#if 'login_status' not in st.session_state:
#   st.session_state.login_status = False
    
#username = st.text_input("User Name")
#password = st.text_input("Password",type = 'password')
#if st.button("Login"):
#    if username == "Subash" and password == "Subash@123":
#        st.session_state.login_status = True
#        st.success("Login Successful!")
    
#    else:
#        st.session_state.login_status = False
#        st.error("Invalid Credentials. Please try again.")

#if st.session_state.login_status:      
#    logout = st.button("Logout")
#    if logout:
#        if 'login_status' in st.session_state:
#            st.session_state.login_status = False
#            st.experimental_rerun()"""




selected = option_menu(None,
                       options = ["About","Dashboard","Predictions"],
                       icons = ["house_with_garden","bar-chart","at"],
                       default_index=0,
                       orientation="horizontal",
                       styles={"container": {"width": "100%"},
                               "icon": {"color": "violet", "font-size": "40px"},
                               "nav-link": {"font-size": "40px","color":"#007bff", "text-align": "center", "margin": "-2px"},
                               "nav-link-selected": {"background-color": "#6F36AD"}})


if selected == "About":
    st.title("H1N1 Vaccine")
    st.markdown('''Influenza virus vaccine, H1N1 is used to prevent infection caused by the influenza A (H1N1) 2009 virus.\n
                The vaccine works by causing your body to produce its own protection (antibodies) against the disease.\n
    It is also known as a "flu shot".\n''')
    st.markdown('''Influenza is a virus infection of the throat, bronchial tubes, and lungs.\n
                 Influenza infection causes fever, chills, cough, headache, muscle aches, and pains in your back, arms, and legs.\n
    In addition, adults and children weakened by other diseases or medical conditions, and persons 50 years of age and over,\n
    even if they are healthy, may get a much more serious illness that may have to be treated in a hospital.\n
    Each year thousands of people die as a result of an influenza infection.\n''')
    st.text("This vaccine is to be administered only by or under the supervision of your doctor or other health care professional.\n")
    st.divider()
    st.title("ML Model")
    st.text("Logestic Regression Model has been used")
    st.markdown('''
                precision    recall  f1-score   support\n
                   0       0.91      0.80      0.85      4212\n
                1       0.48      0.70      0.57      1130\n
                accuracy                    0.77      5342\n
            macro avg       0.69      0.75      0.71      5342\n
            weighted avg    0.82      0.77      0.79      5342''')
    st.success("""
        1) h1n1_worry - Worry about the h1n1 flu(0,1,2,3) 0=Not worried at all, 1=Not very worried, 2=Somewhat worried, 3=Very worried.\n
        2) chronic_medic_condition - Has any chronic medical condition - (0,1).\n
        3) is_h1n1_risky	- What respondents think about the risk of getting ill with h1n1 in the absence of the vaccine- (1,2,3,4,5)- (1=Thinks it is not very low risk, 2=Thinks it is somewhat low risk, 3=don’t know if it is risky or not, 4=Thinks it is a somewhat high risk, 5=Thinks it is very highly risky).\n
        4) sick_from_h1n1_vacc - Does respondent worry about getting sick by taking the h1n1 vaccine - (1,2,3,4,5)- (1=Respondent not worried at all, 2=Respondent is not very worried, 3=Doesn't know, 4=Respondent is somewhat worried, 5Respondent is very worried).\n
        5) is_h1n1_vacc_effective - Does respondent think that the h1n1 vaccine is effective - (1,2,3,4,5)- (1=Thinks not effective at all, 2=Thinks it is not very effective, 3=Doesn't know if it is effective or not, 4=Thinks it is somewhat effective, 5=Thinks it is highly effective).\n
        6) dr_recc_h1n1_vacc	- Doctor has recommended h1n1 vaccine - (0,1).\n
        7) sex	- Respondent's sex - (Female, Male) - 1 - Female,2 - Male.\n
    """)

    st.title("The Prediction Deployed in Render")
    st.text("https://prediction-1-7wk5.onrender.com")

if selected == "Dashboard":
    correlation_matrix = df_en.corr(method="spearman")

    put=plt.figure(figsize=(20, 15))
    sns.heatmap(correlation_matrix, annot=True,cmap='coolwarm',fmt=".1f")
    st.title("Spearman's Rank Correlation Heatmap")
    st.pyplot(put)

    print("0--> Didn't received the H1N1 Vaccine, 1--> Took the H1N1 vaccine")
    df_en["h1n1_vaccine"].value_counts(normalize=True).plot(kind = "bar")
    put=plt.figure(figsize=(8,6))
    print("0 --> People who have cronic condition doesn't take vaccine, 1 --> People who have cronic condition take vaccine ")
    put=sns.countplot(x = "chronic_medic_condition",data = df_en,hue = "h1n1_vaccine")
    st.title("chronic_medic_condition")
    st.pyplot()

    print('Based on Age people take the vaccine')
    sns.countplot(x = "age_bracket",data = df_en,hue = "h1n1_vaccine")
    st.pyplot()

    print('Based on gender')
    sns.countplot(x = "sex",data = df_en,hue = "h1n1_vaccine")
    st.pyplot()

    sns.boxplot(df_en[['h1n1_worry']],showfliers = True)
    st.pyplot()

    plt.figure(figsize=(8, 6))  
    sns.histplot(df_en['h1n1_awareness'], kde=True, color='blue', bins=30)
    st.pyplot()

if selected == "Predictions":

    st.title("Vaccine Usage Prediction")
    st.success("Note: This Application Will Be Helpful For Making A Best Prediction About the Recommendation of H1N1 Vaccination")

    PatientStatus=st.radio("Did you take the h1n1 vaccine previously Yes or No", ('Yes','No')) 
    st.success(""" h1n1_worry - Worry about the h1n1 flu(0,1,2,3) 0=Not worried at all, 1=Not very worried, 2=Somewhat worried, 3=Very worried.""")
    H1N1_Worry = st.radio("H1N1_Worry Input (0=Not worried at all, 1=Not very worried, 2=Somewhat worried, 3=Very worried)", (0, 1, 2, 3))
    st.success("""chronic_medic_condition - Has any chronic medical condition - (0,1).""")
    chronic_medic_condition = st.radio("Chronic Medic Condition Input (Yes or NO)", (0, 1))
    st.success("""is_h1n1_risky	- What respondents think about the risk of getting ill with h1n1 in the absence of the vaccine- (1,2,3,4,5)- (1=Thinks it is not very low risk, 2=Thinks it is somewhat low risk, 3=don’t know if it is risky or not, 4=Thinks it is a somewhat high risk, 5=Thinks it is very highly risky).""")
    is_H1N1_risky = st.radio("Is H1N1 Risky Input (1=Thinks it is not very low risk, 2=Thinks it is somewhat low risk, 3=don’t know if it is risky or not, 4=Thinks it is a somewhat high risk, 5=Thinks it is very highly risky)", (1, 2, 3, 4, 5))
    st.success("""sick_from_h1n1_vacc - Does respondent worry about getting sick by taking the h1n1 vaccine - (1,2,3,4,5)- (1=Respondent not worried at all, 2=Respondent is not very worried, 3=Doesn't know, 4=Respondent is somewhat worried, 5Respondent is very worried).""")
    sick_from_h1n1_vacc = st.radio("Sick from H1N1 Vacc Input (1=Respondent not worried at all, 2=Respondent is not very worried, 3=Doesn't know, 4=Respondent is somewhat worried, 5Respondent is very worried)", (1, 2, 3, 4, 5))
    st.success("""is_h1n1_vacc_effective - Does respondent think that the h1n1 vaccine is effective - (1,2,3,4,5)- (1=Thinks not effective at all, 2=Thinks it is not very effective, 3=Doesn't know if it is effective or not, 4=Thinks it is somewhat effective, 5=Thinks it is highly effective).""")
    is_h1n1_vacc_effective = st.radio("Is H1N1 Vacc Effective Input (1=Thinks not effective at all, 2=Thinks it is not very effective, 3=Doesn't know if it is effective or not, 4=Thinks it is somewhat effective, 5=Thinks it is highly effective)", (1, 2, 3, 4, 5))
    st.success("""dr_recc_h1n1_vacc	- Doctor has recommended h1n1 vaccine - (0,1).""")
    dr_recc_h1n1_vacc = st.radio("Dr Recc H1N1 Vacc Input (Yes or No)", (0, 1))
    st.success("""sex	- Respondent's sex - (Female, Male) - 1 - Female,2 - Male.""")
    sex = st.radio("Select if Male (1) or Female (2)", (1,2))
    submit_button = st.button("Submit")

    if submit_button:
        input_data = pd.DataFrame({
            'h1n1_worry': [H1N1_Worry],
            'chronic_medic_condition': [chronic_medic_condition],
            'is_h1n1_risky': [is_H1N1_risky],
            'sick_from_h1n1_vacc': [sick_from_h1n1_vacc],
            'is_h1n1_vacc_effective': [is_h1n1_vacc_effective],
            'dr_recc_h1n1_vacc': [dr_recc_h1n1_vacc],
            'sex': [sex]
        })

        # Making prediction using knn
        prediction = LGR.predict(input_data)

        st.subheader("H1N1 Vaccine Recommendation")
        if prediction[0]==1:
            st.success("The H1N1 Vaccine is recommended")
        else:
            st.warning("The H1N1 Vaccine is not recommended")
        


            # (1,1,2,1,5,1,1) - 1
            # (1,1,2,1,5,1,0) - 1
            # (1,1,2,1,4,1,1) - 1
            # (1,1,2,3,4,1,1) - 1
