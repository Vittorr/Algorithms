class Graph:

    def __init__(self, gv, arestas):
        self.V = gv
        self.connection = arestas
        self.graph = [[] for i in range(gv)]

    def adj(self, v):
        return self.graph[v]

    def array(self, array1):
        return array1

    def qtdev(self, array1):
        return len(array1)


def bfs(graph, v, listresult, aux, number=1, j=0):

    global queue
    checked = graph.qtdev(aux) * [False]

    if not checked[v]:
        v -= 1
        queue = [v]
        checked[v] = True

        while len(queue) > 0:
            v1 = queue.pop(0)

            for i in graph.adj(v1):

                if checked[i]:
                    pass

                elif not checked[i]:
                    queue.append(i)
                    checked[i] = True
                    number += 1

                else:
                    pass

        getnumber(checked, graph, number, listresult, j)

    else:
        pass


def getnumber(checked, graph, number, listresult, j):
    n = len(checked)
    if j > n:
        pass

    else:
        while n > j:

            if not checked[j]:
                pass

            elif checked[j]:
                listresult[j] = number

            else:
                pass

            j += 1


def main():

    sequence1 = input()
    sequence = sequence1.split()

    array = [int(i) for i in sequence]

    qtdv = array[0]
    
    aux = []
    for i in range(qtdv):
        aux.append(int(i))

    qtde = array[1]

    graph = Graph(qtdv, qtde)

    graph.array(aux)

    cont, var = 0, 0

    while qtde > cont:

        connections1 = input()
        connections2 = connections1.split()

        connections = [int(i) for i in connections2]

        graph.graph[connections[0] - 1].append(connections[1] - 1)
        graph.graph[connections[1] - 1].append(connections[0] - 1)

        cont += 1

    listresult = graph.qtdev(aux) * [None]

    while graph.V > var:
        if listresult[var - 1] is None:
            bfs(graph, var, listresult, aux)

        else:
            pass
            
        var += 1

    print(*listresult, sep=' ')


if __name__ == '__main__':
    main()




    
