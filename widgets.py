import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name = st.text_input("Enter your name:")

age = st.slider("select your age:",0,100,15)

st.write(f"Your age is {age}.")

options = ["Terner","Fitter","welder","plumber"]
choice = st.selectbox("Choose your favorite course:",options)

st.write(f"Selected courses: {choice}")

if name:
    st.write(f"Hello {name}")
    
    
data = {
    "Name":["Monish","Vijay","Paresh","parshu"],
    "Age":[22,18,28,25],
    "City":["Belapur","Airoli","Ulhasnagar","Sanpada"]

}

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)
    

uploaded_file = st.file_uploader("choose a CSV file",type= "csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)