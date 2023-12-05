def uniform_cost_search(graph, start, goal):
    queue = [(0, start, [])]
    visited = set()

    while queue:
        (cost, node, path) = queue.pop(0)
        if node not in visited:
            visited.add(node)
            path = path + [node]

            if node == goal:
                return cost, path

            for neighbor, edge_cost in graph[node].items():
                if neighbor not in visited:
                    total_cost = cost + edge_cost
                    queue.append((total_cost, neighbor, path))
            queue.sort(key=lambda x:x[0])

    return None, None

graph = {
    'A': {'B': 40, 'C': 56, 'D': 68, 'E': 70, 'F': 88, 'G': 180},
    'B': {'C': 56, 'D': 68, 'E': 70, 'F': 88, 'G': 160},
    'C': {'D': 68, 'E': 65, 'F': 88, 'G': 160},
    'D': {'F': 17, 'G': 32},
    'E': {'D': 22, 'F': 55, 'G': 54},
    'F': {'G': 29},
    'G': {}
}

cost, path = uniform_cost_search(graph, 'A', 'G')
print(f"Rute terpendek dari A ke G adalah {path} dengan biaya {cost}")
