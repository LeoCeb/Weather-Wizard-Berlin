# Importing libraries
import streamlit as st
import plotly.express as px

# Setting up the title's page
st.set_page_config(
    page_title='Weather Wizard - Data Visualisation', layout='centered')

# Transfering dataframe to this page
data = st.session_state['data']

# Bringing in the content of the page
st.subheader("Data Visualisation :chart_with_upwards_trend:")
date_range = st.date_input("Select Date Range:", [
    data["Date"].min().date(), data["Date"].max().date()])

# Filter data based on the selected date range
filtered_data = data[(data["Date"].dt.date >= date_range[0])
                     & (data["Date"].dt.date <= date_range[1])]

# Allow the user to select the columns for the Y axes
available_features = [col for col in data.columns if col != 'Date']
y_column = st.selectbox("Select feature:", available_features)
hex_color = st.color_picker('Select a color for your line:')

# Convert hexadecimal color to RGB format
rgb_color = f'rgb({int(hex_color[1:3], 16)},{int(hex_color[3:5], 16)},{int(hex_color[5:7], 16)})'

fig = px.line(
    filtered_data,
    x="Date",
    y=y_column,
    labels={"Date": "Date", y_column: y_column},
    title=f"{y_column} vs. Date"
)
fig.update_traces(line=dict(color=rgb_color))
st.plotly_chart(fig)


# # Create a Streamlit map
# st.subheader("Weather Map for Berlin, Germany")
# m = folium.Map(location=[52.5200, 13.4050], zoom_start=10)  # Berlin coordinates

# # Add weather markers or overlays based on your weather map data
# for location, weather_info in weather_map_data.items():
#     lat, lon = location
#     popup = f"Weather: {weather_info['condition']}, Temp: {weather_info['temp']}°C"
#     folium.Marker([lat, lon], popup=popup).add_to(m)

# # Display the map in Streamlit
# folium_static(m)
