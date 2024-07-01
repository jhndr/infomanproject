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
    st.markdown(f'<h4> <span style="color:gray">Events and Projects</span>', unsafe_allow_html=True)
    st.markdown(f'<h1> Welcome, <span style="color:#5AFFF5">{st.session_state.username}</span>!', unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Not Started", "On Going", "Completed"])
    with tab1:
        st.subheader("Events")
        mycursor.execute("SELECT * FROM tblorgevents")
        eventsOverview = mycursor.fetchall()
        eventsTbl1 = pd.DataFrame(eventsOverview, columns=['Event ID', 'Event Name', 'Participant ID', 'Participant Name', 'Date of Event', 'Event Address', 'Event Status', 'Event Budget', 'Committee ID'])
        st.dataframe(eventsTbl1)

        st.subheader("Projects")
        mycursor.execute("SELECT * FROM tblorgprojects")
        projectOverview = mycursor.fetchall()
        projectTbl1 = pd.DataFrame(projectOverview, columns=['Project ID', 'Project Name', 'Project Status', 'Project Budget', 'Start Date', 'End Date', 'Project Address', 'Committee ID'])
        st.dataframe(projectTbl1)

    with tab2:
        st.subheader("Events")
        mycursor.execute("SELECT * FROM tblorgevents WHERE strEventStatus='NS'")
        eventsNotStarted = mycursor.fetchall()
        eventsTbl2 = pd.DataFrame(eventsNotStarted, columns=['Event ID', 'Event Name', 'Participant ID', 'Participant Name', 'Date of Event', 'Event Address', 'Event Status', 'Event Budget', 'Committee ID'])
        st.dataframe(eventsTbl2)

        st.subheader("Projects")
        mycursor.execute("SELECT * FROM tblorgprojects WHERE strProjStatus='NS'")
        projectNotStarted = mycursor.fetchall()
        projectTbl2 = pd.DataFrame(projectNotStarted, columns=['Project ID', 'Project Name', 'Project Status', 'Project Budget', 'Start Date', 'End Date', 'Project Address', 'Committee ID'])
        st.dataframe(projectTbl2)

    with tab3:
        st.subheader("Events")
        mycursor.execute("SELECT * FROM tblorgevents WHERE strEventStatus='OG'")
        eventsOnGoing = mycursor.fetchall()
        eventsTbl3 = pd.DataFrame(eventsOnGoing, columns=['Event ID', 'Event Name', 'Participant ID', 'Participant Name', 'Date of Event', 'Event Address', 'Event Status', 'Event Budget', 'Committee ID'])
        st.dataframe(eventsTbl3)

        st.subheader("Projects")
        mycursor.execute("SELECT * FROM tblorgprojects WHERE strProjStatus='OG'")
        projectOnGoing = mycursor.fetchall()
        projectTbl3 = pd.DataFrame(projectOnGoing, columns=['Project ID', 'Project Name', 'Project Status', 'Project Budget', 'Start Date', 'End Date', 'Project Address', 'Committee ID'])
        st.dataframe(projectTbl3)
    
    with tab4:
        st.subheader("Events")
        mycursor.execute("SELECT * FROM tblorgevents WHERE strEventStatus='CT'")
        eventsCompleted = mycursor.fetchall()
        eventsTbl4 = pd.DataFrame(eventsCompleted, columns=['Event ID', 'Event Name', 'Participant ID', 'Participant Name', 'Date of Event', 'Event Address', 'Event Status', 'Event Budget', 'Committee ID'])
        st.dataframe(eventsTbl4)

        st.subheader("Projects")
        mycursor.execute("SELECT * FROM tblorgprojects WHERE strProjStatus='CT'")
        projectCompleted = mycursor.fetchall()
        projectTbl4 = pd.DataFrame(projectCompleted, columns=['Project ID', 'Project Name', 'Project Status', 'Project Budget', 'Start Date', 'End Date', 'Project Address', 'Committee ID'])
        st.dataframe(projectTbl4)