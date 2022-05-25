equal = []
notequal = []


def binary_search(orderedlist, nonorderedlist):
    begin = 0
    end = len(orderedlist) - 1

    for value in nonorderedlist:
        begin = 0
        end = len(orderedlist) - 1
        found = False

        while begin <= end and found is False:
            m = (begin + end) // 2

            if value == orderedlist[m]:
                equal.append(value)
                found = True

            elif value > orderedlist[m]:
                begin = m + 1

            elif value < orderedlist[m]:
                end = m - 1

            else:
                pass

        if not found:
            notequal.append(value)

    return equal, notequal


def main():

    orderlist = input()
    nonorderlist = input()
    orderlist1 = orderlist.split()
    nonorderlist1 = nonorderlist.split()

    intorderlist = [int(i) for i in orderlist1]
    intnonorderlist = [int(j) for j in nonorderlist1]

    answerequal, answernotequal = binary_search(intorderlist, intnonorderlist)
    print(*answerequal, sep=' ')
    print(*answernotequal, sep=' ')


if __name__ == '__main__':
    main()

    
