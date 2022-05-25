def empty(length):
    noelement = 0

    if length == 0:
        noelement = 0

    else:
        pass

    answer = noelement

    print('{totalprice} reais podem ser roubados hoje!'.format(totalprice=answer))


def onlyone(cost, length):
    first = cost[0]

    if length == 1:
        first = cost[0]

    else:
        pass

    answer = first

    print('{totalprice} reais podem ser roubados hoje!'.format(totalprice=answer))


def onlytwo(cost, length):
    two = -99999999999999999999999999999

    if length == 2:
        two = max(cost[0], cost[1])

        if two < cost[1]:
            two = cost[1]

        elif two < cost[0]:
            two = cost[0]

        else:
            pass

    else:
        pass

    answer = two

    print('{totalprice} reais podem ser roubados hoje!'.format(totalprice=answer))


def main():
    houses = int(input())

    price = input()
    price1 = price.split()
    array = [int(i) for i in price1]

    if houses == 0:
        empty(houses)

    elif houses == 1:
        onlyone(array, houses)

    elif houses == 2:
        onlytwo(array, houses)

    elif houses > 2:
        maximum = -99999999999999999999999999999

        var1 = array[0]
        var2 = max(array[0], array[1])

        if var2 < array[1]:
            var2 = array[1]

        elif var2 < array[0]:
            var2 = array[0]

        else:
            pass

        for i in range(houses - 1, 1, -1):

            maximum = max(array[i] + var1, var2)

            if maximum < var2:
                maximum = var2

            elif maximum < array[i] + var1:
                maximum = array[i] + var1

            else:
                pass

            var2, var1 = maximum, var2

        answer = maximum

        maximum1 = -999999999999999999999999999999
        var11 = array[0]
        var22 = max(array[0], array[1])

        if var22 < array[1]:
            var22 = array[1]

        elif var22 < array[0]:
            var22 = array[0]

        else:
            pass

        for i in range(2, houses):

            maximum1 = max(array[i] + var11, var22)

            if maximum1 < var22:
                maximum1 = var22

            elif maximum1 < array[i] + var11:
                maximum1 = array[i] + var11

            else:
                pass

            var22, var11 = maximum1, var22

        answer1 = maximum1

        if answer != answer1:
            print('{totalprice} reais podem ser roubados hoje!'.format(totalprice=answer1))

        elif answer == answer1:
            print('{totalprice} reais podem ser roubados hoje!'.format(totalprice=answer))

        else:
            pass

    else:
        pass


if __name__ == '__main__':
    main()

# 5
# 4 5 7 8 1

# 8
# 49 14 21 15 32 32 39 7

