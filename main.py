#from timeit import default_timer as timer

visited_maps_beg = []
visited_maps_end = []

nodes_beg = []
nodes_end = []


class Node:
    def __init__(self, map, parent, direction):
        if parent is None and direction is None:
            self.map = map
            self.depth = 0
            self.parent = None
            self.discovered = 0
            self.direction = None
        else:
            self.map = map
            self.depth = parent.depth + 1
            self.parent = parent
            self.discovered = 0
            self.direction = direction

# Swaps two elements in a list
def swap(c, i, j):
    c = list(c)
    c[i], c[j] = c[j], c[i]
    return ''.join(c)

# Operator up for the map
def op_up(map):
    empty = find_empty(map)
    if empty > 5:
        return None
    else:
        map = swap(map, empty, empty + 3)
        return map

# Operator down for the map
def op_down(map):
    empty = find_empty(map)
    if empty < 3:
        return None
    else:
        map = swap(map, empty, empty - 3)
        return map

# Operator left for the map
def op_left(map):
    empty = find_empty(map)
    if empty == 2 or empty == 5 or empty == 8:
        return None
    else:
        map = swap(map, empty, empty + 1)
        return map

# Operator right for the map
def op_right(map):
    empty = find_empty(map)
    if empty == 0 or empty == 3 or empty == 6:
        return None
    else:
        map = swap(map, empty, empty - 1)
        return map

# Looking for X on a map, returns its index
def find_empty(map):
    for i in range(len(map)):
        if map[i] == "X":
            return i

# Input checker for correct list length
def input_checker():
    temp = input()
    if len(temp) != 9:
        print("Wrong input, try again")
        temp = input_checker()
    return temp

# Printing map function for debugging
def print_map(map):
    print(map[:-6])
    print(map[3:-3])
    print(map[6:])
    print("---")

# Prints sequence of moves to achieve solution
def print_solution(common_map):
    common_node_beg = None
    common_node_end = None

    # Finds node from both ends where BFS searches met
    for i in range(len(nodes_beg)):
        if nodes_beg[i].map == common_map:
            common_node_beg = nodes_beg[i]

    for i in range(len(nodes_end)):
        if nodes_end[i].map == common_map:
            common_node_end = nodes_end[i]


    moves_beg = []
    moves_end = []

    # Writeback direction moves from both ends
    while (common_node_beg.parent != None):
        moves_beg.append(common_node_beg.direction)
        common_node_beg = common_node_beg.parent

    while (common_node_end.parent != None):
        moves_end.append(common_node_end.direction)
        common_node_end = common_node_end.parent

    # Reverse elements in first list
    moves_beg.reverse()

    # Reverese operands in second list
    for i in range(len(moves_end)):
        if moves_end[i] == "Up":
            moves_end[i] = "Down"
            continue
        if moves_end[i] == "Down":
            moves_end[i] = "Up"
            continue
        if moves_end[i] == "Right":
            moves_end[i] = "Left"
            continue
        if moves_end[i] == "Left":
            moves_end[i] = "Right"
            continue

    moves = moves_beg + moves_end

    # Prints moves sequence
    for i in range(len(moves)):
        print(moves[i])

# Seeks for solution between two maps
def solve(beg_map, end_map):

    #start = timer()

    # Beginning and end node init
    beg_node = Node(beg_map, None, None)
    end_node = Node(end_map, None, None)

    # Adding maps of both nodes to visited maps
    visited_maps_beg.append(beg_node.map)
    visited_maps_end.append(end_node.map)

    # Adding both nodes to visited nodes
    nodes_beg.append(beg_node)
    nodes_end.append(end_node)

    depth = 0
    match = 0
    common_map = None

    # Looking for solutions until common map is found
    while (match == 0):

        # Unvisited nodes from beginning
        for i in range(len(nodes_beg)):

            if(nodes_beg[i].depth == depth and nodes_beg[i].discovered == 0):
                beg_up = op_up(nodes_beg[i].map)
                beg_down = op_down(nodes_beg[i].map)
                beg_right = op_right(nodes_beg[i].map)
                beg_left = op_left(nodes_beg[i].map)

                if (beg_up != None) and (beg_up not in visited_maps_beg):
                    node_up = Node(beg_up, nodes_beg[i], "Up")
                    visited_maps_beg.append(beg_up)
                    nodes_beg.append(node_up)

                if (beg_down != None) and (beg_down not in visited_maps_beg):
                    node_down = Node(beg_down, nodes_beg[i], "Down")
                    visited_maps_beg.append(beg_down)
                    nodes_beg.append(node_down)

                if (beg_right != None) and (beg_right not in visited_maps_beg):
                    node_right = Node(beg_right, nodes_beg[i], "Right")
                    visited_maps_beg.append(beg_right)
                    nodes_beg.append(node_right)

                if (beg_left != None) and (beg_left not in visited_maps_beg):
                    node_left = Node(beg_left, nodes_beg[i], "Left")
                    visited_maps_beg.append(beg_left)
                    nodes_beg.append(node_left)

                nodes_beg[i].discovered = 1

        # Unvisited nodes from end
        for i in range(len(nodes_end)):

            if(nodes_end[i].depth == depth and nodes_end[i].discovered == 0):
                end_up = op_up(nodes_end[i].map)
                end_down = op_down(nodes_end[i].map)
                end_right = op_right(nodes_end[i].map)
                end_left = op_left(nodes_end[i].map)

                if (end_up != None) and (end_up not in visited_maps_end):
                    node_up = Node(end_up, nodes_end[i], "Up")
                    visited_maps_end.append(end_up)
                    nodes_end.append(node_up)

                if (end_down != None) and (end_down not in visited_maps_end):
                    node_down = Node(end_down, nodes_end[i], "Down")
                    visited_maps_end.append(end_down)
                    nodes_end.append(node_down)

                if (end_right != None) and (end_right not in visited_maps_end):
                    node_right = Node(end_right, nodes_end[i], "Right")
                    visited_maps_end.append(end_right)
                    nodes_end.append(node_right)

                if (end_left != None) and (end_left not in visited_maps_end):
                    node_left = Node(end_left, nodes_end[i], "Left")
                    visited_maps_end.append(end_left)
                    nodes_end.append(node_left)

                nodes_end[i].discovered = 1

        depth += 1

        # Looking for a match in BFS searches
        for k in range(len(visited_maps_beg)):
            if visited_maps_beg[k] in visited_maps_end:
                match = 1
                common_map = visited_maps_beg[k]
                break

    #end = timer()
    #print("trvanie: ", end - start)
    #print("pocet stavov: ", len(uzle_z)+len(uzle_k))

    print_solution(common_map)


if __name__ == "__main__":
    print("Enter beginning state:")
    beg_map = input_checker()

    print("Enter ending state:")
    end_map = input_checker()
    print("----------------------")
    print("Output:")
    solve(beg_map, end_map)