import streamlit as st
import pandas as pd
from Add_logo import add_logo
import plotly.express as px
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





col1, col2 = st.columns([0.5, 0.5])

with col1:
    st.header("Past record")

    tab1, tab2, tab3, tab4, tab5 = st.tabs(["VOC", "Temperature", "Humidity","Air Quality Index","Air Pressure",])

    with tab1:
        st.subheader("Volatile Organic Compound Variation Log")

        vocDF = pd.read_csv("data/voc_data.csv")
        fig = px.line(vocDF, x = 'Days', y = 'Concentration', color = 'Compound', markers = True)
        fig.update_layout(title_text = 'VOC concentration in µg/m3')
        st.plotly_chart(fig, use_container_width = True)

    
    with tab2:
        st.subheader("Temperature Variation Log")

        tempDF = pd.read_csv("data/temperature.csv")
        fig = px.line(tempDF, x = 'Days', y = 'Avg temp (in degree celsius)', markers = True)
        fig.update_layout(title_text = 'Temperature in degreee Celsius')
        fig.update_yaxes(range = [20, 45])
        st.plotly_chart(fig, use_container_width = True)

    with tab3:
        st.subheader("Humidity Variation Log")

        hdf = pd.read_csv("data\humidity.csv")
        fig = px.line(hdf, x = 'Days', y = 'Humidity (in %)', markers = True)
        fig.update_layout(title_text = 'Humidity in Percentage')
        fig.update_yaxes(range = [0, 100])
        st.plotly_chart(fig, use_container_width = True)

    with tab4:
        st.subheader("Air Quality Index Log")

        hdf = pd.read_csv("aqi_data.csv")
        fig = px.line(hdf, x = 'Days', y = 'AirQualityIndex', markers = True)
        fig.update_layout(title_text = 'Air Quality Index')
        fig.update_yaxes(range = [40, 50])
        st.plotly_chart(fig, use_container_width = True)


    with tab5:
        st.subheader("Atmospheric Pressure Log")

        hdf = pd.read_csv("ap_data.csv")
        fig = px.line(hdf, x = 'Days', y = 'Atmospheric Pressure (in hPa)', markers = True)
        fig.update_layout(title_text = 'Air Pressure in Pascals ')
        fig.update_yaxes(range = [900, 1000])
        st.plotly_chart(fig, use_container_width = True)  

         
          


with col2:
    
    st.header("Jawaan Health overview")
    df = pd.read_csv('data\mock_data(1).csv')

    st.dataframe(df, use_container_width = True)