#Descricao: programa que ira automatizar o cadastro produtos de uma lista .cvs 
#predefinida em um sistema utilizando a biblioteca pyautogui e o sistema MacOS

import pyautogui
import time
pyautogui.pause = 0.5

#pyautogui.pause = 0.5 #para que os comandos nao se atropelem  
#Passo a Passo do projeto

#1.Abrir o Chrome
time.sleep(1) #para que de tempo dele escrever no spotlight
pyautogui.hotkey("command","space",interval=0.25) #para abrir o Spotlight
pyautogui.write("chrome")
pyautogui.press("enter") 
time.sleep(1)

#2.Acessar o site para cadastrar os produtos
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(1) #para aguardar a tela abrir

#3.fazer login 
pyautogui.press("tab")
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("sua senha")
pyautogui.press("enter")
time.sleep(1)
pyautogui.press("enter")
#4.Abrir/importar a base de dados do produto para cadastrar
import pandas as pd 
tabela = pd.read_csv("/Users/maducagy/Desktop/Projetos/backEndProjects/intensicaoPython/produtos.csv")
#5.Realizar o cadastro dos produtos
for linha in tabela.index:
    #preencher codigo
    pyautogui.click(x=566, y=320)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
    #preencher marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    #preencher tipo
    tipo = str(tabela.loc[linha,"tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    #preencer categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    #preencher preco
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")
    #preencher custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    #preencher obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)
#6.Repetir isso tudo para cada produto    

