class Graph:
    def __init__(self, nodes, edge):
        self.V = nodes
        self.A = edge
        self.graph = []


def merge(array, left, middle, right):
    i = left
    j = middle + 1

    for k in range(left, right+1):
        aux[k] = array[k]

    for k in range(left, right+1):
        if i > middle:
            array[k] = aux[j]
            j += 1

        elif j > right:
            array[k] = aux[i]
            i += 1

        elif aux[i][2] > aux[j][2]:
            array[k] = aux[j]
            j += 1

        else:
            array[k] = aux[i]
            i += 1


def components(pred, list, comp1, comp2):

    component1, component2 = getelement(pred, comp1), getelement(pred, comp2)

    if list[component1] == list[component2]:
        pred[component2] = component1
        list[component1] += 1

    elif list[component1] > list[component2]:
        pred[component2] = component1

    elif list[component1] < list[component2]:
        pred[component1] = component2

    else:
        pass


def td_mergesort(array, left, right):
    if left >= right:
        return

    middle = (left + right) // 2
    td_mergesort(array, left, middle)
    td_mergesort(array, middle+1, right)
    merge(array, left, middle, right)


def getelement(pred, v):
    if pred[v] != v:
        return getelement(pred, pred[v])

    elif pred[v] == v:
        return v

    else:
        pass


def mergesort(array, n):
    global aux
    aux = list(array)
    td_mergesort(array, 0, n-1)
    del aux


def kruskal(graph):
    totalweight, pred, list = [], [], []

    n = len(graph.graph)
    mergesort(graph.graph, n)

    for j in range(graph.V):
        list.append(9999999999999)
        pred.append(j)

    index, edge = 0, 0
    while (graph.V - 1) > edge:

        [u, v, w] = graph.graph[index]
        index += 1
        compl, compr = getelement(pred, u), getelement(pred, v)

        if compl == compr:
            pass

        elif [u, v, w] == [v, u, w]:
            pass

        elif compl != compr:
            edge += 1
            totalweight.append([u, v, w])
            components(pred, list, compl, compr)

        else:
            pass

    totalcost = 0
    for cost in totalweight:
        totalcost += cost[2]

    return totalcost


def main():
    graphinfo = input()
    graph1 = graphinfo.split()

    array = [int(i) for i in graph1]

    vert = array[0]
    edg = array[1]

    graph = Graph(vert, edg)

    for i in range(edg):
        informations = input()
        info = informations.split()

        array1 = [int(i) for i in info]

        u = array1[0]
        v = array1[1]
        w = array1[2]

        graph.graph.append([u, v, w])

    cost = kruskal(graph)

    print(cost)


if __name__ == '__main__':
    main()



    
