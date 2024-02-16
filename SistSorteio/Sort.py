from random import sample

# Função para encontrar o vértice com a chave mínima
def min_key(vertices, key, mst_set):
    min_val = float('inf')
    min_index = -1
    for v in range(vertices):
        if key[v] < min_val and not mst_set[v]:
            min_val = key[v]
            min_index = v
    return min_index

# Função para imprimir a Árvore Geradora Mínima
def print_mst(parent, graph):
    print("Aresta \tPeso")
    for i in range(1, len(graph)):
        print(parent[i], "-", i, "\t", graph[i][parent[i]])

# Função para implementar o algoritmo de Prim e encontrar a Árvore Geradora Mínima
def prim_mst(graph):
    vertices = len(graph)
    key = [float('inf')] * vertices
    parent = [None] * vertices
    key[0] = 0
    mst_set = [False] * vertices
    parent[0] = -1
    for _ in range(vertices - 1):
        u = min_key(vertices, key, mst_set)
        mst_set[u] = True
        for v in range(vertices):
            if 0 < graph[u][v] < key[v] and not mst_set[v]:
                key[v] = graph[u][v]
                parent[v] = u
    print_mst(parent, graph)

# Lista de opções do sorteio
options = list(range(1, 101))
print(f'Opções do sorteio:\n{options}')
# Sorteio de 3 números sem repetição
sorteados = sample(options, 3)
print("=="*60)
print(f'\nResultado do sorteio: {sorteados}')
print("=="*60)

graph = [[0] * 3 for _ in range(3)] #criação de uma matriz de adjacência
for i in range(3):
    for j in range(i + 1, 3):
        distance = abs(sorteados[i] - sorteados[j])
        graph[i][j] = distance
        graph[j][i] = distance
print('\nMatriz de adjacência do grafo:')
for row in graph:
    print(row)
print("=="*60)
print('\nÁrvore Geradora Mínima:')
prim_mst(graph)
print("=="*60)
