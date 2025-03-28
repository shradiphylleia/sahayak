import streamlit as st
from mail import mail_reminder as mail

@st.dialog("set a reminder📅")
def set_mail_reminder():
    st.write("Enter details to receive a reminder mail.")
    email=st.text_input("your email address")
    reminder_subject=st.text_input("enter the subject")
    reminder_content=st.text_input("enter the contents to the reminder mail")
    reminder_date=st.text_input("enter date for the event")
    if st.button("enter"):
        mail(user_email=email,subject=reminder_subject,content=reminder_content,date=reminder_date)
