from dijkstra.dijkstra import Dijkstra


def make_empty_table(height, width):
    table = []
    for y in range(height):
        line = []
        for x in range(width):
            line.append(f'space{y}{x}')
        table.append(line)
    return(table)


table = make_empty_table(10,7)
table[0][0] = 'start'
table[7][5] = 'end'


dj = Dijkstra(table)
dj.run()