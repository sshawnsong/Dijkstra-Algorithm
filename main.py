import mod1

class Error(Exception):
    pass

def checkInGraph(input):
    if input not in mod1.graph.nodes:
        raise Error()
    else:
        pass

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