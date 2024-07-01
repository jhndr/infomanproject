import mysql.connector
import streamlit as st
import pandas as pd
import datetime
from datetime import date, timedelta

mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "cosmicharmony07",
    database = "dtbpupads"
)
mycursor = mydb.cursor()
print("Connection Successful")

def selected():
    st.markdown(f'<h4> <span style="color:gray">Dashboard</span>', unsafe_allow_html=True)
    st.markdown(f'<h1> Welcome, <span style="color:#5AFFF5">{st.session_state.username}</span>!', unsafe_allow_html=True)

    today = date.today()
    today_date = today.strftime("%B %d, %Y") 
    st.markdown(f'<h5><span style="color:gray">{today_date}</span>', unsafe_allow_html=True)

    with st.container():
        col1, col2 = st.columns([4,4])
        with col1:
            st.caption(" ")
            st.caption(" ")
            st.markdown('<h3><span style="color:white">Current Activities</span>', unsafe_allow_html=True)
            st.markdown('<h5><span style="color:white">Events</span>', unsafe_allow_html=True)
            mycursor.execute("SELECT strEventID, strEventName, datEvent FROM tblorgevents WHERE strEventStatus='OG'")
            eventsOnGoing = mycursor.fetchall()
            eventsTbl3 = pd.DataFrame(eventsOnGoing, columns=['Event ID', 'Event Name', 'Date of Event'])
            st.dataframe(eventsTbl3)
        
        with col2:
            st.header("#")
            st.caption(" ")
            st.markdown('<h5><span style="color:white">Projects</span>', unsafe_allow_html=True)
            mycursor.execute("SELECT strProjID, strProjName, strProjName, datProjStart, datProjEnd FROM tblorgprojects WHERE strProjStatus='OG'")
            projectOnGoing = mycursor.fetchall()
            projectTbl3 = pd.DataFrame(projectOnGoing, columns=['Project ID', 'Project Name', 'Project Status', 'Start Date', 'End Date'])
            st.dataframe(projectTbl3)

    st.caption("")
    st.markdown('<h3><span style="color:white">Organization\'s Members</span>', unsafe_allow_html=True)
    mycursor.execute("SELECT strScholarID, strFirstName, strMidName, strLastName, strCourseID, datBirthdate FROM tblScholars")
    members = mycursor.fetchall()
    membersTbl = pd.DataFrame(members, columns=['Scholar ID', 'First Name', 'Middle Name', 'Last Name', 'Course', 'Date of Birth'])
    st.dataframe(membersTbl)
