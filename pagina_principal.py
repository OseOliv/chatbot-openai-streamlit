import streamlit as st
from utils_files import *
from utils_openai import *

def pagina_principal():
  mensagens = ler_mensagem(st.session_state['mensagens'])  

  st.header("💬", divider=True)
  
  for mensagem in mensagens:
    chat = st.chat_message(mensagem['role'])
    chat.markdown(mensagem['content'])
    
  prompt = st.chat_input(placeholder="Digite sua mensagem...")    
  if prompt:
    if st.session_state['api_key'] == '':
      st.error('Adicione sua chave de API nas configurações!')
    else:
      nova_mensagem = {'role': 'user', 'content': prompt}
      
      chat = st.chat_message(nova_mensagem['role'])
      chat.markdown(nova_mensagem['content'])
      
      mensagens.append(nova_mensagem)
      
      chat = st.chat_message('assistant')
      placeholder = chat.empty()
      placeholder.markdown('▌')
      resposta_completa = ''
      
      respostas = retorna_resposta_modelo(mensagens, 
                                          modelo=st.session_state['modelo'],
                                          stream=True)
      for resposta in respostas:
        delta_content = resposta.choices[0].delta.content or ''
        resposta_completa += delta_content            
        placeholder.markdown(resposta_completa + '▌')
      placeholder.markdown(resposta_completa)    
      
      nova_mensagem = {'role': 'assistant', 'content': resposta_completa} 
      mensagens.append(nova_mensagem) 
      
      st.session_state['mensagens'] = mensagens
      salva_mensagens(mensagens)
