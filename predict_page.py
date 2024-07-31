import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('model.pkl', 'rb') as file:
        data = pickle.load(file)
        return data
    
data = load_model()

regressor = data['model']
label_country = data['label_country']
label_age = data['label_age']
label_education = data['label_education']

def show_predict_page():
    st.title("Software Developer Salary Prediction")
    
    countries = (
        'United States of America',
        'Germany',
        'United Kingdom of Great Britain and Northern Ireland',
        'Canada',
        'India',
        'France',
        'Netherlands',
        'Australia',
        'Brazil',
        'Spain',
        'Sweden',
        'Italy',
        'Poland',
        'Switzerland',
        'Denmark',
        'Norway',
        'Israel',
        'Portugal',
        'Austria',
        'Finland',
        'Belgium',
        'Russian Federation',
        'New Zealand',
        'Ukraine',
        'Turkey',
    )
    
    education = (
        'Less than a Bachelor’s degree',
        'Bachelor’s degree',
        'Master’s degree',
        'Professional degree',
    )
    
    age = (
        '25-34 years old',
        '35-44 years old',
        '45-54 years old',
        '18-24 years old',
        '55-64 years old',
        '65 years or older'
    )
    
    country = st.selectbox('Country', countries)
    education = st.selectbox('Education Level', education)
    experience = st.slider('Years of Experience', 0, 50, 3)
    age = st.selectbox('Age', age)
    
    ok = st.button('Calculate Salary')
    if ok:
        X = np.array([[country, education, age, experience]])
        X[:, 0] = label_country.transform(X[:,0])
        X[:, 1] = label_education.transform(X[:,1])
        X[:, 2] = label_age.transform(X[:, 2])
        X = X.astype(float)
        
        salary = regressor.predict(X)
        st.subheader(f'The estimated salary is ${salary[0]:.2f}')