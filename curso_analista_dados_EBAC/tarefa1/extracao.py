import requests
import pandas as pd
import os
from datetime import datetime
import seaborn as sns
from time import sleep


# Função para extrair a taxa CDI do site do Banco Central
url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.12/dados?formato=json"

response = requests.get(url, timeout=10)  # Faz uma requisição HTTP GET ao URL com um timeout de 10 segundos
response.raise_for_status()  # Levanta uma exceção para códigos de status HTTP ruins
data = response.json()  # Faz o parsing do conteúdo JSON
taxa_cdi = data[-1]['valor']  # Extrai a última taxa CDI disponível     

# Função para salvar a taxa CDI em um arquivo CSV
for _ in range(0,10):
    data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Obtém a data e hora atuais formatadas
    file_exists = os.path.isfile('./taxa-cdi.csv')  # Verifica se o arquivo CSV já existe
    if file_exists:
        df = pd.read_csv("taxa-cdi.csv")  # Lê o arquivo CSV existente
    else:
        df = pd.DataFrame(columns=['data_hora', 'taxa'])  # Cria um DataFrame vazio com colunas específicas
    
    # Adiciona uma nova linha ao DataFrame com a data/hora e a taxa
    new_row = pd.DataFrame({'data_hora': [data_hora], 'taxa': [taxa_cdi]})
    df = pd.concat([df, new_row], ignore_index=True)
    
    df.to_csv('taxa-cdi.csv', index=False)  # Salva o DataFrame no arquivo CSV
    print("Taxa CDI salva com sucesso")
    sleep(1)
