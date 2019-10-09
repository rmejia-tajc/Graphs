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
            #TODO: do we need error checking here

        
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

    # Make a queue
    qq = Queue()
    # Add first node to stack, as list by adding []
    qq.enqueue([starting_node])
    # Track max path length, initial value is 1
    longest_path_len = 1
    # Track earliest ancestor, initial value is -1 / if starting node has no parent, this will return -1
    earliest_ancestor = -1
    # While queue not empty...
    while qq.size() > 0:
        # Remove first list from queue and assign it to path
        path = qq.dequeue()
        # assign the last value of path to "value"
        value = path[-1]
        # If the path is longer or equal to longest_path_len and the value is smaller than earliest_ancestor (to keep path where lowest numeric ancestor), or if the path is longer than longest_path_len...
        if (len(path) >= longest_path_len and value < earliest_ancestor) or (len(path) > longest_path_len):
            # Then update earliest_ancestor with value
            earliest_ancestor = value
            # Then update longest_path_len with length of path
            longest_path_len = len(path)
        # loop through and get neighbors of value
        for neighbor in tree.vertices[value]:
            # make a copy of path (not a reference)
            new_path = list(path)
            # add neighbors to end of path
            new_path.append(neighbor)
            # add new path to end of queue
            qq.enqueue(new_path)

    print("\nearliest_ancestor")
    print(earliest_ancestor)
    return earliest_ancestor





test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

earliest_ancestor(test_ancestors, 6)