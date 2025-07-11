import streamlit as st
import pandas as pd
import os

#---------- Page Configuration ----------
st.set_page_config(page_title="Navi Mumbai school portal", layout="centered")

# ---------- Custom Styling ----------
st.markdown("""
    <style>
    /* Set main background */
    .main {
        background-color: #f0f4f8;
        padding: 20px;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Headings */
    h1, h2, h3 {
        color: #2c3e50;
        font-weight: bold;
        text-align: center;
    }

    /* Buttons */
    .stButton > button {
        background-color: #3498db;
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px 30px;
        font-size: 16px;
        font-weight: 600;
        transition: 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #2980b9;
        transform: scale(1.05);
    }

    /* Input Fields */
    .stTextInput > div > input,
    .stTextArea > div > textarea {
        border: 2px solid #3498db;
        border-radius: 8px;
        padding: 10px;
        font-size: 15px;
    }

    /* Radio, Selectbox, Slider */
    .stRadio > div,
    .stSelectbox > div,
    .stSlider > div {
        background-color: #ffffff;
        border: 1px solid #dfe6e9;
        border-radius: 8px;
        padding: 10px;
    }

    /* Expander Styling */
    .streamlit-expanderHeader {
        font-weight: bold;
        font-size: 18px;
        color: #34495e;
    }

    /* Customize DataFrame Scroll */
    .stDataFrame {
        background-color: #ffffff;
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Sidebar Navigation ----------
st.sidebar.title("🔍 Navigation")
page = st.sidebar.radio("Go To", ["Home", "Upload CSV", "About"])

# ---------- Page Functions ----------
def home_page():
    st.title("🏠 Welcome to the Customer Info Portal")
    st.markdown("""
        Welcome to the **Customer Information Management System**.  
        Use this portal to:
        - 📂 Upload and manage customer data
        - 📊 View insights from your files
        - 👥 Store basic customer profiles
        Use the sidebar to navigate between pages.
    """)
    st.image("https://cdn-icons-png.flaticon.com/512/711/711769.png", width=140)

    st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>🏙️ Navi Mumbai School Portal</h1>", unsafe_allow_html=True)
    st.markdown("### Please enter your details below 👇")

    save_path = "submitted_students.csv"

    with st.form("student_form"):
        st.subheader("👨‍🎓👩‍🎓 Student Information")
        Name = st.text_input("👨‍🎓👩‍🎓 Enter Student Name")
        DOB = st.date_input("🎂 Date of Birth")
        Gender = st.radio("⚧️ Gender", ['Male', 'Female', 'Other'])
        standard = st.slider("🧑‍🏫👨‍🏫📚 Select Student Standard (Class)", 1, 12, 5)
        Medium = st.selectbox("🗣️ Select Medium", ['Marathi', "English", "Semi-English"])
        Address = st.text_input("🏠 Address")
        Contact_number = st.text_input("📞 Contact Number")
        Email = st.text_input("📧 Email ID")
        Blood_Group = st.selectbox("🩸 Blood Group", ['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-'])
        Hobbies = st.multiselect("🎯 Hobbies", ['Drawing', 'Singing', 'Dancing', 'Sports', 'Reading', 'Coding'])
        Submit = st.form_submit_button("✅ Submit")

        if Submit:
            if not Name or not Email:
                st.error("Please enter at least Name and Email.")
            else:
                new_data = {
                    "Name": Name,
                    "DOB": str(DOB),
                    "Gender": Gender,
                    "Standard": standard,
                    "Medium": Medium,
                    "Address": Address,
                    "Contact_number": Contact_number,
                    "Email": Email,
                    "Blood_Group": Blood_Group,
                    "Hobbies": ', '.join(Hobbies)
                }

                if os.path.exists(save_path):
                    df_existing = pd.read_csv(save_path)
                    df_new = pd.DataFrame([new_data])
                    df_combined = pd.concat([df_existing, df_new], ignore_index=True)
                    df_combined.to_csv(save_path, index=False)
                else:
                    pd.DataFrame([new_data]).to_csv(save_path, index=False)

                st.success("🎉 Student Registered Successfully and data saved!")

    st.markdown("----------")

    # Show saved submissions if available
    if os.path.exists(save_path):
        st.subheader("📂 Submitted Student Records")
        df_saved = pd.read_csv(save_path)
        st.dataframe(df_saved, use_container_width=True)
        st.download_button(
            label="⬇️ Download Submitted Data",
            data=df_saved.to_csv(index=False),
            file_name="submitted_students.csv",
            mime="text/csv"
        )
    else:
        st.info("No student records found yet. Submit the form above to add data.")

def uploaded_csv_page():
    st.title("📂 Upload Your CSV File")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.success("✅ File uploaded successfully!")
        st.write("### Preview of uploaded data:")
        st.dataframe(df)

def about_page():
    st.title("ℹ️ About Navi Mumbai School")
    st.markdown("""
        ### 🏫 Welcome to Navi Mumbai School  
        Navi Mumbai School provides high-quality education from **Standard 1 to Standard 12**, blending traditional values with modern digital learning experiences.

        #### 🎯 Our Vision:
        To foster intellectual curiosity, creativity, and lifelong learning through a student-centered, technology-integrated education system.

        #### 📘 What We Offer:
        - 👩‍🏫 Live & Recorded Online Lectures  
        - 📱 Mobile App Access for Students & Parents  
        - 🖥️ Smart Classrooms with Interactive Whiteboards  
        - 🎥 Virtual Classrooms & Video Conferencing  
        - 🧪 Advanced Science and Computer Labs  
        - 🧑‍🔬 AI-based Performance Tracking  
        - 🧭 Digital Timetables & Homework Assignments  
        - 🎓 Exam Portals & Online Evaluation  
        - 📊 Student Analytics and Reports  
        - 🧑‍💻 Coding & Robotics Labs  
        - 📝 E-Notes, PDFs & Learning Resources  
        - 🧾 Automated Attendance System  
        - 💬 Chat & Query Support for Students

        #### 🛠️ Technologies Used in this Portal:
        - Python 🐍 (Backend)
        - Streamlit 📊 (Frontend Web Interface)
        - Pandas 🐼 (Data Handling)
        - Firebase 🔥 (Authentication & Real-Time Database)
        - Google Meet / Zoom 🎥 (Live Lectures)
        - AWS / Azure ☁️ (Cloud Infrastructure)
        - GitHub 🧠 (Version Control)
        - MongoDB / PostgreSQL 🗃️ (Database Storage)

        #### 📍 Location:
        Navi Mumbai, Maharashtra - 400709

        #### 📧 Contact:
        `monish.sakpal@email.com`
    """)

# ---------- Page Routing ----------
if page == "Home":
    home_page()
elif page == "Upload CSV":
    uploaded_csv_page()
elif page == "About":
    about_page()

# # Now based on the selected page, show content conditionally
# if Page == "Home":
#     st.title("Welcome to Navi Mumbai School")
#     st.write("This is the home page.Please enter required details under.")
    
# elif page == "Upload CSV":
#     st.title("Upload Your CSV File")
#     uploaded_file = st.file_uploader("Choose a CSV file",type= "csv")
#     if uploaded_file is not None:
#         df = pdd.read_csv(uploaded_file)
#         st.dataframe(df)
        
        
# elif page == "About":
#     st.title("About Us")
#     st.write("""
#     This app is built to collect Navi Mumbai School  information and upload CSV files.
#     Created using Streamlit.
#     """)








    

     
     
# file uploading
# st.markdown("### 📤 Upload Your CSV File")
# uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# if uploaded_file is not None:
#     user_df = pdd.read_csv(uploaded_file)
#     st.success("✅ File Uploaded Successfully!")
#     st.dataframe(user_df,use_container_width=True)
    
        

