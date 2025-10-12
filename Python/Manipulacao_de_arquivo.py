def escrever():
        with open("Prb06", "a") as arq:
            y = True
            while y == True:
                nomes = str(input("De um nome:"))
                arq.write(nomes + "\n") 
                escolha = int(input("Escrever mais = 1 \nPara de escrever = 0\nR:"))
                print("\n")
                if escolha == 1:
                    y = True 
                elif escolha == 0:
                    y = False
                else:
                    y = False
                    print("Valor invalido!!\n")
                    
                    
                
                     

def imprimir():
    try:
        with open("Prb06", "r") as arq:
            dados = arq.readlines()
            print(dados)
    except Exception as erro:
        print(TypeError)

i = True
while i == True:
    
        opcao = int(input("Grava = 1 \nImprimir = 0\nR:"))
        print("\n")
        
        if opcao == 1:
            escrever()
        
        elif opcao == 0:
            imprimir()
        else:
            print("Valor invalido!!\n")
            breakpoint
    
        opcao2 = int(input("Deseja voltar ao menu principal? \nSim = 1 \nNão = 0\nR:"))
        print("\n")
        if opcao2 == 1:
            i = True 
        elif opcao2 == 0:
            i = False
        else:
             print("Valor invalido!!\nPrograma incerrará\n")
    
        
                        
        


