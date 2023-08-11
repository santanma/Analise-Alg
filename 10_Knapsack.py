import numpy as np

def InicializarInstancias (nomeArquivoInstancia):
    arquivo = open(nomeArquivoInstancia,"r")
    primeiraLinha = arquivo.readline()
    
    n = (int)(primeiraLinha.split()[0])
    B = (int)(primeiraLinha.split()[1])
    
    w = [] 
    v = [] 

    for linha in arquivo:
        v.append((int)(linha.split()[0]))
        w.append((int)(linha.split()[1]))
             
    return n,B,v,w

def Knapsack10(B,v,w,index,U,dp):
    if index == 0:
        return (B // w[0]) * v[0]

    if dp[index][B] != -1:
        return dp[index][B]

    #Pegar ou Não Pegar o Item na Mochilha
    #Posso Pegar se a quantidade de Itens que já pegamos do mesmo tipo for
    # igual ou inferior a 10 unidades e se a Capacidade não estiver estourada
    naoPegarItem = Knapsack10(B,v,w,index-1,10,dp)
    
    pegarItem = float('-inf')
    
    if w[index] <= B and U > 0:
        pegarItem = v[index] + Knapsack10(B-w[index],v,w,index,U-1,dp)

    dp[index][B] = max(pegarItem,naoPegarItem)
    return dp[index][B]

nomeArquivoInstancia = "inst8"
U = 10
dp = []

n,B,v,w = InicializarInstancias(nomeArquivoInstancia)
dp = [[-1 for _ in range(B+1)] for _ in range(n)]

print(n,B,v,w)
print("Solução Ótima",Knapsack10(B,v,w,n-1,U,dp))
#print(dp)


#Encontrar a Solução Ótima, além do Valor
#A Partir da Matriz de Memoização conseguimos ir Lendo de Baixo para
#cima as Linhas e Fazendo uma Varredura simples podemos descobrir o
#conjunto ótimo

#Pegar o último elemento da matriz
#Verificar se ele estava presente na linha acima, caso sim passa para cima
#caso não consome um elemento e verifica novamente até conseguir

ultimoElemento = dp[n-1][B]
linhaCorrente = n-2

resultado = dict()
for i in range(n):
    resultado.update({i+1:0})

while linhaCorrente >= 0:
    vetorLinha = dp[linhaCorrente][:]
    retorno = vetorLinha.index(ultimoElemento) if ultimoElemento in vetorLinha else -1

    if retorno == -1:
        if linhaCorrente == 0:
            valorZero = v[linhaCorrente]
            valorUm = v[linhaCorrente+1]

            if (ultimoElemento % valorZero) == 0:
                resultado[linhaCorrente+1] = resultado.get(linhaCorrente+1,0) + ultimoElemento // valorZero
            else:
                resultado[linhaCorrente+2] = resultado.get(linhaCorrente+2,0) + ultimoElemento // valorUm

            linhaCorrente -= 1 # Para fechar o Algoritmo
        else:      
            ultimoElemento -= v[linhaCorrente+1]
            resultado[linhaCorrente+2] = resultado.get(linhaCorrente+2,0) + 1
    else:
        linhaCorrente -= 1

for chave,valor in resultado.items():
    print("Foram usados ",valor," do item",chave)	
    
