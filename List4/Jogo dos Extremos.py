def change(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def maxheapify(array, i):
    left1 = 2 * i
    right1 = (2 * i) + 1

    if left1 < len(array) and array[left1] > array[i]:
        maior = left1

    else:
        maior = i

    if right1 < len(array) and array[right1] > array[maior]:
        maior = right1

    if maior != i:
        change(array, i, maior)

        maxheapify(array, maior)


def buildmaxheap(array):
    n = len(array)
    for i in range((n//2), 0, -1):
        maxheapify(array, i)


def getmaxheap(array):
    if len(array) <= 0:
        return None

    else:
        return array[1]


def getminheap(array):
    minimum_parameter_leafs = array[len(array)//2]

    for i in range((len(array)//2 + 1), len(array)):
        minimum_parameter_leafs = min(minimum_parameter_leafs, array[i])

    return minimum_parameter_leafs


def removemaxheap(array):
    length = len(array)

    last = array[-1]
    array[1] = last

    length = length - 1

    maxheapify(array, 1)


def main():

    sequence = input()
    constant = int(input())

    sequence1 = sequence.split()

    index0 = [None]
    for i in sequence1:
        index0.append(int(i))

    cont = 0
    length = len(index0)
    buildmaxheap(index0)
    maximumvalue_heap = getmaxheap(index0)
    minimumvalue_heap = getminheap(index0)

    while len(index0) > 1:
        maximumvalue_heap = getmaxheap(index0)
        minimumvalue_heap = getminheap(index0)

        value = maximumvalue_heap - abs(minimumvalue_heap * constant)

        if value < 1:
            index0[0] = None
            removemaxheap(index0)
            index0 = index0[:-1]
            cont += 1

        elif value > 0:
            index0[1] = None
            index0[1] = value
            cont += 1

        else:
            pass

        maxheapify(index0, 1)

    print('{cont} rodadas!'.format(cont=cont))


if __name__ == '__main__':
    main()


    
