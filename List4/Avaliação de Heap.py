def maxheap(array):
    if len(array) <= 1:
        return True

    for i in range(1, len(array) // 2):
        if array[i] < array[2*i]:
            return False

        elif array[i] < array[2*i+1]:
            return False

    return True


def minheap(array):
    if len(array) <= 1:
        return True

    for i in range(1, len(array) // 2):
        if array[i] > array[2*i]:
            return False

        elif array[i] > array[2*i+1]:
            return False

    return True


def main():

    listquestion = input()
    listquestionsplit = listquestion.split()
    index0 = [None]

    for i in listquestionsplit:
        index0.append(int(i))

    max_heap = maxheap(index0)
    min_heap = minheap(index0)

    if max_heap is True and min_heap is True:
        print('E uma Heap de maximo e minimo!')

    elif min_heap is True:
        print('E uma Heap de minimo!')

    elif max_heap is True:
        print('E uma Heap de maximo!')

    elif max_heap is False and min_heap is False:
        print('Nao e uma Heap!')

    else:
        print('Nao e nada.')


if __name__ == '__main__':
    main()

