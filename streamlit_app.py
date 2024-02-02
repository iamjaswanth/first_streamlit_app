import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# Custom CSS for styling
custom_css = """
<style>
    /* Add your custom styles here */
    body {
        color: #333;
        font-family: 'Arial', sans-serif;
        margin: 0;
        padding: 0;
        background-color: #f4f4f4;
    }
    
    .main-container {
        padding: 2rem;
    }

    h1 {
        color: #005a8d;
    }

    table.dataframe {
        border-collapse: collapse;
        width: 100%;
        margin-top: 1rem;
    }

    th, td {
        border: 1px solid #ddd;
        padding: 8px;
        text-align: left;
    }

    th {
        background-color: #005a8d;
        color: white;
    }

    tr:nth-child(even) {
        background-color: #f2f2f2;
    }
</style>
"""

# Inject the custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Create a sample DataFrame
data = {
    'Name': ['John', 'Jane', 'Bob', 'Alice'],
    'Age': [28, 35, 22, 45],
    'Salary': [50000, 60000, 45000, 80000]
}

df = pd.DataFrame(data)

# Streamlit app
st.title('Interactive DataFrame Display')

# Display the DataFrame
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.write(df)
st.markdown('</div>', unsafe_allow_html=True)
