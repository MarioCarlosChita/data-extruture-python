class Graph:

    def __init__(self, edges):
        self.graph = {}
        self.edges = edges
        for start, end in edges:
            if start not in self.edges:
                self.graph[start] = [end]
            else:
                self.graph[start].append(end)

    def get_path_from(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [start]

        if start not in self.graph:
            return []
        
        paths = []
        for node in self.graph[start]:
              if node not in path:
                new_node = self.get_path_from(node, end, path)
                for p in new_node:
                   paths.append(p)
        return paths
