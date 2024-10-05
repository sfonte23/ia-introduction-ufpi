'''A busca gulosa (ou greedy search) é um algoritmo de busca que toma decisões locais ótimas em cada etapa, com a esperança de que essas escolhas levarão a uma solução global ótima. O algoritmo utiliza uma função heurística para estimar o custo de chegar ao objetivo a partir de um determinado nó e prioriza os nós com base nesse custo estimado.'''

import heapq

def greedy_search(graph, start, goal, heuristic):
    # Fila de prioridade (usando heapq)
    queue = []
    heapq.heappush(queue, (0, start))  # (custo heurístico, nó atual)
    
    # Conjunto para armazenar nós visitados
    visited = set()
    
    # Dicionário para armazenar o caminho
    parent = {start: None}

    while queue:
        # Remove o nó com menor custo heurístico
        current_cost, current_node = heapq.heappop(queue)

        # Se chegamos ao objetivo, reconstruímos o caminho
        if current_node == goal:
            return reconstruct_path(parent, goal)

        visited.add(current_node)

        # Explora os vizinhos do nó atual
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                # Adiciona o custo heurístico do vizinho
                heapq.heappush(queue, (heuristic[neighbor], neighbor))
                # Atualiza o caminho
                parent[neighbor] = current_node

    return None  # Se não encontrar caminho

def reconstruct_path(parent, goal):
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()  # Inverte para obter a ordem correta
    return path

# Exemplo de grafo (nós com seus vizinhos)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'H'],
    'E': ['B', 'H'],
    'F': ['C'],
    'H': ['D', 'E']
}

# Heurística para cada nó (valores fictícios)
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 3,
    'F': 4,
    'H': 0
}

# Executa a busca gulosa de 'A' para 'H'
path = greedy_search(graph, 'A', 'H', heuristic)
print("Caminho encontrado:", path)
