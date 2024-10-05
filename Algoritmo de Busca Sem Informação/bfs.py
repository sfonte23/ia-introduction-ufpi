'''A busca em largura (BFS - Breadth First Search) é um algoritmo de travessia de grafos que explora todos os vizinhos de um vértice antes de ir mais fundo em outros vértices. Ela utiliza uma fila (queue) para armazenar os nós que precisam ser explorados, garantindo que os nós são visitados em camadas (ou níveis) a partir do nó inicial.'''

from collections import deque

# Função de Busca em Largura (BFS)
def bfs(graph, start):
    visited = set()        # Conjunto para armazenar nós visitados
    queue = deque([start]) # Fila para explorar os nós, começando pelo nó inicial

    visited.add(start)      # Marca o nó inicial como visitado

    while queue:
        # Remove o próximo nó da fila
        current = queue.popleft()
        print(current)  # Exibir o nó visitado (ou processar de outra forma)

        # Visita todos os vizinhos não visitados
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)  # Marca o vizinho como visitado
                queue.append(neighbor) # Adiciona o vizinho à fila

# Grafo de exemplo (usando lista de adjacência)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Executar a busca em largura começando do nó 'A'
bfs(graph, 'A')
