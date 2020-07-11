from src.dijkstra_algorithm.dijkstra import Dijkstra
import random


def make_empty_table(height, width, start, end):
    table = []
    for y in range(height):
        line = []
        for x in range(width):
            line.append(f'space-{y}-{x}')
        table.append(line)
    table[start[0]][start[1]] = 'start'
    table[end[0]][end[1]] = 'end'


    return(table)



    