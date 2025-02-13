import streamlit as st
from utils_files import *

def tab_conversas(tab):
  tab.button('Nova conversa', 
             on_click=seleciona_conversa,
             args=('',),
             use_container_width=True)
  tab.markdown('')
  conversas = listar_conversas()
  for nome_arquivo in conversas:
    nome_mensagem = desconverte_nome_mensagem(nome_arquivo).capitalize()
    if len(nome_mensagem) == 30:
      nome_mensagem += '...'
    tab.button(nome_mensagem, 
               on_click=seleciona_conversa,
               args=(nome_arquivo,),
               disabled=nome_arquivo == st.session_state['conversa_atual'],
               use_container_width=True)
  
def seleciona_conversa(nome_arquivo):
  if nome_arquivo == '':
    st.session_state['mensagens'] = []
  else:
    mensagem = ler_mensagem_por_nome_arquivo(nome_arquivo, key='mensagens')
    st.session_state['mensagens'] = mensagem  
  st.session_state['conversa_atual'] = nome_arquivo  

def tab_configuracoes(tab):
  modelo_escolhido = tab.selectbox('Selecione o modelo',
                                   ['gpt-3.5-turbo', 
                                    'gpt-4', 
                                    'gpt-4o-mini'])
  st.session_state['modelo'] = modelo_escolhido
  
  api_key = tab.text_input('Adicione sua api key', 
                         value=st.session_state['api_key'])
  if api_key != st.session_state['api_key']:
    st.session_state['api_key'] = api_key
    salvar_api_key(api_key)
    tab.success('api_key salva com sucesso!')