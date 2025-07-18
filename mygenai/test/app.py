import pandas as pd
import numpy as np
import streamlit as st

## Title of the Application
st.title("Hello Streamlit")

# display a simple Text
st.write("This is an emergency message for the battalion regarding a war emergency.")

# create simple data frame
df = pd.DataFrame({
    "first column": [1,2,3,4,5,6],
    "second column" : [11,22,33,44,55,66]
})

# display the dataframe
st.write("Here is  the dataframe:")
st.write(df)

# create a line chart
chart_data = pd.DataFrame(
    np.random.rand(20,3),
    columns=["a","b","c"]
    
)

st.write("Line chart:")

#st.line_chart("Line chart:")
st.line_chart(chart_data)