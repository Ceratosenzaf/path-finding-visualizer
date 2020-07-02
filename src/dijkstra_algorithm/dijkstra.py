import sys
from src.utils.default_structure import Default


class Dijkstra(Default):
    """[summary]

    Args:
        Default ([type]): [description]
    """


    def __init__(self, table):
        self.non_visited_nodes = []
        self.lowest_distance = {}
        self.previous_node = {}

        super().__init__(table) 
        

    def run(self):
        # set up variables
        for line in self.table:
            for node in line:
                self.non_visited_nodes.append(node)
                self.lowest_distance[node] = sys.maxsize
                self.previous_node[node] = None
        self.lowest_distance[self.table[self.start[0]][self.start[1]]] = 0

        # run algorithm
        while self.non_visited_nodes:  
            print('***************************************************************')
            minimum = self.get_minimum_distance_node()
            minimum_coords = self.get_coordinates(minimum)
            minimum_distance = self.lowest_distance[minimum]

            res = self.check_nodes(minimum, minimum_distance, minimum_coords)
            if res:
                print(f'SUCCESS: found {self.table[res[0]][res[1]]}\nunseen nodes {self.non_visited_nodes}\ndistances {self.lowest_distance}\nprevious nodes {self.previous_node}')
                print(f'\nSHORTEST PATH: {self.get_path(res)}')
                break

            if minimum_coords == self.goal:
                print(f'SUCCESS: found {minimum}\nunseen nodes {self.non_visited_nodes}\ndistances {self.lowest_distance}\nprevious nodes {self.previous_node}')
                print(f'\nSHORTEST PATH: {self.get_path(minimum_coords)}')
                break

            self.non_visited_nodes.remove(minimum)

            print(f'currently on {minimum}\nunseen nodes {self.non_visited_nodes}\ndistances {self.lowest_distance}\nprevious nodes {self.previous_node}')
        

    def get_minimum_distance_node(self):
        l = [k for k in self.lowest_distance.keys() if k in self.non_visited_nodes]
        li = [self.lowest_distance[k] for k in l]

        minimum_index = li.index(min(li))
        minimum = l[minimum_index]

        return minimum


    def check_nodes(self, num, min_dist, min_coords):    
        try:   
            x = min_coords[0]
            y = min_coords[1]-1
            if self.table[x][y] and x >= 0 and y >= 0:
                self.check_node(num, min_dist, (x,y))
            if (x, y) == self.goal:
                return (x,y)
        except:
            pass

        try:
            x = min_coords[0]
            y = min_coords[1]+1
            if self.table[x][y] and x >= 0 and y >= 0:
                self.check_node(num, min_dist, (x,y))
            if (x, y) == self.goal:
                return (x,y)
        except:
            pass

        try:    
            x = min_coords[0]+1
            y = min_coords[1]
            if self.table[x][y] and x >= 0 and y >= 0:
                self.check_node(num, min_dist, (x,y))
            if (x, y) == self.goal:
                return (x,y)
        except:
            pass

        try:
            x = min_coords[0]-1
            y = min_coords[1]
            if self.table[x][y] and x >= 0 and y >= 0:
                self.check_node(num, min_dist, (x,y))
            if (x, y) == self.goal:
                return (x,y)
        except:
            pass

        return None


    def check_node(self, num, min_dist, coords):
        node = self.table[coords[0]][coords[1]]
        if min_dist + 1 < self.lowest_distance[node]:
            self.lowest_distance[node] = min_dist + 1
            self.previous_node[node] = num


    def get_path(self, coords):
        num = self.table[coords[0]][coords[1]]
        path = []
        while num != self.table[self.start[0]][self.start[1]]:
            path.append(num)
            num = self.previous_node[num]
        path.append(num)

        return(path)