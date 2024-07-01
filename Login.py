import mysql.connector
import streamlit as st

# Connection
mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "cosmicharmony07",
    database = "dtbpupads"
)   
mycursor = mydb.cursor()
print("Connection Successful")

# Login Page
if 'page' not in st.session_state:
    st.session_state.page = 'login_page'
if 'username' not in st.session_state:
    st.session_state.username = ''

saveMember = "SELECT strSchoolID, strFirstName FROM tblscholars WHERE strMembID = %s"
saveMemberAdviser = "SELECT strAdvID FROM tbladvisers WHERE strMembID = %s"
saveAdviserName = "SELECT strFirstName FROM tblscholars WHERE strMembID = %s"


def login_page():
    background_image = """
    <style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(rgba(0, 0, 0, 0.9), rgba(0, 0, 0, 0.6)), 
            url("https://i.pinimg.com/originals/9a/d4/4c/9ad44c066b7ff6ba95afcb2b8e8e9c5f.jpg") no-repeat left;
        background-size: cover;
        color: white;
    }
    </style>
    """

    st.markdown(background_image, unsafe_allow_html=True)

    col1, col2, col3= st.columns([2.5, 1.5, 2.5])
    with col3:
        st.markdown('#')
        st.caption(" ")
        st.markdown('<div style="display: flex; justify-content: center;"><h2>PUP Association of DOST Scholars</div>', unsafe_allow_html=True) 
        st.markdown('<div style="display: flex;"><h9> The <span style="color:#5AFFF5">Polytechnic University of the Philippines – Association of DOST Scholars (PUP-ADS)</span> , the university’s premiere academic organization, has been playing a vital role in the development and leadership training of the PUP DOST Scholars towards the betterment of the quality of life with its best abilities over the past few years.</p></div>', unsafe_allow_html=True)
        st.caption(" ")
        st.link_button(label="Facebook", url="https://www.facebook.com/PUPADSOfficial")

    with col1:
        st.markdown('<div style="display: flex; justify-content: center;"><h1>Greetings, <span style="color:#5AFFF5">Scholars</span>!</></div>', unsafe_allow_html=True) 
        st.markdown('<div style="display: flex; justify-content: center;"><h7>Welcome to the <span style="color:#5AFFF5">Organizational Database</span></></div>', unsafe_allow_html=True)
        st.subheader(" ")

        select = st.selectbox("Please choose your role:", ["Student", "Adviser"], index=None)
        
        if select == "Student":
            st.caption(" ")
            st.markdown('<h7>Please enter your student credentials', unsafe_allow_html=True) 
            member = st.text_input(label="Member ID", value="", placeholder="Enter Member ID")
            password = st.text_input(label="Password", value="", placeholder="Enter password", type="password")
            st.button("Sign In", on_click=student_login_click, args=(member, password))
        if select == "Adviser":
            st.caption(" ")
            st.markdown('<h7>Please enter your adviser credentials', unsafe_allow_html=True) 
            member = st.text_input(label="Member ID", value="", placeholder="Enter Member ID")
            password = st.text_input(label="Password", value="", placeholder="Enter password", type="password")
            st.button("Sign In", on_click=adviser_login_click, args=(member, password))

def student_login_click(member, password):    
    mycursor.execute(saveMember, (member,))
    membercheck = mycursor.fetchall()

    if not membercheck:
        st.markdown("<p style='color:#5AFFF5;'>Invalid member ID! Please try again.</p>", unsafe_allow_html=True)
    else:
        strSchoolID, strFirstName = membercheck[0]
        if strSchoolID != password:
            st.markdown("<p style='color:#5AFFF5;'>Invalid password! Please try again.</p>", unsafe_allow_html=True)
        else:
            login_succes(strFirstName)

def adviser_login_click(member, password):    
    mycursor.execute(saveMemberAdviser, (member,))
    advisercheck = mycursor.fetchall()

    if not advisercheck:
        st.markdown("<p style='color:#5AFFF5;'>Invalid member ID! Please try again.</p>", unsafe_allow_html=True)
    else:
        mycursor.execute(saveAdviserName, (member,))
        namecheck = mycursor.fetchall()
        strAdvID = advisercheck[0][0] 
        if strAdvID != password:
            st.markdown("<p style='color:#5AFFF5;'>Invalid password! Please try again.</p>", unsafe_allow_html=True)
        else:
            login_succes(namecheck[0][0])

def login_succes(username):
    st.session_state.page = 'main_page'
    st.session_state.username = username
