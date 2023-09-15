# importing libraries

import gspread
import pandas as pd
import streamlit as st


# defining function to get the data from the google spreadsheet
def get_data(sheet_name):
    # Authenticate and open the Google Sheet
    gc = gspread.service_account(
        filename="../service_account.json")
    wks = gc.open(sheet_name).sheet1

    # Get all the values from the Google Sheet
    data = wks.get_all_values()

    # Specify column names (assuming the first row of the Google Sheet contains column headers)
    column_names = data[0]

    # Create a Pandas DataFrame from the data, skipping the first row (header row)
    df = pd.DataFrame(data[1:], columns=column_names)

    # Convert columns to appropriate data types
    df['Date'] = pd.to_datetime(df['Date'])
    df['Temperature'] = pd.to_numeric(
        df['Temperature'].str.replace(',', '.'), errors='coerce')
    df['Temperature feels like'] = pd.to_numeric(
        df['Temperature feels like'].str.replace(',', '.'), errors='coerce')
    df['Temperature Min'] = pd.to_numeric(
        df['Temperature Min'].str.replace(',', '.'), errors='coerce')
    df['Temperature Max'] = pd.to_numeric(
        df['Temperature Max'].str.replace(',', '.'), errors='coerce')
    df['Humidity'] = pd.to_numeric(
        df['Humidity'], errors='coerce').astype('Int8')
    df['Wind Speed'] = pd.to_numeric(
        df['Wind Speed'].str.replace(',', '.'), errors='coerce')

    return df


data = get_data('weather_api_project')


# Streamlit app
st.set_page_config(page_title='Weather Wizard - Home', layout='centered')

# Adding a title and description
st.title('Weather Wizard - Berlin Data Delve')
st.title(':sun_small_cloud: :barely_sunny: :partly_sunny_rain: :rain_cloud: :snow_cloud:')

st.divider()

st.header(':book:  Description:')
st.write("Welcome to the Weather Wizard, your gateway to Berlin's atmospheric secrets! This dynamic web app isn't just about weather – it's your passport to forecasting, exploring, and uncovering meteorological insights in the heart of Germany.")

st.divider()

st.header(':gear:  How to Use It:')
st.write('Navigate effortlessly using the sidebar on the left to access four captivating sections:')
st.markdown(
    ":gray[1.]  **Home:** Here's where you are right now! Delve into the fascinating world of Berlin's weather data.")
st.markdown(":gray[2.]  **Raw Data:** Dive headfirst into the raw, unfiltered data. For the data purists and analysts, this section unveils every detail.")
st.markdown(":gray[3.]  **Data Statistics:** Get ready to be amazed by the numbers! Discover key statistics like count, mean, standard deviation, minimum, maximum, and more, all at your fingertips.")
st.markdown(":gray[4.]  **Data Visualization:** Transform data into vivid insights! Choose from an array of features and dates to create stunning visualizations that reveal Berlin's weather trends.")

st.divider()

st.header(':crystal_ball:  Forecast Updates:')
st.write("Wondering about the future? Our Weather Wizard automatically refreshes the forecasted data every 3 hours using the powerful OpenWeather API. Stay ahead of the weather with accurate predictions! Prepare to embark on a weather journey like no other. Berlin's climate secrets await your exploration – step into the Weather Wizard's world today!")

# Applying session_state[] to the data  transfer the dataframe (data) across the pages
st.session_state['data'] = data

# streamlit run streamlit_app.py
