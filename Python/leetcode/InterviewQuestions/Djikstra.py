import heapq
class Graph:

    def __init__(self, n, edges):
        self.number_of_vertices = n
        self.edges = edges
    
    def get_adjacency(self):
        self.graph = {i: [] for i in range(self.number_of_vertices)}
        for edge in self.edges:
            v1, v2, weight = edge
            self.graph[v1].append((v2, weight))
            self.graph[v2].append((v1, weight))

    def get_shortest_distance(self, starting_vertex):
        visited = set()
        distance = [float('inf') for i in range(self.number_of_vertices)]
        distance[starting_vertex] = 0
        heap = [(0, starting_vertex)]

        while heap:
            curr_distance, curr_vertex = heapq.heappop(heap)
            if curr_vertex not in visited:
                visited.add(curr_vertex)

                for ne in self.graph[curr_vertex]:
                    tent_distance = curr_distance + ne[1]
                    if tent_distance < distance[ne[0]]:
                        distance[ne[0]] = tent_distance
                        heapq.heappush(heap, (tent_distance, ne[0]))
        return distance
            
    
graph = Graph(5, [[0,1,9], [1,2,2], [2,3,4], [3,4,7], [1,3,5], [0,4,3]])
graph.get_adjacency()
print(graph.get_shortest_distance(0))

