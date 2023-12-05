from queue import PriorityQueue

def uniform_cost_search(graph, start_node, goal_node):
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start_node, [start_node]))

    while not queue.empty():
        (cost, current_node, path) = queue.get()

        if current_node not in visited:
            visited.add(current_node)

            if current_node == goal_node:
                return cost, path

            for neighbor, neighbor_cost in graph[current_node].items():
                total_cost = cost + neighbor_cost
                queue.put((total_cost, neighbor, path + [neighbor]))

    return None

graph = {
    'brebes': {'tegal': 33, 'slawi': 32},
    'tegal': {'brebes': 33, 'slawi': 20, 'pemalang': 30},
    'slawi': {'brebes': 32, 'tegal': 20, 'purwokerto': 50},
    'pemalang': {'tegal': 30, 'purbalingga': 69, 'pekalongan': 35},
    'pekalongan': {'pemalang': 35, 'kendal': 71},
    'kendal': {'pekalongan': 71, 'temanggung': 80, 'semarang': 29},
    'semarang': {'kendal': 29, 'salatiga': 48, 'demak': 26},
    'demak': {'semarang': 26, 'purwodadi': 21, 'kudus': 25},
    'kudus': {'demak': 25, 'purwodadi': 46, 'rembang': 80},
    'rembang': {'kudus': 80, 'blora': 36},
    'purwokerto': {'slawi': 50, 'cilacap': 61, 'kroya': 30, 'kebumen': 75, 'purbalingga': 30},
    'cilacap': {'purwokerto': 61, 'kroya': 28},
    'kroya': {'purwokerto': 30, 'cilacap': 28, 'kebumen': 50},
    'kebumen': {'purwokerto': 75, 'kroya': 50, 'purworejo': 44},
    'purbalingga': {'purwokerto': 30, 'pemalang': 69, 'banjarnegara': 49},
    'banjarnegara': {'purbalingga': 49, 'wonosobo': 31},
    'wonosobo': {'banjarnegara': 31, 'magelang': 62, 'temanggung': 43},
    'temanggung': {'wonosobo': 43, 'kendal': 80, 'salatiga': 52, 'magelang': 23},
    'salatiga': {'temanggung': 52, 'semarang': 48, 'boyolali': 27},
    'purworejo': {'kebumen': 44, 'magelang': 43},
    'magelang': {'purworejo': 43, 'wonosobo': 62, 'temanggung': 23, 'boyolali': 42},
    'boyolali': {'magelang': 42, 'salatiga': 27, 'solo': 35, 'klaten': 38},
    'klaten': {'boyolali': 38},
    'solo': {'boyolali': 35, 'purwodadi': 42, 'sragen': 32, 'sukoharjo': 12},
    'sukoharjo': {'solo': 12, 'wonogiri': 42},
    'wonogiri': {'sukoharjo': 42},
    'sragen': {'solo': 32, 'blora': 84},
    'purwodadi': {'demak': 21, 'kudus': 46, 'solo': 42, 'blora': 62},
    'blora': {'purwodadi': 62, 'rembang': 36, 'sragen': 84}
}

start_node = input("Masukkan node awal: ")
goal_node = input("Masukkan node tujuan: ")

result = uniform_cost_search(graph, start_node, goal_node)

if result is None:
    print("Tidak ada rute dari {} ke {}".format(start_node, goal_node))
else:
    cost, path = result
    print("Rute terpendek dari {} ke {} adalah: {}".format(start_node, goal_node, " -> ".join(path)))
    print("Dengan jarak total: {} kilometer".format(cost))
