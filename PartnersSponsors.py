import mysql.connector
import streamlit as st
import pandas as pd

mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "cosmicharmony07",
    database = "dtbpupads"
)
mycursor = mydb.cursor()
print("Connection Successful")

def selected():
    st.markdown(f'<h4> <span style="color:gray">Partners and Sponsors</span>', unsafe_allow_html=True)
    st.markdown(f'<h1> Welcome, <span style="color:#5AFFF5">{st.session_state.username}</span>!', unsafe_allow_html=True)
    
    tab1, tab2= st.tabs(["Partners", "Sponsors"])
    with tab1:
        st.subheader("Partnerships")
        mycursor.execute("SELECT * FROM tblpartnerships")
        partners = mycursor.fetchall()
        partnersTbl1 = pd.DataFrame(partners, columns=['Partner ID', 'Partner Name', 'Partner Email', 'Partner Phone Number', 'Partnership Date', 'Committee ID', 'Project ID', 'Event ID'])
        st.dataframe(partnersTbl1)

    with tab2:
        st.subheader("Sponsorships")
        mycursor.execute("SELECT * FROM tblsponsorships")
        sponsors = mycursor.fetchall()
        sponsorsTbl1 = pd.DataFrame(sponsors, columns=['Sponsor ID', 'Sponsor Name', 'Sponsor Email', 'Sponsor Phone Number', 'Sponsorship Date', 'Committee ID', 'Project ID', 'Event ID'])
        st.dataframe(sponsorsTbl1)