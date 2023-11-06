from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.dfs = ""
        self.found = False

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSutil(self, root, search, visited):
        visited.add(root)
        self.dfs = self.dfs + root + " "
        if root == search:
            self.found = True
        for neighbour in self.graph[root]:
            if neighbour not in visited:
                self.DFSutil(neighbour, search, visited)

    def DFS(self, root, search):
        visited = set()
        self.DFSutil(root, search, visited)

g = Graph()
n = int(input("enter the no.of nodes: "))
root = input("enter root node: ")
search = input("enter search element: ")
print("enter the vertices of the tree:")
for i in range(n - 1):
    s = input()
    x = s.split(",")
    g.addEdge(x[0], x[1])
g.DFS(root, search)
if g.found:
    print("The element is found")
    print("Following is the Depth-First Search:")
    print(g.dfs)
else:
    print("Given element not found in tree")
