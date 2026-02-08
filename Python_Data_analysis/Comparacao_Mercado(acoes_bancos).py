import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import yfinance as yf
import mplcyberpunk as mcp
plt.style.use("cyberpunk")

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


#Reamostrar os dados para período anual
def resample_periodo(dado, periodo):
    dado_periodo_novo = dado.resample(f"{periodo}").last()
    dado_periodo_novo = dado_periodo_novo.pct_change()
    dado_periodo_novo = dado_periodo_novo.dropna()

    return dado_periodo_novo


#Calcular os anos onde a cotação do ativo esteve a cima da cotação do mercado
def longShort_mercado(dados_ativo, periodo, nome_ativo):
    long = resample_periodo(dados_ativo, periodo)
    short = resample_periodo(dados_mercado, periodo)
    long, short = long.align(short, join="inner")
    outperform = (long - short) * 100

    print(outperform)

    plt.figure(figsize=(10,5))
    plt.plot(outperform.index, outperform.values, marker="o")
    plt.title(f"Long x Short - Comparação: {nome_ativo} / Mercado")
    plt.ylabel("Diferença (%)")
    plt.grid(True)
    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter())
    plt.show()



#Análise Long/Short anual para o Banco do Brasil
longShort_mercado(banco_do_brasil, "YE", "BB")
longShort_mercado(santander, "YE", "Santander")
longShort_mercado(itau, "YE", "Itau")
longShort_mercado(bradesco, "YE", "Bradesco")