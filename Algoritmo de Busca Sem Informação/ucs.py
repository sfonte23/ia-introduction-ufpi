'''O algoritmo começa no nó inicial e explora os nós adjacentes com base no custo acumulado de chegar até eles.
Ele usa uma fila de prioridade (geralmente implementada com uma min-heap) para sempre expandir o nó com o menor custo acumulado até o momento.
Quando ele chega ao nó objetivo, o custo desse nó será o menor possível.'''

import heapq

def uniform_cost_search(graph, start, goal):
    # Fila de prioridade (usando heapq)
    queue = []
    heapq.heappush(queue, (0, start))  # (custo acumulado, nó atual)
    
    # Dicionário para armazenar o menor custo para chegar a cada nó
    cost_so_far = {start: 0}
    
    # Dicionário para armazenar os pais dos nós (para reconstruir o caminho)
    came_from = {start: None}

    while queue:
        # Remove o nó com o menor custo acumulado da fila
        current_cost, current_node = heapq.heappop(queue)

        # Verifica se chegamos ao objetivo
        if current_node == goal:
            break

        # Explora os vizinhos do nó atual
        for neighbor, edge_cost in graph[current_node]:
            new_cost = current_cost + edge_cost

            # Só consideramos expandir este caminho se ele for mais barato
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                came_from[neighbor] = current_node
                heapq.heappush(queue, (new_cost, neighbor))

    # Reconstrução do caminho
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = came_from[node]
    
    path.reverse()  # Reverter o caminho para que ele comece no início

    return path, cost_so_far[goal]

# Grafo de exemplo (nós, com custos das arestas)
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('E', 5)],
    'C': [('A', 4), ('F', 3)],
    'D': [('B', 2)],
    'E': [('B', 5), ('F', 1)],
    'F': [('C', 3), ('E', 1)]
}

# Executar a busca de custo uniforme de 'A' para 'F'
path, cost = uniform_cost_search(graph, 'A', 'F')
print("Caminho:", path)
print("Custo total:", cost)
