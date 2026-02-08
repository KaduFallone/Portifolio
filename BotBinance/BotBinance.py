import pandas as pd
import os 
import time 
from binance.client import Client
from binance.enums import *
#Importar as variaveis de ambiente
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("KEY_BINANCE")
secret_key = os.getenv("SECRET_BINANCE")

cliente_binance = Client(api_key, secret_key)


codigo_operado = "XRPBRL"
ativo_operado = "XRP"
periodo_candle = Client.KLINE_INTERVAL_1HOUR
quantidade = 1.10

def pegando_dados(codigo, intervalo):
    #Capturar os dados das candles
    candles = cliente_binance.get_klines(symbol = codigo, interval = intervalo, limit = 1000)

    #Criar dataframes com os dados das candles
    precos = pd.DataFrame(candles)

    #Nomes das colunas do dataframe
    precos.columns = ["tempo_abertura", "abertura", "maxima", "minima", "fechamento", 
                      "volume", "tempo_fechamento", "moedas_negociadas", "numero_trades",
                      "volume_ativo_base_compra", "volume_ativo_cotação", "-"]
    
    #Selecionar as colunas que interessam
    precos = precos[["fechamento", "tempo_fechamento"]]
    #Converter os dados para float
    precos["fechamento"] = precos["fechamento"].astype(float)

    #Converter o tempo de fechamento para o horario de Brasilia
    precos["tempo_fechamento"] = pd.to_datetime(precos["tempo_fechamento"], unit = "ms").dt.tz_localize("UTC")
    precos["tempo_fechamento"] = precos["tempo_fechamento"].dt.tz_convert("America/Sao_Paulo")

    return precos


def estrategia_trade(dados, codigo_ativo, ativo_operado, quantidade, posicao):
    #Calcular as medias moveis
    dados["media_rapida"] = dados["fechamento"].rolling(window = 7).mean()
    dados["media_devagar"] = dados["fechamento"].rolling(window = 40).mean()

    #Pegar as ultimas medias moveis
    ultima_media_rapida = dados["media_rapida"].iloc[-1]
    ultima_media_devagar = dados["media_devagar"].iloc[-1]

    print(f"\nÚltima Média Rápida: {ultima_media_rapida} | Última Média Devagar: {ultima_media_devagar}")
    
    #Acesso da conta 
    conta = cliente_binance.get_account()

    #Verificação de saldo do ativo
    for ativo in conta["balances"]:

        if ativo["asset"] == ativo_operado:

            quantidade_atual = float(ativo["free"])

    #Compra de ativo
    if ultima_media_rapida > ultima_media_devagar:

        if posicao == False:

            order = cliente_binance.create_order(symbol = codigo_ativo,
                side = SIDE_BUY,
                type = ORDER_TYPE_MARKET,
                quantity = quantidade
                )


            print("ATIVO ADQUIRIDO")

            posicao = True

    #venda de ativo
    elif ultima_media_rapida < ultima_media_devagar:

        if posicao == True:

            order = cliente_binance.create_order(symbol = codigo_ativo,
                side = SIDE_SELL,
                type = ORDER_TYPE_MARKET,
                quantity = int(quantidade_atual * 1000)/1000)
            
            print("ATIVO VENDIDO")

            posicao = False

    return posicao

posicao_atual = False

#MAIN LOOP
while True:

    dados_atualizados = pegando_dados(codigo=codigo_operado, intervalo=periodo_candle)
    print("\n\nExecutando estratégia...:")
    posicao_atual = estrategia_trade(dados_atualizados, codigo_ativo=codigo_operado, 
                                        ativo_operado=ativo_operado, quantidade=quantidade, posicao=posicao_atual)
    time.sleep(60*60)
