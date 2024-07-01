import mysql.connector
import streamlit as st
import pandas as pd
import datetime

mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "cosmicharmony07",
    database = "dtbpupads"
)
mycursor = mydb.cursor()
print("Connection Successful")   

def selected():
    st.markdown(f'<h4><span style="color:gray">Members</span>', unsafe_allow_html=True)
    st.markdown(f'<h1>Welcome, <span style="color:#5AFFF5">{st.session_state.username}</span>!', unsafe_allow_html=True)

    tab1, tab2, tab3, tab4, tab5, tab6, tab7= st.tabs(["General", "CS", "COED", "CSSD", "CE", "CCIS", "CADBE"])
    with tab1:
        st.markdown('<h3> S.Y. 2023 - 2024', unsafe_allow_html=True)

        st.caption(" ")
        with st.container():
            col1, col2, col3= st.columns([2, 5, 2])
            with col1:
                target = st.selectbox('Select', ['Member ID', 'First Name', 'Last Name', 'Birthdate'], index=None)  
            with col2:
                choice = st.date_input(label="", value='today', min_value=datetime.date(1900, 1, 1)) if target == "Birthdate" else st.text_input(label="", value="", placeholder=f"Search for {target}")
            with col3:
                st.markdown(" ")
            
        search(choice, target)

        st.caption(" ")
        mycursor.execute("SELECT * FROM tblScholars")
        scholar = mycursor.fetchall()
        scholarTbl = pd.DataFrame(scholar, columns=['Member ID', 'Scholar ID', 'Scholar Type', 'First Name', 'Middle Name', 'Last Name', 'Birthdate', 'Email Address', 'Phone Number', 'Address', 'School ID', 'Course ID', 'Year Level', 'Start Term', 'End Term'])
        st.dataframe(scholarTbl)


        with tab2:
            st.markdown(f"<h4> College of Science", unsafe_allow_html=True)
            st.markdown("<h5>Course Details", unsafe_allow_html=True)
            mycursor.execute("SELECT * FROM tblCourses WHERE strCourseID = 'CSC101'")
            csc = mycursor.fetchall()
            cscTbl = pd.DataFrame(csc, columns=['Course ID', 'Course Name', 'Units', 'Department College'])
            st.dataframe(cscTbl)

            mycursor.execute("SELECT * FROM tblScholars WHERE strCourseID = 'CSC101'")
            st.caption(" ")
            st.markdown("<h5>Students", unsafe_allow_html=True)
            membercsc = mycursor.fetchall()
            membercscTbl = pd.DataFrame(membercsc, columns=['Member ID', 'Scholar ID', 'Scholar Type', 'First Name', 'Middle Name', 'Last Name', 'Birthdate', 'Email Address', 'Phone Number', 'Address', 'School ID', 'Course ID', 'Year Level', 'Start Term', 'End Term'])
            st.dataframe(membercscTbl)

        with tab3:
            st.markdown(f"<h4>College of Education", unsafe_allow_html=True)
            st.markdown("<h5>Course Details", unsafe_allow_html=True)
            mycursor.execute("SELECT * FROM tblCourses WHERE strCourseID = 'CED102'")
            ced = mycursor.fetchall()
            cedTbl = pd.DataFrame(ced, columns=['Course ID', 'Course Name', 'Units', 'Department College'])
            st.dataframe(cedTbl)

            mycursor.execute("SELECT * FROM tblScholars WHERE strCourseID = 'CED102'")
            st.caption(" ")
            st.markdown("<h5>Students", unsafe_allow_html=True)
            memberced = mycursor.fetchall()
            membercedTbl = pd.DataFrame(memberced, columns=['Member ID', 'Scholar ID', 'Scholar Type', 'First Name', 'Middle Name', 'Last Name', 'Birthdate', 'Email Address', 'Phone Number', 'Address', 'School ID', 'Course ID', 'Year Level', 'Start Term', 'End Term'])
            st.dataframe(membercedTbl)
        
        with tab4:
            st.markdown("<h4>College of Social Sciences and Development", unsafe_allow_html=True)
            st.markdown("<h5>Course Details", unsafe_allow_html=True)
            mycursor.execute("SELECT * FROM tblCourses WHERE strCourseID = 'CSD103'")
            csd = mycursor.fetchall()
            csdTbl = pd.DataFrame(csd, columns=['Course ID', 'Course Name', 'Units', 'Department College'])
            st.dataframe(csdTbl)

            mycursor.execute("SELECT * FROM tblScholars WHERE strCourseID = 'CSD103'")
            st.caption(" ")
            st.markdown("<h5>Students", unsafe_allow_html=True)
            membercsd = mycursor.fetchall()
            membercsdTbl = pd.DataFrame(membercsd, columns=['Member ID', 'Scholar ID', 'Scholar Type', 'First Name', 'Middle Name', 'Last Name', 'Birthdate', 'Email Address', 'Phone Number', 'Address', 'School ID', 'Course ID', 'Year Level', 'Start Term', 'End Term'])
            st.dataframe(membercsdTbl)

        with tab5:
            st.markdown(f"<h4>College of Egineering", unsafe_allow_html=True)
            st.markdown("<h5>Course Details", unsafe_allow_html=True)
            mycursor.execute("SELECT * FROM tblCourses WHERE strCourseID = 'CEN104'")
            cen = mycursor.fetchall()
            cenTbl = pd.DataFrame(cen, columns=['Course ID', 'Course Name', 'Units', 'Department College'])
            st.dataframe(cenTbl)

            mycursor.execute("SELECT * FROM tblScholars WHERE strCourseID = 'CEN104'")
            st.caption(" ")
            st.markdown("<h5>Students", unsafe_allow_html=True)
            membercen = mycursor.fetchall()
            membercenTbl = pd.DataFrame(membercen, columns=['Member ID', 'Scholar ID', 'Scholar Type', 'First Name', 'Middle Name', 'Last Name', 'Birthdate', 'Email Address', 'Phone Number', 'Address', 'School ID', 'Course ID', 'Year Level', 'Start Term', 'End Term'])
            st.dataframe(membercenTbl)
        
        with tab6:
            st.markdown(f"<h4>College of Computer and Information Sciences</h3>", unsafe_allow_html=True)
            st.markdown("<h5>Course Details", unsafe_allow_html=True)
            mycursor.execute("SELECT * FROM tblCourses WHERE strCourseID = 'CCIS105'")
            ccis = mycursor.fetchall()
            ccisTbl = pd.DataFrame(ccis, columns=['Course ID', 'Course Name', 'Units', 'Department College'])
            st.dataframe(ccisTbl)

            mycursor.execute("SELECT * FROM tblScholars WHERE strCourseID = 'CCIS105'")
            st.caption(" ")
            st.markdown("<h5>Students", unsafe_allow_html=True)
            memberccis = mycursor.fetchall()
            memberccisTbl = pd.DataFrame(memberccis, columns=['Member ID', 'Scholar ID', 'Scholar Type', 'First Name', 'Middle Name', 'Last Name', 'Birthdate', 'Email Address', 'Phone Number', 'Address', 'School ID', 'Course ID', 'Year Level', 'Start Term', 'End Term'])
            st.dataframe(memberccisTbl)
        
        with tab7:
            st.markdown(f"<h4>College of Architecture, Design, and Built Environment</h3>", unsafe_allow_html=True)
            st.markdown("<h5>Course Details", unsafe_allow_html=True)
            mycursor.execute("SELECT * FROM tblCourses WHERE strCourseID = 'CAB106'")
            cab = mycursor.fetchall()
            cabTbl = pd.DataFrame(cab, columns=['Course ID', 'Course Name', 'Units', 'Department College'])
            st.dataframe(cabTbl)

            mycursor.execute("SELECT * FROM tblScholars WHERE strCourseID = 'CAB106'")
            st.caption(" ")
            st.markdown("<h5>Students", unsafe_allow_html=True)
            membercab = mycursor.fetchall()
            membercabTbl = pd.DataFrame(membercab, columns=['Member ID', 'Scholar ID', 'Scholar Type', 'First Name', 'Middle Name', 'Last Name', 'Birthdate', 'Email Address', 'Phone Number', 'Address', 'School ID', 'Course ID', 'Year Level', 'Start Term', 'End Term'])
            st.dataframe(membercabTbl)

def search(choice, target):
    if target == 'Member ID':
        membID = "SELECT * FROM tblscholars WHERE strMembID = %s"
        mycursor.execute(membID, (choice,))
        membercheck = mycursor.fetchall()

        if not membercheck:
            st.error('Member ID cannot be found')
        else:
            st.markdown(f'<h5> <span style="color:gray">Results</span>', unsafe_allow_html=True)
            memberFound = pd.DataFrame(membercheck, columns=['Member ID', 'Scholar ID', 'Scholar Type', 'First Name', 'Middle Name', 'Last Name', 'Birthdate', 'Email Address', 'Phone Number', 'Address', 'School ID', 'Course ID', 'Year Level', 'Start Term', 'End Term'])
            st.dataframe(memberFound)
        
    if target == 'First Name':
        firstName = "SELECT * FROM tblscholars WHERE strFirstName = %s"
        mycursor.execute(firstName, (choice,))
        membercheck = mycursor.fetchall()

        if not membercheck:
            st.error('Member ID cannot be found')
        else:
            st.markdown(f'<h5> <span style="color:gray">Results</span>', unsafe_allow_html=True)
            memberFound = pd.DataFrame(membercheck, columns=['Member ID', 'Scholar ID', 'Scholar Type', 'First Name', 'Middle Name', 'Last Name', 'Birthdate', 'Email Address', 'Phone Number', 'Address', 'School ID', 'Course ID', 'Year Level', 'Start Term', 'End Term'])
            st.dataframe(memberFound)

    if target == 'Last Name':
        lastName = "SELECT * FROM tblscholars WHERE strLastName = %s"
        mycursor.execute(lastName, (choice,))
        membercheck = mycursor.fetchall()

        if not membercheck:
            st.error('Member ID cannot be found')
        else:
            st.markdown(f'<h5> <span style="color:gray">Results</span>', unsafe_allow_html=True)
            memberFound = pd.DataFrame(membercheck, columns=['Member ID', 'Scholar ID', 'Scholar Type', 'First Name', 'Middle Name', 'Last Name', 'Birthdate', 'Email Address', 'Phone Number', 'Address', 'School ID', 'Course ID', 'Year Level', 'Start Term', 'End Term'])
            st.dataframe(memberFound)
        
    if target == 'Birthdate':
        bday = "SELECT * FROM tblscholars WHERE datBirthdate = %s"
        mycursor.execute(bday, (choice,))
        membercheck = mycursor.fetchall()

        if not membercheck:
            st.error('Member ID cannot be found')
        else:
            st.markdown(f'<h5> <span style="color:gray">Results</span>', unsafe_allow_html=True)
            memberFound = pd.DataFrame(membercheck, columns=['Member ID', 'Scholar ID', 'Scholar Type', 'First Name', 'Middle Name', 'Last Name', 'Birthdate', 'Email Address', 'Phone Number', 'Address', 'School ID', 'Course ID', 'Year Level', 'Start Term', 'End Term'])
            st.dataframe(memberFound)