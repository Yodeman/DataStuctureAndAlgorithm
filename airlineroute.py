from queue import Queue
#import pprint

def bfs(graph, start_vertex, end_vertex):
    predecessor = {}
    q = Queue()
    q.put(start_vertex)
    while not q.empty() and end_vertex not in predecessor:
        vertex = q.get()
        for adjacent_vertex in graph[vertex]:
            if adjacent_vertex not in predecessor:
                q.put(adjacent_vertex)
                predecessor[adjacent_vertex] = vertex
        #pprint.pprint(predecessor)
    return predecessor

def find_path(graph, start_vertex, end_vertex):
    predecessor = bfs(graph, start_vertex, end_vertex)
    #print('-'*50)
    #pprint.pprint(predecessor)
    path = []
    if end_vertex in predecessor:
        path = [end_vertex]
        vertex = end_vertex
        while vertex != start_vertex:
            vertex = predecessor[vertex]
            path = [vertex] + path
    return path

def main():
    routes = {
        "ATL":{"MIA", "DCA", "ORD", "MCI", "DFW", "DEN"},
        "MIA":{"LGA", "DCA", "ATL", "DFW"},
        "DFW":{"LAX", "DEN", "MCI", "ORD", "ATL", "MIA"},
        "LAX":{"SFO", "DEN", "MCI", "DFW"},
        "DEN":{"SFO", "LAX", "MCI", "DFW", "SEA", "ATL"},
        "SEA":{"SFO", "DEN", "ORD", "LGA"},
        "MCI":{"DEN", "LAX", "DFW", "ATL", "ORD", "LGA"},
        "ORD":{"SEA", "MCI", "DFW", "ATL", "DCA", "LGA"},
        "DCA":{"ORD", "ATL", "MIA", "LGA"},
        "LGA":{"SEA", "MCI", "ORD", "DCA", "MIA"},
        "SFO":{"SEA", "DEN", "LAX"},
        "CLT":{"BNA", "CHA"},
        "BNA":{"CLT", "CHA"},
        "CHA":{"CLT", "BNA"}
    }

    print(find_path(routes, "LAX", "DCA"))
    print(find_path(routes, "MIA", "SFO"))
    print(find_path(routes, "ATL", "MIA"))
    print(find_path(routes, "LGA", "LGA"))
    print(find_path(routes, "CLT", "BNA"))
    print(find_path(routes, "BNA", "ATL"))

if __name__ == "__main__":
    main()