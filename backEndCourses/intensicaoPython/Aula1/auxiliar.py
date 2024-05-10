import pandas
import pyautogui
import time

time.sleep(5)
print(pyautogui.position())

tabela = pandas.read_csv("/Users/maducagy/Desktop/Projetos/backEndProjects/intensicaoPython/produtos.csv")
#for linha in tabela.index:
#    codigo = str(tabela.loc[linha, "codigo"])
#    print(codigo)
