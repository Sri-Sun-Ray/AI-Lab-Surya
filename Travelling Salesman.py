import itertools

def tsp_bruteforce(graph, start):
    # Total number of cities
    n = len(graph)
    
    # All cities except the starting city
    cities = list(range(n))
    cities.remove(start)

    paths = []

    # Generate all possible routes from the starting city
    for perm in itertools.permutations(cities):
        current_distance = 0
        k = start
        for j in perm:
            current_distance += graph[k].get(j, float('inf'))
            k = j
        current_distance += graph[k].get(start, float('inf'))  # return to start

        paths.append(([start] + list(perm), current_distance))

    # Sort paths by distance
    paths.sort(key=lambda x: x[1])

    return paths

if __name__ == '__main__':
    n = int(input("Enter the number of cities: "))
    graph = [{} for _ in range(n)]

    for i in range(n):
        adjacent_cities = input(f"Enter the adjacent cities and weights for city {i} (format: city,weight): ").split()
        for j in range(0, len(adjacent_cities), 2):
            city, weight = int(adjacent_cities[j]), int(adjacent_cities[j+1])
            graph[i][city] = weight

    start_city = int(input("Enter the starting city: "))
    paths = tsp_bruteforce(graph, start_city)
    print("All paths in increasing order of distance:")
    for path, distance in paths:
        print(f"Path: {path}, Distance: {distance}")
    dis=paths[0][1]
    for path,distance in paths:
        if distance==dis:
            print(f"\nOptimized Path from city {start_city}: {path}")
            print(f"Shortest Distance: {distance}")
