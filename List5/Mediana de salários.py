def merge(array, left, middle, right):
    i = left
    j = middle + 1

    for k in range(left, right+1):
        array1[k] = array[k]

    for k in range(left, right+1):
        if i > middle:
            array[k] = array1[j]
            j += 1

        elif j > right:
            array[k] = array1[i]
            i += 1

        elif array1[i] > array1[j]:
            array[k] = array1[j]
            j += 1

        else:
            array[k] = array1[i]
            i += 1


def td_mergesort(salarios_together, salarios_n, left, right):
    if left >= right:
        return

    length = len(salarios_n) - 1
    middle = length
    merge(salarios_together, left, middle, right)


def mergesort(salarios_together, n, intsalarios_n):
    array1 = list(salarios_together)
    global array1

    td_mergesort(salarios_together, intsalarios_n, 0, n - 1)

    del array1


def main():

    salarios_m = input()
    salarios_n = input()
    salarios_m1 = salarios_m.split()
    salarios_n1 = salarios_n.split()

    intsalarios_m = [int(i) for i in salarios_m1]
    intsalarios_n = [int(i) for i in salarios_n1]

    salarios_together = intsalarios_n + intsalarios_m
    n = len(salarios_together)

    mergesort(salarios_together, n, intsalarios_n)

    if n % 2 == 0:
        pos = n // 2
        mediana = (salarios_together[pos-1] + salarios_together[pos]) / 2
        print('{mediana:.2f}'.format(mediana=mediana))

    elif n % 2 != 0:
        pos = n // 2
        print('{salarios_together:.2f}'.format(salarios_together=salarios_together[pos]))

    else:
        pass


if __name__ == '__main__':
    main()

    
