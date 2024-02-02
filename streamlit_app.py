import streamlit as st
import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['John', 'Jane', 'Bob', 'Alice'],
    'Age': [28, 35, 22, 45],
    'Salary': [50000, 60000, 45000, 80000]
}

df = pd.DataFrame(data)

# Streamlit app
st.title('DataFrame Display Example')

# Display the DataFrame
st.write(df)





