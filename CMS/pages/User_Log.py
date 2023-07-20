import streamlit as st
import pandas as pd
from Add_logo import add_logo


st.set_page_config(page_title='CMS Platform',  layout='wide', page_icon='assets/imgs/lvlAlpha_logo.png', 
                   initial_sidebar_state='expanded',
                   menu_items = {
                        'Report a Bug': "mailto:contact@lvlalpha.com",
                        'About' : "The App is powered by lvlAlpha Pvt. Ltd."
                   })

add_logo(logo_url = 'assets/imgs/ArmyLogo.png')

st.title("User Activity Logs")

df = pd.read_csv("data/user_log.csv")

st.table(df)