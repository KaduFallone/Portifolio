import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import yfinance as yf
import mplcyberpunk as mcp
plt.style.use("cyberpunk")

#Carregar os dados de lucro dos bancos
lucro_bancos = pd.read_excel("lucros_bancos.xlsx")


#Criar grafico para comparar a variação do lucro dos bancos (lucro_bancos.xlsx)
lucro_bancos = lucro_bancos.set_index("data")
variacao_lucro = lucro_bancos.iloc[-1]/lucro_bancos.iloc[0] -1
variacao_lucro = variacao_lucro * 100
variacao_lucro = variacao_lucro.sort_values(ascending = False) 

#Criar gráfico de barras simples para a variação do lucro dos bancos
fig, ax = plt.subplots()
ax.bar(x = variacao_lucro.index, height = variacao_lucro.values)
ax.yaxis.set_major_formatter(mtick.PercentFormatter())
plt.xticks(fontsize = 9)
plt.show()
