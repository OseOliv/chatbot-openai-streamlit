import pickle
import re
from unidecode import unidecode
from pathlib import Path


PASTA_CONFIGURACOES = Path(__file__).parent / 'configuracoes'
PASTA_CONFIGURACOES.mkdir(exist_ok=True)
PASTA_MENSAGENS = Path(__file__).parent / 'mensagens'
PASTA_MENSAGENS.mkdir(exist_ok=True)
CACHE_DESCONVERTE = {}

def converte_nome_mensagem(nome_mensagem):
  nome_arquivo = unidecode(nome_mensagem)    
  nome_arquivo = re.sub('\W+', '', nome_arquivo).lower()
  return nome_arquivo

def desconverte_nome_mensagem(nome_arquivo):
  if not nome_arquivo in CACHE_DESCONVERTE:
    nome_mensagem = ler_mensagem_por_nome_arquivo(nome_arquivo, key='nome_mensagem')
    CACHE_DESCONVERTE[nome_arquivo] = nome_mensagem
  return CACHE_DESCONVERTE[nome_arquivo]

def retorna_nome_da_mensagem(mensagens):
  nome_messagem = ''
  for mensagem in mensagens:
    if mensagem['role'] == 'user':
      nome_messagem = mensagem['content'][:30]
      break
  return nome_messagem  
    
def salva_mensagens(mensagens):
  if len(mensagens) == 0:
    return False
  
  nome_messagem = retorna_nome_da_mensagem(mensagens)
  nome_arquivo = converte_nome_mensagem(nome_messagem)    
  arquivo_salvar = {'nome_mensagem': nome_messagem, 
                    'nome_arquivo': nome_arquivo,
                    'mensagens': mensagens}
  with open(PASTA_MENSAGENS / nome_arquivo, 'wb') as f:
    pickle.dump(arquivo_salvar, f)

def ler_mensagem_por_nome_arquivo(nome_arquivo, key='mensagens'):
  with open(PASTA_MENSAGENS / nome_arquivo, 'rb') as f:
    mensagens = pickle.load(f)
  return mensagens[key]
 
def ler_mensagem(mensagens, key='mensagens'):
  if len(mensagens) == 0:
    return []
  nome_messagem = retorna_nome_da_mensagem(mensagens)
  nome_arquivo = converte_nome_mensagem(nome_messagem)  
  with open(PASTA_MENSAGENS / nome_arquivo, 'rb') as f:
    mensagens = pickle.load(f)
  return mensagens[key]

def listar_conversas():
  conversas = list(PASTA_MENSAGENS.glob('*'))
  conversas = sorted(conversas, key=lambda item: item.stat().st_mtime_ns, reverse=True)
  return [c.stem for c in conversas]

def salvar_api_key(chave):
  with open(PASTA_CONFIGURACOES / 'chave', 'wb') as f:
    pickle.dump(chave, f)

def ler_api_key():
  if (PASTA_CONFIGURACOES / 'chave').exists():
    with open(PASTA_CONFIGURACOES / 'chave', 'rb') as f:
      return pickle.load(f)    
  else:
    return ''  