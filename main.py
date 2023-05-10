import mod1

class Error(Exception):
    pass

def checkInNodes(input):
    if input not in mod1.graph.nodes:
        raise Error()

while True:
    while True:
        start = input('start')
        finish = input('finish')

        try:
            checkInGraph(start)
            checkInGraph(finish)
        except Error:
            print('re-write')
            continue
        else:
            break

    print(mod1.getDijkstra(start)[finish])
    end = input('end? (Y/n)')
    if end == 'Y':
        break