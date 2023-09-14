import requests

# Obtener las ubicaciones de los clientes
response = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA")
locations = response.json()["results"][0]["geometry"]["location"]

# Crear una matriz de distancias
distances = []
for i in range(len(locations)):
    for j in range(len(locations)):
        response = requests.get("https://maps.googleapis.com/maps/api/directions/json?origin={},{}&destination={},{}&mode=driving".format(
            locations[i]["lat"], locations[i]["lng"], locations[j]["lat"], locations[j]["lng"]
        ))
        distances.append(response.json()["routes"][0]["legs"][0]["distance"]["value"])

# Resolver el problema de la ruta más corta
routes = []
for i in range(len(locations)):
    routes.append(dijkstra(distances, i))

# Imprimir las rutas
for route in routes:
    print(route)
