import heapq
''' Um heap é uma estrutura de dados que mantém a propriedade de ordenação parcial, ou seja, o menor elemento está sempre no topo. No caso do min-heap, o menor valor sempre será removido primeiro, o que é muito útil em algoritmos como o A*, onde precisamos explorar primeiro os nós com menor custo estimado. O algoritmo A* (A estrela) é um dos mais conhecidos algoritmos de busca heurística. Ele utiliza tanto o custo real do caminho até o nó atual quanto uma estimativa (heurística) do custo para atingir o objetivo, e é amplamente utilizado em problemas de caminho mínimo em grafos, como em navegação e jogos.'''

# Função de heurística: Distância euclidiana
def heuristic(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

# Algoritmo A*
def a_star(graph, start, goal):
    # Fila de prioridade para os nós a serem explorados
    open_list = []
    heapq.heappush(open_list, (0, start))
    
    # Dicionário para armazenar o custo total do início até o nó atual
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    
    # Dicionário para armazenar o custo estimado do início até o objetivo passando por este nó
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic(start, goal)
    
    # Dicionário para rastrear o caminho
    came_from = {}

    while open_list:
        # Extrair o nó com menor f_score
        current = heapq.heappop(open_list)[1]
        
        # Se atingirmos o objetivo, reconstruímos o caminho
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Retorna o caminho invertido
        
        # Explorar os vizinhos
        for neighbor, cost in graph[current]:
            tentative_g_score = g_score[current] + cost
            
            # Se o caminho até o vizinho for melhor
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                
                # Adicionar à lista aberta se ainda não estiver nela
                heapq.heappush(open_list, (f_score[neighbor], neighbor))
    
    # Se o objetivo não foi encontrado
    return None

# Grafo de exemplo (cada nó tem uma lista de vizinhos com o custo do caminho)
graph = {
    (0, 0): [((1, 1), 1.4), ((0, 1), 1), ((1, 0), 1)],
    (1, 1): [((0, 0), 1.4), ((1, 2), 1), ((2, 1), 1)],
    (0, 1): [((0, 0), 1), ((1, 1), 1)],
    (1, 0): [((0, 0), 1), ((2, 0), 1)],
    (1, 2): [((1, 1), 1), ((2, 2), 1)],
    (2, 1): [((1, 1), 1), ((2, 2), 1)],
    (2, 0): [((1, 0), 1)],
    (2, 2): [((1, 2), 1), ((2, 1), 1)]
}

# Executar o algoritmo A*
start = (0, 0)
goal = (2, 2)
path = a_star(graph, start, goal)

if path:
    print("Caminho encontrado:", path)
else:
    print("Nenhum caminho encontrado.")
