import streamlit as st
import time


time.sleep(1)
st.balloons()
st.header('About',divider=True)
st.image('upskill.png')
st.write("growth is a chatbot which enables you to ask questions for personalized careeer suggestions, career progressions and set reminders for jobs")

st.subheader('Roadmaps and personalized',divider=True)
st.image('goal.png')
st.write("Ask growth chatbot to provide you with detailed career goal roadmaps, step-by-step guidance, and personalized strategies to help you achieve your professional aspirations.")

st.subheader('Prepare and progress',divider=True)
st.image('interview.png')
st.write('Prepare for career progression and get a head start on your career')


st.divider()
st.markdown("""Credits
- graphics for the app logo were sourced from [Canva](https://www.canva.com)
- speech to text [huggingface](https://huggingface.co)   
- built with [streamlit](https://streamlit.io/)
- gemini: for response model
""")

st.divider()
st.write("this project was created as part of a competition submission to AI/ML multi-track competition hosted by PeerHub x CIG IIT Roorkee")
st.write("by shraddha/shradiphylliea")
st.link_button("get in touch", "https://github.com/shradiphylleia")
