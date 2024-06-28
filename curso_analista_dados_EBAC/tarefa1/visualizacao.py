import pandas as pd
import seaborn as sns

# Lê o arquivo CSV
df = pd.read_csv('taxa-cdi.csv')
    
#gerar grafico
plot_df = sns.lineplot(x='data_hora', y='taxa', data=df, marker='o')
plot_df.tick_params(axis='x', labelrotation=45)

# Salva o gráfico em um arquivo
plot_df.figure.savefig("grafico.png")
print('Sucesso')