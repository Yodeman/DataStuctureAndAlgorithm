def dfs(graph, start_vertex=None, end_vertex=None):
    visited = set()
    if graph:
        if not start_vertex:
            start_vertex = list(graph.kes())[0]

    s = []
    s.append(start_vertex)
    while len(s) > 0 and end_vertex not in visited:
        vertex = s.pop()
        if vertex not in visited:
            visited.add(vertex)
            for adjacent_vertex in graph[vertex]:
                if adjacent_vertex not in visited:
                    s.append(adjacent_vertex)
    return visited

def dfs2(graph, start_vertex=None, end_vertex=None):
    visited = set()
    def dfs3(start_vertex, end_vertex):
        visited.add(start_vertex)
        for adjacent_vertex in graph[start_vertex]:
            if adjacent_vertex not in visited and end_vertex not in visited:
                dfs3(adjacent_vertex, end_vertex)
    if graph:
        if not start_vertex:
            start_vertex = list(graph.keys())[0]
        dfs3(start_vertex, end_vertex)

    return visited