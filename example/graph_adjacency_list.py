def add_vertex(v):
    global graph
    global vertices_no
    if v in graph:
        print("vertex ", v, " already exists.")
    else:
        vertices_no = vertices_no + 1
        graph[v] = []
        
def add_edge(v1, v2, e):
    global graph
    if v1 not in graph:
        print("vertex ", v1, " already exists.")
    elif v2 not in graph:
        print("vertex ", v2, " already exists.")
    else:
        temp = [v2, e]
        graph[v1].append(temp)
        
def print_graph():
    global graph
    for vertex in graph:
        for edges in graph[vertex]:
            print(vertex, " -> ", edges[0], "  edge weight: ", edges[1])

# driver code
if __name__ == "__main__":
    graph = {}
    vertices_no = 0
    # stores the number of vertics in the graph
    add_vertex(1)
    add_vertex(2)
    add_vertex(3)
    add_vertex(4)
    # add the edges beween the vertics by specifying
    # the from and to vertex along with the edge weights.
    add_edge(1, 2, 1)
    add_edge(1, 3, 1)
    add_edge(2, 3, 3)
    add_edge(3, 4, 4)
    add_edge(4, 1, 5)
    print_graph()
    # reminder : the second element of each list inside the dictionary
    # denotes the edge weight.
    print("Internal representation: ", graph)