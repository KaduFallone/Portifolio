#Letra A
def maior(vetor):
    ordenado = sorted(vetor)
    return ordenado[-1]

#Letra B
def media(vetor):
    tamanho_vetor = len(vetor)
    soma = sum(vetor)
    return soma/tamanho_vetor

#Letra C
def ordemCrescente(vetor):
    crescente = sorted(vetor)
    return crescente 

#Letra D
def primo(vetor):
    def primo(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    return [x for x in vetor if primo(x)]