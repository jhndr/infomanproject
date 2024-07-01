import mysql.connector
import streamlit as st
import pandas as pd
from Login import *
from streamlit_option_menu import option_menu
import Dashboard, Executives, Members, Committees, EventsProjects, PartnersSponsors

st.set_page_config(layout="wide")

# Connect Database
mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "cosmicharmony07",
    database = "dtbpupads"
)
mycursor = mydb.cursor()
print("Connection Successful")

if 'page' not in st.session_state:
    st.session_state.page = 'login_page'
if 'username' not in st.session_state:
    st.session_state.username = ''

def main_page():
    #sidebar
    with st.sidebar:
        #Logo
        col1, col2 = st.columns([1, 4])
        with col1:
            st.image("Logo.png", width=50)
        with col2:
            st.markdown('<div style="display: flex; justify-content: center;"><h3>PUP Association of DOST Scholars</div>', unsafe_allow_html=True) 
        
        #Navigational Panel
        st.caption("")
        st.markdown(f'<h2><span style="color:white">Navigation</span>', unsafe_allow_html=True)
        selected = option_menu(None, ['Dashboard', 'Executives', 'Members', 'Committees', 'Events and Projects', 'Partners and Sponsors'], 
        icons=['house-fill', 'person-fill', 'people-fill', 'diagram-3-fill', 'clipboard-fill', 'hand-thumbs-up-fill'], menu_icon="none", default_index=5, 
        
            styles={
                "container": {"padding": "0!important", "background-color": "#262730"},
                "icon": {"color": "white", "font-size": "15px"}, 
                "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#5AFFF5"},
                "nav-link-selected": {"background-color": "#0E1117"},}
        )

        #Social Media Links
        st.markdown(f'<h2><span style="color:white">Social Medias</span>', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            st.link_button(label="Facebook", url="https://www.facebook.com/PUPADSOfficial", use_container_width=True)
        with c2:
            st.link_button(label="Instagram", url="https://www.instagram.com/pupads_official", use_container_width=True)

        # Logout button
        st.divider()
        c1, c2, c3 = st.columns(3)
        with c2:
            st.button("Sign Out", on_click=logout_success,  use_container_width=True)
            

    if selected == 'Dashboard':
        Dashboard.selected()
    if selected == 'Executives':
        Executives.selected()
    if selected == 'Members':   
        Members.selected()
    if selected == 'Committees':
        Committees.selected()
    if selected == 'Events and Projects':
        EventsProjects.selected()
    if selected == 'Partners and Sponsors':
        PartnersSponsors.selected()

def logout_success():
    st.session_state.page = 'login_page'

if st.session_state.page == 'login_page':
    login_page()
elif st.session_state.page == 'main_page':
    main_page()


