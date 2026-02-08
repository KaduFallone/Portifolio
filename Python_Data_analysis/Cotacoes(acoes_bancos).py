import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import yfinance as yf
import mplcyberpunk as mcp

#Selecionar os astivos bancários e o índice Bovespa
lista_tickers = ["BBAS3.SA","SANB4.SA","ITUB4.SA","BBDC4.SA","^BVSP"]
dados_bancarios = yf.download(lista_tickers, start="2009-12-31", end="2021-12-31")

#Selecionar apenas os preços de fechamento
dados_bancarios = dados_bancarios["Close"]

#Carregar os dados de lucro dos bancos
lucro_bancos = pd.read_excel("lucros_bancos.xlsx")

#Separar os dados de cada banco e do índice Bovespa
banco_do_brasil = dados_bancarios["BBAS3.SA"]
santander = dados_bancarios["SANB4.SA"]
itau = dados_bancarios["ITUB4.SA"]
bradesco = dados_bancarios["BBDC4.SA"]
dados_mercado = dados_bancarios["^BVSP"]

#Cálculo dos retornos das ações (Valor da cotação final / Valor da cotação inicial - 1)
def retorno(lista_cotacoes):
    retorno = lista_cotacoes[-1] / lista_cotacoes[0] - 1

    return retorno 

#Calcular o retorno de cada ativo separadamente
retorno_bb = retorno(banco_do_brasil)
retorno_santander = retorno(santander)
retorno_itau = retorno(itau)
retorno_bradesco = retorno(bradesco)
retorno_dados_mercado = retorno(dados_mercado)

#Criar dataframe para armazenar os retornos
df_retorno = pd.DataFrame(
    data = {"retorno": [retorno_bb,retorno_santander,retorno_itau,retorno_bradesco,retorno_dados_mercado]},
    index = ["Banco do Brasil", "Santander", "Itau","Bradesco","Ibovespa"]
)

#Filtrar os retornos em porcentagem e ordenar em ordem decrescente
df_retorno = df_retorno * 100
df_retorno = df_retorno.sort_values(by = "retorno", ascending  = False)

#Criar gráfico de barras simples para os retornos
plt.style.use("cyberpunk")
fig, ax = plt.subplots()
ax.bar(x = df_retorno.index, height = df_retorno["retorno"])
ax.yaxis.set_major_formatter(mtick.PercentFormatter())
plt.xticks(fontsize = 9)
plt.show()