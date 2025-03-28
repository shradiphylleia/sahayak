import streamlit as st

st.title("growth🧙🏽‍♂️")
st.logo("flower.png",size='large')
pages={
    "General":[st.Page("about.py",title="growth")],
    "chatbot":[st.Page("chat.py",title="growth chatbot")]
}

pg=st.navigation(pages)
pg.run()
