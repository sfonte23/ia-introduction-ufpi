'''A busca em profundidade limitada e a busca em profundidade iterativa são variações do algoritmo de busca em profundidade (DFS) que oferecem formas de controlar a profundidade de exploração e lidar melhor com certos tipos de problemas, como grafos muito profundos ou infinitos.'''

def depth_limited_search(graph, start, goal, limit):
    def recursive_dls(node, depth):
        if node == goal:
            return [node]  # Encontrou o objetivo
        elif depth == 0:
            return "limite atingido"  # Profundidade limite alcançada
        else:
            for neighbor in graph.get(node, []):
                result = recursive_dls(neighbor, depth - 1)
                if result != "limite atingido":
                    return [node] + result  # Constrói o caminho de volta
            return "limite atingido"

    return recursive_dls(start, limit)

# Exemplo de grafo
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [], 'E': [], 'F': [], 'G': []
}

# Busca com limite de profundidade 2
path = depth_limited_search(graph, 'A', 'F', 2)
print("Caminho encontrado:", path)
