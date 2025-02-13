from openai import OpenAI
import streamlit as st

def inicializa_cliente_openai(api_key):
  return OpenAI(api_key=api_key)

def retorna_resposta_modelo(mensagens, 
                            modelo='gpt-3.5-turbo', 
                            temperature=0, 
                            stream=False):
  client = inicializa_cliente_openai(st.session_state['api_key'])
  response = client.chat.completions.create(
    model=modelo,
    messages=mensagens,
    temperature=temperature,
    stream=stream
  )
  return response 