# Define la matriz de distancias (ejemplo)
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Función para encontrar la ruta más corta usando el algoritmo de Dijkstra
def dijkstra(matrix, start):
    n = len(matrix)
    visited = [False] * n
    distance = [float('inf')] * n
    parent = [-1] * n

    distance[start] = 0

    for _ in range(n):
        min_distance = float('inf')
        nodo_actual = -1

        for i in range(n):
            if not visited[i] and distance[i] < min_distance:
                min_distance = distance[i]
                nodo_actual = i

        visited[nodo_actual] = True

        for nodo_destino in range(n):
            if not visited[nodo_destino] and matrix[nodo_actual][nodo_destino] > 0 and distance[nodo_actual] + matrix[nodo_actual][nodo_destino] < distance[nodo_destino]:
                distance[nodo_destino] = distance[nodo_actual] + matrix[nodo_actual][nodo_destino]
                parent[nodo_destino] = nodo_actual

    return parent, distance

# Llama a la función dijkstra para cada ubicación de inicio
for start_location in range(len(distances)):
    parent, distance = dijkstra(distances, start_location)

    # Imprime la ruta más corta desde la ubicación de inicio
    for i in range(len(parent)):
        if parent[i] != -1:
            print(f"Ruta desde la ubicación {start_location} a {i}:")
            nodo_actual = i
            ruta = []
            while nodo_actual != -1:
                ruta.insert(0, nodo_actual)
                nodo_actual = parent[nodo_actual]
            print(" -> ".join(map(str, ruta)))
            print(f"Distancia total: {distance[i]}")
