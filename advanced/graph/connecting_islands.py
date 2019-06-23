# Solution

# The following Solution makes use of one of Python's PriorityQueue implementation (heapq)
# For more details - https://thomas-cokelaer.info/tutorials/python/module_heapq.html
import heapq
def create_graph(num_islands, bridge_config):
    """
    Helper function to create graph using adjacency list implementation
    """
    adjacency_list = [list() for _ in range(num_islands + 1)]
    
    for config in bridge_config:
        source = config[0]
        destination = config[1]
        cost = config[2]
        adjacency_list[source].append((destination, cost))
        adjacency_list[destination].append((source, cost))

    return adjacency_list

def minimum_cost(graph):
    """
    Helper function to find minimum cost of connecting all islands
    """
    
    # start with vertex 1 (any vertex can be chosen)
    start_vertex = 1
    
    # initialize a list to keep track of vertices that are visited
    visited = [False for _ in range(len(graph) + 1)]
    
    # initialize starting list - (edge_cost, neighbor)
    heap = [(0, start_vertex)]
    total_cost = 0

    while len(heap) > 0:
        cost, current_vertex = heapq.heappop(heap)
        
        # check if current_vertex is already visited
        if visited[current_vertex]:
            continue

        # else add cost to total-cost
        total_cost += cost

        for neighbor, edge_cost in graph[current_vertex]:
            heapq.heappush(heap, (edge_cost, neighbor))

        # mark current vertex as visited
        visited[current_vertex] = True

    return total_cost

def get_minimum_cost_of_connecting(num_islands, bridge_config):
    graph = create_graph(num_islands, bridge_config)
    return minimum_cost(graph)

def test_function(test_case):
    num_islands = test_case[0]
    bridge_config = test_case[1]
    solution = test_case[2]
    output = get_minimum_cost_of_connecting(num_islands, bridge_config)
    print(output)
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")

num_islands = 4
bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
solution = 6

test_case = [num_islands, bridge_config, solution]
test_function(test_case)

num_islands = 5
bridge_config = [[1, 2, 5], [1, 3, 8], [2, 3, 9]]
solution = 13

test_case = [num_islands, bridge_config, solution]
test_function(test_case)

num_islands = 5
bridge_config = [[1, 2, 3], [1, 5, 9], [2, 3, 10], [4, 3, 9]]
solution = 31
​
test_case = [num_islands, bridge_config, solution]
test_function(test_case)
