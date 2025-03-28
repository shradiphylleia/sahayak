import streamlit as st
import time
import re
import string
from mail_button import set_mail_reminder as reminder_btn
from json_loader import load_json
from speech_2_text import speech_text
from response_model import response_query

json_data=load_json()
 
def get_response_json(user_query):
    user_query = user_query.lower().translate(str.maketrans('', '', string.punctuation))
    
    for conv in json_data:
        for msg in conv["messages"]:
            if msg["role"] == "user":
                normalized_text = msg["text"].lower().translate(str.maketrans('', '', string.punctuation))       
                pattern = re.compile(re.escape(normalized_text), re.IGNORECASE)
                if pattern.search(user_query):
                    return next((m["text"] for m in conv['messages'] if m['role'] == 'bot'),None)  
    return None


def rsp(response):
    for word in response.split():
        yield word + " "
        time.sleep(0.2)



st.write("poshan is a chatbot which enables you to ask questions for personalized diet suggestions, diseases and set reminders")
st.button(label='reminder 📨', on_click=reminder_btn)

# if no session histroy we reate a list and append to it
if "msgs" not in st.session_state:
    st.session_state.msgs=[]

# dict like role and the contents of the msg
for msg in st.session_state.msgs:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


input_format=st.radio(
    "how would you like to search your queries",
    ['text','audio'])


if input_format=='audio':
    audio_input=st.audio_input(label='speak your query',help='add audio input for your query')
    if audio_input:
        
        prompt=speech_text(audio_input)
        
        clean_prompt=re.sub(r"</?s>|<pad>", "",prompt).strip()
        st.write(f"audio detected as:{clean_prompt}")
        
        ai_response=get_response_json(prompt)
        if not ai_response:
            ai_response=response_query(prompt_ques=prompt)

        with st.chat_message('ai'):
            response=st.write_stream(rsp(ai_response))
        st.session_state.msgs.append({'role':'ai','content':response})



else:
    if prompt:=st.chat_input("ask your query.."):
        st.chat_message("user").markdown(prompt)
        st.session_state.msgs.append({"role":"user","content":prompt})
        
        ai_response=get_response_json(prompt)
        if not ai_response:
            ai_response=response_query(prompt_ques=prompt)

        with st.chat_message('ai'):
            response=st.write_stream(rsp(ai_response))
        st.session_state.msgs.append({'role':'ai','content':response})
