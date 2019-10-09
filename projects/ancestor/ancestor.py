# ancestors = dataset
# starting_node(vertex) - child
# no cycles - can only flow in one direction


class Graph:
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):

        # without this check, the sets get overwritten by an empty set if the vertex shows up again!!!

        # if the vertex does not exist in vertices...
        if vertex not in self.vertices:
            # then create an empty set for it
            self.vertices[vertex] = set()

        
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Can not create edge based on given vertices!")


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


def earliest_ancestor(ancestors, starting_node):

    # create a family tree graph
    tree = Graph()
    # loop through ancestors dataset
    for pair in ancestors:
        # add parent
        tree.add_vertex(pair[0])
        # add child
        tree.add_vertex(pair[1])
        # add relationship from child to parent | no cycles - can only go in one direction | important!!!
        tree.add_edge(pair[1], pair[0])

    print("\ntree.vertices")
    print(tree.vertices)





test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

earliest_ancestor(test_ancestors, 1)