class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id in self.vertices:
            #print("WARNING: That vertex already exists")
            pass
        else:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def get_parents(self, vertex_id):
        return self.vertices[vertex_id]    



def earliest_ancestor(ancestors, starting_vertex):
    graph = Graph()
    for i in ancestors: 
        graph.add_vertex(i[0])
        graph.add_vertex(i[1])
        graph.add_edge(i[1], i[0])
    s = Stack()
    s.push([starting_vertex])
    visited = set()
    results = []
    while s.size() > 0:
        p = s.pop()
        last_vertex = p[-1]
        if len(graph.get_parents(last_vertex)) == 0:
            results.append(p)
        if last_vertex not in visited:
            visited.add(last_vertex)
            for neighbor in graph.get_parents(last_vertex):
                copy = p.copy()
                copy.append(neighbor)
                s.push(copy) 
    print(results)
    if results[-1][-1] == starting_vertex: 
        return -1  
    else:
        max_length = max([len(i) for i in results])
        return min([i[-1] for i in results if len(i) == max_length])