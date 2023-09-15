# Importing libraries
import streamlit as st

# Setting up the title's page
st.set_page_config(page_title='Weather Wizard - Raw Data', layout='centered')

# Transfering dataframe to this page
data = st.session_state['data']

# Bringing in the content of the page
st.subheader("Raw Data :clipboard:")
st.write(data)
