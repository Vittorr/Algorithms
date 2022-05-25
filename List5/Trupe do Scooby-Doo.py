def particao(array, array1, left, right):

    pivot = array1[left]
    i = left
    j = right + 1

    while True:
        i += 1
        j -= 1

        while array[i] < pivot:
            if i >= right:
                break
            i += 1

        while array[j] > pivot:
            if j <= left:
                break
            j -= 1

        if i >= j:
            break

        array[i], array[j] = array[j], array[i]

    array[left], array[j] = array[j], array[left]

    return j


def qs(array, array1, left, right):
    if left >= right:
        return

    position = particao(array, array1, left, right)
    qs(array, array1, left, position - 1)
    qs(array, array1, position + 1, right)


def quicksort(array, array1, n):
    qs(array, array1, 0, n - 1)


def main():
    number = int(input())
    while number > 0:

        key = input()
        chest = input()
        key1 = key.split()
        n1 = len(key1)
        chest1 = chest.split()
        n2 = len(chest1)

        key2 = [str(i) for i in key1]
        chest2 = [str(i) for i in chest1]

        if key2 != chest2:

            while key2 != chest2:
                quicksort(key2, chest2, n1)

                quicksort(chest2, key2, n2)

        quicksort(chest2, key2, n2)

        quicksort(key2, chest2, n1)

        print(*key2, sep=' ')
        print(*chest2, sep=' ')

        number -= 1


if __name__ == '__main__':
    main()



    
