
import streamlit as st
from utils_files import *
from utils_tabs import *  
from pagina_principal import *
from inicializacao import *

def main():
  inicializacao()
  pagina_principal()
  tab1, tab2 = st.sidebar.tabs(['Conversas', 'Configurações'])
  tab_conversas(tab1)
  tab_configuracoes(tab2)

if __name__ == '__main__':
  main()