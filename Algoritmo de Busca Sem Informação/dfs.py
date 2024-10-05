'''
A busca em profundidade (DFS - Depth First Search) é um algoritmo de travessia ou busca em grafos e árvores. Ele explora o caminho completo de um vértice até o seu fim antes de retroceder e explorar outros caminhos, seguindo um princípio de exploração em profundidade.
'''
# Função de Busca em Profundidade (DFS)
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # Conjunto para armazenar nós visitados

    # Marcar o nó atual como visitado
    visited.add(start)
    print(start)  # Exibir o nó visitado (ou processar de outra forma)

    # Visitar cada vizinho não visitado recursivamente
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    
    return visited

# Grafo de exemplo (usando lista de adjacência)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Executar a busca em profundidade começando do nó 'A'
dfs(graph, 'A')
