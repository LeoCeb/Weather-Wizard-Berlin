# Importing libraries
import streamlit as st

# Setting up the title's page
st.set_page_config(
    page_title='Weather Wizard - Data Statistics', layout='centered')

# Transfering dataframe to this page
data = st.session_state['data']

# Bringing in the content of the page
st.subheader("Data Statistics :bar_chart:")
st.write(data.describe())
