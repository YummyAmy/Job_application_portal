import streamlit as st
import datetime
from PIL import Image
img = Image.open("WHO.png")
st.image(img, width=500)

st.header("Welcome to the World Health Organization Job Appication Portal")
st.write("Fill the appropriate fields")

Name = st.text_input("Enter your name")
Age = st.number_input("Age", min_value=18, max_value=100, step=1)
birth_date = st.date_input("Date of Birth", min_value=datetime.date(1921, 1, 1),
                           max_value=datetime.date(2022, 12, 31))
Sex = st.selectbox("Sex",
                   ("Male", "Female", "Undisclosed"))
State = st.selectbox("State of Origin",
                     ("Abia", "Anambra", "Bayelsa", "Kogi", "Akwa Ibom"))
Education = st.radio("Highest level of Education",
                     ("Primary", "Secondary", "Tertiary"))
Number = st.text_input("Phone Number: ", max_chars=11)
email = st.text_input("Email Address: ")
How = st.selectbox("How did you hear about this job opportunity?",
                   ("WHO website", "From a friend", "From Facebook", "Other sources"))

st.subheader("Data Analysis Skills")
st.text("Rate your analysis skills on the following tools")
Excel = st.slider("Microsoft Excel", 1, 5)
st.text('Selected: {}'.format(Excel))
SPSS = st.slider("IBM SPSS Statistical Software", 1, 5)
st.text('Selected: {}'.format(SPSS))
Python = st.slider("Python", 1, 5)
st.text('Selected: {}'.format(Python))
st.text_input("Why do you want to work for WHO?")
document = st.file_uploader("Upload your CV", type=['docx'])
submit = st.button("Submit")
if submit:
    st.write("You have successfully submitted your job application")