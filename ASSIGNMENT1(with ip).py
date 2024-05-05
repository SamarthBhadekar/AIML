def create_graph():
    graph = {}
    num_nodes = int(input("Enter the number of nodes in the graph: "))

    for _ in range(num_nodes):
        node = input("Enter a node: ")
        neighbors = input("Enter neighbors for the node (comma-separated): ").split(',')
        graph[node] = neighbors

    return graph

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)

        # Check if the current node has neighbors before accessing them
        if graph.get(node):
            for neighbour in graph[node]:
                dfs(visited, graph, neighbour)

# Driver Code
print("Please create a graph:")
user_graph = create_graph()
start_node = input("Enter the starting node for DFS: ")

visited = set()  # Set to keep track of visited nodes of graph.

print("Following is the Depth-First Search:")
dfs(visited, user_graph, start_node)
