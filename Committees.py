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
    st.markdown(f'<h4> <span style="color:gray">Committees</span>', unsafe_allow_html=True)
    st.markdown(f'<h1> Welcome, <span style="color:#5AFFF5">{st.session_state.username}</span>!', unsafe_allow_html=True)

    tab1, tab2, tab3= st.tabs(["Operations", "Communications", "Finance"])
    with tab1:
        st.subheader("Operations Committee")
        mycursor.execute("SELECT * FROM tblOperations")
        operations = mycursor.fetchall()
        operationsTbl = pd.DataFrame(operations, columns=['Operations ID', 'SubCommittee', 'Committee ID'])
        st.dataframe(operationsTbl)

    with tab2:
        st.subheader("Communications Committee")
        mycursor.execute("SELECT * FROM tblCommunications")
        communications = mycursor.fetchall()
        communicationsTbl = pd.DataFrame(communications, columns=['Communications ID', 'SubCommittee', 'Committee ID'])
        st.dataframe(communicationsTbl)

    with tab3:  
        st.subheader("Finance Committee")
        mycursor.execute("SELECT * FROM tblFinance")
        finance = mycursor.fetchall()
        financeTbl = pd.DataFrame(finance, columns=['Finance ID', 'SubCommittee', 'Committee ID'])
        st.dataframe(financeTbl)