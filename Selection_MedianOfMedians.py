#Lista de números - Não Assume que está Ordenada
#k - K-ésimo menor elemento da Lista
import statistics
import math
import random
import time

import matplotlib.pyplot as plt

def BubbleSort(Lista):
    tamanhoLista = len(Lista)

    invertido = False

    for i in range(tamanhoLista - 1):
        for j in range(0,tamanhoLista-i-1):
            if Lista[j] > Lista[j+1]:
                invertido = True
                Lista[j],Lista[j+1] = Lista[j+1],Lista[j]
        if not invertido:
            return

def SortSelection(Lista,k):
    Lista = [*set(Lista)]
    BubbleSort(Lista)
    return Lista[k-1]

def LinearSelection(Lista,k):
    Lista = [*set(Lista)]
    
    if(k < 0 or k > len(Lista)):
       raise Exception("Valor de 'k' é Inválido")

    if(len(Lista) <= 1):
        #print("Atingiu Caso Base")
        return Lista[0]

    #Passo 1.: Dividir a Lista em n/5 grupos de tamanho 5
    #          Os que sobrarem entram em um Grupo de n mod 5 elementos
    n = len(Lista)
    quantidadeGrupos = (int)(n/5)

    listaGrupos = []
    Mediana = []
    
    for i in range(quantidadeGrupos):
        indiceMenor = i*5
        indiceMaior = (i+1)*5
        
        listaGrupos.append(Lista[indiceMenor:indiceMaior])
        BubbleSort(listaGrupos[i])

        #Mediana
        mediana = statistics.median(listaGrupos[i])
        Mediana.append(mediana)


    #Tratar Lista Restante
    #Passo 2.: Ordenar cada Grupo de até 5 e encontrar a mediana dentro dele
    tamanhoUltimoGrupo = (int)(n%5)

    if tamanhoUltimoGrupo > 0:
        ultimoGrupo = Lista[(quantidadeGrupos*5):(quantidadeGrupos*5) + tamanhoUltimoGrupo]

        BubbleSort(ultimoGrupo)

        indiceMedianaUltimoGrupo = math.floor((tamanhoUltimoGrupo-1)/2)
        mediana = ultimoGrupo[indiceMedianaUltimoGrupo]  #floor[(n-1)/2]
        Mediana.append(mediana)

        listaGrupos.append(ultimoGrupo)

    BubbleSort(Mediana)
    
    #Passo 3.: Usar a Chamada Recursiva para Encontrar a Mediana entre as Medianas
    medianaDaMediana = LinearSelection(Mediana,math.floor(len(Mediana)/2))

    #Passo 4.: Dividir em Dois vetores. Um com elementos Menores que a MedianaDasMedianas
    #          outro com os Elementos Maiores
    listaEsquerda = []
    listaDireita = []

    for i in range(len(Lista)):
        if (Lista[i] < medianaDaMediana):
            listaEsquerda.append(Lista[i])
        elif (Lista[i] > medianaDaMediana):
            listaDireita.append(Lista[i])

    if len(listaEsquerda) == k-1:
        return medianaDaMediana
    elif len(listaEsquerda) > k-1:
        return LinearSelection(listaEsquerda,k)
    elif len(listaEsquerda) < k-1:
        return LinearSelection(listaDireita,k-len(listaEsquerda)-1)

#Exemplo do Slide
#Lista = [2,5,91,19,24,54,5,87,9,10,44,32,18,13,21,4,23,26,16,191,25,39,47,56,71]
#k = 2

base = 1000
numeroInstancias = 10
quantidadePassos = 10
limiteInferior = 1
limiteSuperior = 100000

Lista = []

somaSort = [0]*quantidadePassos
somaLinear = [0]*quantidadePassos

mediasSort = []
mediasLinear = []

#Gerar Instâncias
for n in range(numeroInstancias):
    for i in range(1,quantidadePassos+1):
        ListaAleatoria = []

        for j in range(base*i):
            numero = round(random.uniform(limiteInferior,limiteSuperior),1)
            ListaAleatoria.append(numero)

        Lista.append(ListaAleatoria)


#Teste de Corretude
    for i in range(quantidadePassos):
        k = (int)(len(Lista[i])/2)
        index = (int)((len(Lista[i])/base)-1)
    
        tempoInicial = time.time()
        resultadoSortSelection = SortSelection(Lista[i],k)
        tempoFinal = time.time()
    
        tempoDecorrido = round(tempoFinal - tempoInicial,2)
        somaSort[index] += tempoDecorrido

        tempoInicial = time.time()
        resultadoLinearSelection = LinearSelection(Lista[i],k)
        tempoFinal = time.time()

        tempoDecorrido = round(tempoFinal - tempoInicial,2)
        somaLinear[index] += tempoDecorrido    

        print(i,len(Lista[i]),k,resultadoSortSelection,resultadoLinearSelection)

#Executa o Cálculo das Médias para Cada Tamanho n
i = 1
for x in somaSort:
    n = (base*i)
    mediasSort.append((n,x/numeroInstancias))
    i += 1

i = 1  
for x in somaLinear:
    n = (base*i)
    mediasLinear.append((n,x/numeroInstancias))
    i += 1

xSort,ySort = zip(*mediasSort)
xLinear,yLinear = zip(*mediasLinear)

plt.scatter(xSort,ySort,color = 'blue')
plt.scatter(xLinear,yLinear,color = 'red')
plt.xlabel("Tamanho da Entrada")
plt.ylabel("Tempo Médio de Execução")
plt.show()

    


