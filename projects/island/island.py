# Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:

# islands = [[0, 1, 0, 1, 0],
#             [1, 1, 0, 1, 1],
#             [0, 0, 1, 0, 0],
#             [1, 0, 1, 0, 0],
#             [1, 1, 0, 0, 0]]

# island_counter(islands) # returns 4

islands =  [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
            [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
            [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
            [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
            [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
            [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
            [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]

# island_counter(islands) # returns 13


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


def island_counter(matrix):
    # create a visited matrix
    visited = []
    for i in range(len(matrix)):
        visited.append([False] * len(matrix[0]))
    
    island_count = 0

    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            # if not visited
            if not visited[y][x]:
                if matrix[y][x] == 1:
                    # Run some DFT and mark each as visited
                    dft(x, y, matrix, visited)

                    island_count += 1

    return island_count


def dft(x, y, matrix, visited):
    s = Stack()
    s.push((x, y))

    while s.size() > 0:
        v = s.pop()
        x = v[0]
        y = v[1]

        if not visited[y][x]:
            # mark as visited
            visited[y][x] = True

            for neighbor in get_neighbors((x, y), matrix):
                s.push(neighbor)

    return visited


def get_neighbors(vertex, graph_matrix):
    x = vertex[0]
    y = vertex[1]

    neighbors = []

    # North
    if y > 0 and graph_matrix[y-1][x] == 1:
        neighbors.append((x, y-1))

    # South
    if y < len(graph_matrix) - 1 and graph_matrix[y+1][x] == 1:
        neighbors.append((x, y + 1))

    # East
    if x < len(graph_matrix[0]) - 1 and graph_matrix[y][x+1] == 1:
        neighbors.append((x+1, y))

    # West
    if x > 0 and graph_matrix[y][x-1] == 1:
        neighbors.append((x-1, y))

    return neighbors





print(island_counter(islands))



######### breakout room group solution

# class Queue():
#     def __init__(self):
#         self.queue = []
    
#     def enqueue(self, value):
#         self.queue.append(value)
    
#     def dequeue(self):
#         if self.size() > 0:
#             return self.queue.pop(0)
#         else:
#             return None
    
#     def size(self):
#         return len(self.queue)

# def island_counter(islands):
#     # visited cache
#     # count of islands
#     visited = set()
#     island_count = 0
#     q = Queue()
#     for y in range(0, len(islands)):
#         for x in range(0, len(islands[y])):
#             if islands[y][x] == 1 and (y,x) not in visited:
#                 island_count += 1
#                 print([y, x])
#                 q.enqueue([y,x])
#                 visited.add((y,x))
#                 while q.size() > 0:
#                     v = q.dequeue()
#                     y_cord = v[0]
#                     x_cord = v[1]
#                     if y_cord > 0:
#                         if (y_cord-1, x_cord) not in visited and islands[y_cord-1][x_cord] == 1:
#                             visited.add((y_cord-1, x_cord))
#                             q.enqueue([y_cord-1, x_cord])
#                     if y_cord < len(islands)-1:
#                         if (y_cord+1, x_cord) not in visited and islands[y_cord+1][x_cord] == 1:
#                             visited.add((y_cord+1, x_cord))
#                             q.enqueue([y_cord+1, x_cord])
#                     if x_cord < len(islands[y_cord])-1:
#                         if (y_cord, x_cord+1) not in visited and islands[y_cord][x_cord+1] == 1:
#                             visited.add((y_cord, x_cord+1))
#                             q.enqueue([y_cord, x_cord+1])
#                     if x_cord > 0:
#                         if (y_cord, x_cord-1) not in visited and islands[y_cord][x_cord-1] == 1:
#                             visited.add((y_cord, x_cord-1))
#                             q.enqueue([y_cord, x_cord-1])
    
#     return island_count

# print(island_counter(islands))