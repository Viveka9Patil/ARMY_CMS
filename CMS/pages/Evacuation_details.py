import streamlit as st
from Add_logo import add_logo



st.set_page_config(page_title='CMS Platform',  layout='wide', page_icon='assets/imgs/lvlAlpha_logo.png', 
                   initial_sidebar_state='expanded',
                   menu_items = {
                        'Report a Bug': "mailto:contact@lvlalpha.com",
                        'About' : "The App is powered by lvlAlpha Pvt. Ltd."
                   })

add_logo(logo_url = 'assets/imgs/ArmyLogo.png')

st.title("Evacuation Details")
c1,c2,c3 = st.columns(3)
c1.checkbox("Request Ambulance")
c2.checkbox("Request Air Ambulance")
c3.checkbox("")

def number_system():
    st.header("Number of Patients to be evacuated")
    
    number = st.number_input("Enter number of patients:", value=0, step=1)
   
    #st.write("You entered:", number)

    #st.write("Press '+' to increase the number or '-' to decrease the number:")

    increase_btn = st.button("+")
    decrease_btn = st.button("-")

    if increase_btn:
           number += 1

    if decrease_btn:
            number -= 1

    #st.write("Updated number of patients:", number)

if __name__ == "__main__":
       number_system()


st.text_input("Additional Requirements")
