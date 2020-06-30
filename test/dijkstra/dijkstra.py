import sys
from heapq import nsmallest

table = [
    [1, 3, 5, 7, 23, 43, 54, 65, 76, 87, 84],
    [8, 2, 4, 0, 78, 64, 21, 82, 50, 26, 82],
    [9, 6, 10, 11, 54554, 57647, 656, 65, 65],
    [424, 4543, 434, 43543, 23423465]
]

non_visited_nodes = []
lowest_distance = {}
previous_node = {}
start = (0,0)
goal = (3,4)
win = False


def get_minimum_distance_node(low_dist, unseen):
    l = [k for k in low_dist.keys() if k in unseen]
    li = [low_dist[k] for k in l]

    minimum_index = li.index(min(li))
    minimum = l[minimum_index]

    return minimum

def get_coordinates(tab,min):
    for i, line in enumerate(tab):
        try:
            return (i, line.index(min))
        except:
            pass


def check_nodes(tab, num, min_dist, min_coords):    
    try:   
        x = min_coords[0]
        y = min_coords[1]-1
        if tab[x][y] and x >= 0 and y >= 0:
            check_node(tab, num, min_dist, (x,y))
        if (x, y) == goal:
            return (x,y)
    except:
        pass

    try:
        x = min_coords[0]
        y = min_coords[1]+1
        if tab[x][y] and x >= 0 and y >= 0:
            check_node(tab, num, min_dist, (x,y))
        if (x, y) == goal:
            return (x,y)
    except:
        pass

    try:    
        x = min_coords[0]+1
        y = min_coords[1]
        if tab[x][y] and x >= 0 and y >= 0:
            check_node(tab, num, min_dist, (x,y))
        if (x, y) == goal:
            return (x,y)
    except:
        pass

    try:
        x = min_coords[0]-1
        y = min_coords[1]
        if tab[x][y] and x >= 0 and y >= 0:
            check_node(tab, num, min_dist, (x,y))
        if (x, y) == goal:
            return (x,y)
    except:
        pass

    return None


def check_node(tab, num, min_dist, coords):
    node = tab[coords[0]][coords[1]]
    if min_dist + 1 < lowest_distance[node]:
        lowest_distance[node] = min_dist + 1
        previous_node[node] = num


def get_path(tab, prev_node, coords, start):
    num = tab[coords[0]][coords[1]]
    path = []
    while num != tab[start[0]][start[1]]:
        path.append(num)
        num = prev_node[num]
    
    path.append(num)
    print(f'SHORTEST PATH: {path}')


if __name__ == "__main__":
    for line in table:
        for node in line:
            non_visited_nodes.append(node)
            lowest_distance[node] = sys.maxsize
            previous_node[node] = None

    lowest_distance[table[start[0]][start[1]]] = 0

    while non_visited_nodes:  
        print('***************************************************************')
        minimum = get_minimum_distance_node(lowest_distance, non_visited_nodes)
        minimum_coords = get_coordinates(table, minimum)
        minimum_distance = lowest_distance[minimum]

        res = check_nodes(table, minimum, minimum_distance, minimum_coords)
        if res:
            print(f'SUCCESS: found {table[res[0]][res[1]]}\nunseen nodes {non_visited_nodes}\ndistances {lowest_distance}\nprevious nodes {previous_node}')
            get_path(table, previous_node, res, start)
            break

        if minimum_coords == goal:
            print(f'SUCCESS: found {minimum}\nunseen nodes {non_visited_nodes}\ndistances {lowest_distance}\nprevious nodes {previous_node}')
            get_path(table, previous_node, minimum_coords, start)
            break

        non_visited_nodes.remove(minimum)

        print(f'currently on {minimum}\nunseen nodes {non_visited_nodes}\ndistances {lowest_distance}\nprevious nodes {previous_node}')
        