import streamlit as st
import pandas as pd
from Add_logo import add_logo
# from annotated_text import annotation


st.set_page_config(page_title='CMS Platform',  layout='wide', page_icon='assets/imgs/lvlAlpha_logo.png', 
                   initial_sidebar_state='expanded',
                   menu_items = {
                        'Report a Bug': "mailto:contact@lvlalpha.com",
                        'About' : "The App is powered by lvlAlpha Pvt. Ltd."
                   })

add_logo(logo_url = 'assets/imgs/ArmyLogo.png')


mockData = pd.read_csv("data/mock_data.csv")

st.title("Jawaan Details")

# Get the employee ID
emp = st.text_input(label = 'Search Jawaan', help = 'Enter Jawaan ID', placeholder = 'ABCD0000')

# Check if there is a match
empVal = mockData.query('@emp == ID')

if not empVal.empty:
     c1, c2, c3 = st.columns([0.2, 0.6, 0.2])

   
     with c1:
        st.header(empVal.iloc[0]['Name'])
        st.markdown(f"""**Jawaan ID:** {empVal.iloc[0]['ID']} """)

        def calculate_news_score(hr, spo2, temperature, hrv):
          hr_score = 0 if (hr >= 51 and hr <= 90) else (1 if (hr >= 40 and hr <= 50) or (hr >= 91 and hr <= 110) else 2)
          spo2_score = 0 if spo2 >= 96 else (1 if spo2 >= 91 and spo2 <= 95 else 2)
          temperature_score = 0 if (temperature >= 36.1 and temperature <= 38) else 1
          hrv_score = 0 if (hrv >= 12 and hrv <= 20) else (1 if hrv < 9 or hrv > 20 else 2)

          modified_news = (hr_score * 3) + (spo2_score * 2) + (temperature_score * 2) + (hrv_score * 3)
          return modified_news

        def display_news_score():
          hr = empVal.iloc[0]["HR"]
          spo2 = empVal.iloc[0]["SpO2"]
          temperature = empVal.iloc[0]["Temp"]
          hrv = empVal.iloc[0]["HRV"]

          news_score = calculate_news_score(hr, spo2, temperature, hrv)
          scaled_news_score = int((news_score / 10 )*100)

          st.subheader("Health Score")
          st.progress(scaled_news_score)
          st.write(f"{scaled_news_score:.1f}%")
          #st.write("Modified NEWS Score:", news_score)

         
        display_news_score()

     with c2:
        st.write("---")
        st.write(f"### Condition: __Stable__ ") # str(annotation("Stable", background = "#00FF00")), unsafe_allow_html = True )
        with st.expander("Medications"):
            st.write("This area contains medication")

        with st.expander("Treatments"):
            st.write("No ongoing Treatments.")

        with st.expander("Past Injuries"):
            st.write("No of Injuries.")

        with st.expander("Records of Hospitalisation"):
            st.write("Past Records of Hospitilisation")

        with st.expander("Prescription"):
            st.write("Prescribed by Medic Officials")

        if st.button("Add Injury"):
            st.nav_page("Injury_Report")

        if st.button("Share Report"):
            st.image("assets/imgs/qr.png")

     with c3:
        st.write("## Vitals")
        st.metric(label="Heart Rate", value=empVal.iloc[0]['HR'])
        st.metric(label="Heart Rate Variablity", value=empVal.iloc[0]['HRV'])
        st.metric(label="SpO2", value=empVal.iloc[0]['SpO2'])
        st.metric(label="Body Temperature", value=empVal.iloc[0]['Temp'])
        st.metric(label="Respiratory Rate", value=empVal.iloc[0]['Temp'])

    