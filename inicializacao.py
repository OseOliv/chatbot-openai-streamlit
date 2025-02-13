import streamlit as st
from utils_files import *

def inicializacao():
  session_state = {
    'mensagens': [],
    'conversa_atual': '',
    'modelo': 'gpt-3.5-turbo',
    'api_key': ler_api_key()
  }
  
  for key, value in session_state.items():
    if key not in st.session_state:
      st.session_state[key] = value