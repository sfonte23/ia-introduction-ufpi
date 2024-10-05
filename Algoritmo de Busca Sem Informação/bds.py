'''A busca bidirecional é uma técnica de busca que explora dois caminhos simultaneamente: um a partir do nó inicial e outro a partir do nó objetivo. O objetivo é encontrar o ponto de interseção entre os dois caminhos, o que pode levar a uma solução mais rápida em comparação com buscas unidimensionais.'''

from collections import deque

def bidirectional_search(graph, start, goal):
    # Filas para as buscas
    queue_start = deque([start])
    queue_goal = deque([goal])
    
    # Conjuntos para os nós visitados
    visited_start = {start}
    visited_goal = {goal}
    
    # Dicionários para rastrear os pais dos nós
    parent_start = {start: None}
    parent_goal = {goal: None}

    while queue_start and queue_goal:
        # Busca do lado do início
        current_start = queue_start.popleft()
        for neighbor in graph.get(current_start, []):
            if neighbor not in visited_start:
                visited_start.add(neighbor)
                parent_start[neighbor] = current_start
                queue_start.append(neighbor)
                
                # Verifica interseção com a busca do objetivo
                if neighbor in visited_goal:
                    return reconstruct_path(parent_start, parent_goal, neighbor)

        # Busca do lado do objetivo
        current_goal = queue_goal.popleft()
        for neighbor in graph.get(current_goal, []):
            if neighbor not in visited_goal:
                visited_goal.add(neighbor)
                parent_goal[neighbor] = current_goal
                queue_goal.append(neighbor)
                
                # Verifica interseção com a busca do início
                if neighbor in visited_start:
                    return reconstruct_path(parent_start, parent_goal, neighbor)

    return None  # Se não encontrar caminho

def reconstruct_path(parent_start, parent_goal, meeting_point):
    # Reconstrói o caminho a partir do nó de interseção
    path_start = []
    node = meeting_point
    while node is not None:
        path_start.append(node)
        node = parent_start[node]
    path_start.reverse()  # Inverte para obter a ordem correta

    path_goal = []
    node = meeting_point
    while node is not None:
        path_goal.append(node)
        node = parent_goal[node]

    # Combina os dois caminhos, excluindo o ponto de interseção repetido
    return path_start[:-1] + path_goal[::-1]

# Exemplo de grafo
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

# Executa a busca bidirecional para encontrar o caminho entre 'A' e 'H'
path = bidirectional_search(graph, 'A', 'H')
print("Caminho encontrado:", path)
