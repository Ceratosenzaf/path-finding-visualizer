from dijkstra.dijkstra import Dijkstra

table = [
    ['1', '3', '5', '7', '23', '43', '54', '65', '76', '87', '84'],
    ['8', '2', '4', '0', '78', '64', '21', '82', '50', '26', '82'],
    ['9', '6', 'end', 'start']
]

dj = Dijkstra(table)
dj.run()