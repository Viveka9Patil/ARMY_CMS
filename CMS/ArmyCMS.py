import streamlit as st
import pandas as pd
from Add_logo import add_logo
import plotly.express as px
import folium
from streamlit_folium import folium_static

from folium.plugins import Draw

from streamlit_folium import st_folium



import numpy as np

import pydeck as pdk


st.set_page_config(page_title='CMS Platform',  layout='wide', page_icon='assets/imgs/lvlAlpha_logo.png', 
                   initial_sidebar_state='expanded',
                   menu_items = {
                        'Report a Bug': "mailto:contact@lvlalpha.com",
                        'About' : "The App is powered by lvlAlpha Pvt. Ltd."
                   })

add_logo(logo_url = 'assets/imgs/Armylogo.png')



# Container for the Header
with st.container():
    t1, t2 = st.columns([0.9, 0.1])
    
    t1.title("Casualty Management Platform")
    t2.image('assets/imgs/lvlAlpha_logo.png', width = 150)

with st.container():
    c1, c2, c3, c4, c5= st.columns([0.20, 0.20, 0.20, 0.20, 0.20])

    c1.metric(label = 'All Devices', value = '240', 
              help = 'Number of All Devices currently deployed and Working')
    c2.metric(label = 'Active Devices', value = '200', delta = '12', 
              help = 'Number of Active Devices currently deployed and Working')
    c3.metric(label = 'Not Active Devices', value = '40', delta = '3', 
              help = 'Number of Not Active Devices currently deployed and Working')
    c4.metric(label = 'Injuries' , value = '0',
              help = 'Indicates the amount of people injured currently')
    c5.metric(label = 'Altitude' , value = '219m',
              help = 'Indicates the current altitude')
    

    st.title("Health Condition")

with st.container():
    # st.header("health condition")
    selectCanvas = st.radio ("Body Layer",
                            options = ('ALL', 'STABLE', 'UNSTABLE', 'CRITICAL'),
                            horizontal = True,
                            label_visibility = 'hidden')
   
df = pd.DataFrame(
    np.random.randn(75, 2) / [200, 200] + [28.3839, 77.3332],
    columns=['lat', 'lon'])



# Generate Folium map using Streamlit
st.write("Folium Map:")
m = folium.Map(location=[28.3839, 77.3332], zoom_start=13)
folium.Marker(
    [28.3839, 77.3332], popup="Base", tooltip="Indian Army"
).add_to(m)

Draw(export=True).add_to(m)

col1, col2 = st.columns([0.8, 0.2])
with col1:



# Add scatter plot to the Folium map based on body layer
 for i in range(25):
    hover_name=i
    
    color = 'green' if selectCanvas == 'STABLE' or selectCanvas == 'ALL' else "transparent"
    folium.CircleMarker(
        location=[df['lat'][i], df['lon'][i]],
        radius=5,
        color=color,
        fill=True,
        fill_color=color
        
    
    ).add_to(m)
 
    
    
   
 for i in range(26, 50):
    color = 'yellow' if selectCanvas == 'UNSTABLE' or selectCanvas == 'ALL' else "transparent"
    folium.CircleMarker(
        location=[df['lat'][i], df['lon'][i]],
        radius=5,
        color=color,
        fill=True,
        fill_color=color
    ).add_to(m)

 for i in range(50, 75):
    color = 'red' if selectCanvas == 'CRITICAL' or selectCanvas == 'ALL' else 'transparent'
    folium.CircleMarker(
        location=[df['lat'][i], df['lon'][i]],
        radius=5,
        color=color,
        fill=True,
        fill_color=color
    ).add_to(m)

# Render Folium map in Streamlit
 folium_static(m)


with col2:
    st.info("""
        ### Legend
        🟢Green: Normal Vitals

        🟡Yellow: Slight Irregularity in Vitals
        
        🔴Red: High Irregularity in Vitals
        """)
















