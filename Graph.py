import itertools
    
def BFS_Vertices(G,s):
    Niveis = []
    Niveis.append([s])
    G[s][1] = True  #Marcar como Visitado

    i = 1

    while True:
        Niveis.append([])
        for u in Niveis[i-1]:
            for v in G[u][0]:
                if G[v][1] == False:
                    Niveis[i].append(v)
                    G[v][1] = True #Marcar como Visitado
        if len(Niveis[i]) == 0:
            return i,Niveis[i-1] #Numero de Níveis,Configuração Último Nível
        i += 1

def BFS_Grafo(G):
    quantidadeComponentes = 0

    for vertice in G:
        if G[vertice][1] == False:

            BFS_Vertices(G,vertice)
            
            quantidadeComponentes += 1

    return quantidadeComponentes

def CalcularCaminhoMaisCurto (G,s):
    profundidadeMaiorNivel,Niveis = BFS_Vertices(G,s)
    return profundidadeMaiorNivel,Niveis

def GerarListaMovimentos(estado):
    listaMovimentos = []

    asterisco = estado.index('*')

    switcher = {
        0: [estado[1] + estado[0] + estado[2:],estado[3]+ estado[1:3] + estado[0]+ estado[4:]],
        1: [estado[1] + estado[0] + estado[2:],estado[0] + estado[2] + estado[1] + estado[3:],
            estado[0] + estado[4] + estado[2:4] + estado[1] + estado[5:]],
        2: [estado[0] + estado[2] + estado[1] + estado[3:],estado[:2] + estado[5] + estado[3:5] + estado[2] + estado[6:]],
        3: [estado[3] + estado[1:3] + estado[0] + estado[4:],estado[:3] + estado[4] + estado[3] + estado[5:],
            estado[:3] + estado[6] + estado[4:6] + estado[3] + estado[7:]],
        4: [estado[0] + estado[4] + estado[2:4] + estado[1] + estado[5:],estado[:3] + estado[4] + estado[3] + estado[5:],
            estado[:4] + estado[5] + estado[4] + estado[6:],estado[:4] + estado[7] + estado[5:7] + estado[4] + estado[8]],
        5: [estado[:2] + estado[5] + estado[3:5] + estado[2] + estado[6:],estado[:4] + estado[5] + estado[4] + estado[6:],
            estado[:5] + estado[8] + estado[6:8] + estado[5]],
        6: [estado[:3] + estado[6] + estado[4:6] + estado[3] + estado[7:],estado[:6] + estado[7] + estado[6] + estado[8]],
        7: [estado[:4] + estado[7] + estado[5:7] + estado[4] + estado[8],estado[:6] + estado[7] + estado[6] + estado[8],
            estado[:7] + estado[8] + estado[7]],
        8: [estado[:5] + estado[8] + estado[6:8] + estado[5],estado[:7] + estado[8] + estado[7]]
    }
 
    return switcher.get(asterisco, [])

#Inicialização do Dicionário com todas as Movimentações Possíveis
#Dicionário possui uma Chave[Nó do Grafo] e no Valor uma Tupla (Movimentos Possíveis,Visitado_V_ou_F)

estadoInicial = '*12345678'
quantidadeNos = 0
quantidadeArestas = 0

listaEstados = ([''.join(estado) for estado in itertools.permutations(estadoInicial)])

Grafo = {key: value for key, value in []}

for estado in listaEstados:
    listaMovimentos = GerarListaMovimentos(estado)
    #Inicializar os Nós com a Coloração False == Não Visitado
    Grafo[estado] = list((listaMovimentos,False))
    quantidadeArestas += len(listaMovimentos)
    quantidadeNos += 1

print("Item 1a. Quantidade de Nós.:",quantidadeNos)
print("Item 1a. Quantidade de Arestas.:",quantidadeArestas)
print("Item 1b. Nós  Conectados por Uma Aresta.:",'*23146758','-->',Grafo['*23146758'][0][0])
print("Item 1c. Nós  não Conectados por Uma Aresta.:",'*23146758',Grafo['2647135*8'][0][0])

quantidadeComponentes = BFS_Grafo(Grafo)

print("Item 2. Quantidade de Componentes Conexos do Grafo.:",quantidadeComponentes)

configuracaoFinal = '12345678*'

for vertice in Grafo: #Reiniciar os Vertices como 'Não Visitados'
    Grafo[vertice][1] = False

profundidadeMaiorNivel,maxViaveis = CalcularCaminhoMaisCurto(Grafo,configuracaoFinal)
print("Item 3a. Configuração Inicial Viável com Maior Número de Movimentos Necessários.:",maxViaveis)
print("Item 3b. Maior Número de Movimentos Necessários.:",profundidadeMaiorNivel)

