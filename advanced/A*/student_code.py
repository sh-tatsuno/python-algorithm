import math

def calc_distance_guess(i, j, intersections):
    square = (intersections[i][0] - intersections[j][0])**2 + (intersections[i][1] - intersections[j][1])**2
    return round(math.sqrt(square),3)

def calc_matrix_guess(intersections):
    matrix = [[0 for x in range(len(intersections))] for x in range(len(intersections))]
    for r in range(len(intersections)):
        for c in range(len(intersections)):
            matrix[r][c] = calc_distance_guess(r, c, intersections)
    return matrix

def add_next_routes(route, roads, goal):
    nodes = roads[route[-1]] #next step from last route
    ret = []
    goal_path = None
    for node in nodes:
        if not node in route:
            ret.append(route + [node])
        if node == goal:
            goal_path = route + [node]
    return ret, goal_path

def calc_next_routes(routes, matrix_guess):
    paths = []
    for i in range(len(routes)):
        route = routes[i]
        length = 0
        for j in range(len(route)-1):
            length += matrix_guess[route[j]][route[j+1]]
        paths.append(length)
        
    min_routes_length=math.inf
    min_routes_index=-1
    for i in range(len(paths)):
        if paths[i] < min_routes_length:
            min_routes_length = paths[i]
            min_routes_index = i
    min_route = routes.pop(min_routes_index)
    return routes, min_route

def next_step(routes, matrix_guess, goal, roads):
    routes, min_route = calc_next_routes(routes, matrix_guess) 
    nexts, goal_path = add_next_routes(min_route, roads, goal) 
    routes += nexts
    return routes, goal_path

def shortest_path(M,start,goal):
    print("shortest path called")
    routes = [[start]] 
    if start == goal:
        return [start]
    matrix_guess = calc_matrix_guess(M.intersections)
    while(1):
        routes, goal_path = next_step(routes, matrix_guess, goal, M.roads)
        if goal_path !=None: break
    return goal_path