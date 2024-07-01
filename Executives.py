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
    st.markdown(f'<h4> <span style="color:gray">Executives</span>', unsafe_allow_html=True)
    st.markdown(f'<h1> Welcome, <span style="color:#5AFFF5">{st.session_state.username}</span>!', unsafe_allow_html=True)

    st.caption(" ")
    st.markdown('<h3> S.Y. 2023 - 2024', unsafe_allow_html=True)
    mycursor.execute("SELECT * FROM tblExecutives")
    executive = mycursor.fetchall()
    executiveTbl = pd.DataFrame(executive, columns=['Committee ID', 'Member ID', 'Committee', 'Role'])
    st.dataframe(executiveTbl)