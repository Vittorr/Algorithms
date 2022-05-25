class GraphCreation:

    def __init__(self, nodes, edge):
        self.V = nodes
        self.A = edge
        self.graph = []


def relax(p, u, v, w, pred):
    if p[v] > p[u] + w:
        pred[v] = u
        p[v] = p[u] + w


def bellmanford(origin, graph, v):
    pred = [-1] * v
    p = [99999999999999999999] * graph.V
    p[origin] = 0

    for i in range(graph.V - 1):
        for u, v, w in graph.graph:
            relax(p, u, v, w, pred)

    for u, v, w in graph.graph:
        if p[v] > p[u] + w:
            print('Ciclo negativo encontrado!')
            return False

    for i in range(graph.V):
        print('Vertice: {i} Antecessor: {antecessor} Distancia: {dist}'.format(i=i, antecessor=pred[i], dist=p[i]))

    return True


def main():
    time = int(input())

    while time > 0:

        graphinfo = input()
        graph1 = graphinfo.split()
        array1 = [int(i) for i in graph1]

        vert = array1[0]
        edg = array1[1]

        graph = GraphCreation(vert, edg)

        for i in range(edg):
            informations = input()
            info = informations.split()

            array = [int(i) for i in info]

            u = array[0]
            v = array[1]
            w = array[2]

            graph.graph.append([u, v, w])

        search = int(input())

        bellmanford(search, graph, vert)

        time -= 1


if __name__ == '__main__':
    main()



    
