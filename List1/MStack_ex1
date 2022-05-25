class NewStack:

    def __init__(self, data):
        self.data = data
        self.size = 0
        self.next = None
        self.previous = None


def isempty(nodetop):
    if nodetop is None:
        return True

    elif nodetop is not None:
        return False

    else:
        pass


def push(nodetop, data):
    node = NewStack(data)
    if nodetop is None:
        nodetop = node

    elif nodetop is not None:
        node.previous = nodetop
        node.next = None
        nodetop = node

    else:
        pass

    return nodetop


def maximum(nodetop):
    valuehigh = -99999999999999999999
    while nodetop is not None:
        if nodetop.data > valuehigh:
            valuehigh = nodetop.data

        elif valuehigh == -99999999999999999999:
            print('stack must be redone. maximum number reached.')

        else:
            pass
        nodetop = nodetop.previous

    return valuehigh


def minimum(nodetop):
    valuelow = 99999999999999999999
    while nodetop is not None:
        if nodetop.data < valuelow:
            valuelow = nodetop.data

        elif valuelow == 99999999999999999999:
            print('stack must be redone. minimum number reached.')

        else:
            pass
        nodetop = nodetop.previous

    return valuelow


def pop(nodetop):
    if nodetop.previous is not None:
        nodetop = nodetop.previous
        nodetop.next = None

    elif nodetop.previous is None:
        nodetop = None

    else:
        pass

    return nodetop


def __len__(nodetop):
    if nodetop is None:
        nodetop.size = 0
        return False

    elif nodetop is not None:
        nodetop.size += 1
        return True

    else:
        pass

    return nodetop


def main():
    nodetop = None
    number = int(input())
    count = 0

    while count < number:
        commands = str(input())
        commands = commands.split()

        if commands[0] == 'push':
            value = int(commands[-1])
            nodetop = push(nodetop, value)

        if commands[0] == 'getMax':
            if not isempty(nodetop):
                print(maximum(nodetop))

            elif isempty(nodetop):
                print('empty stack')

            else:
                pass

        if commands[0] == 'getMin':
            if not isempty(nodetop):
                print(minimum(nodetop))

            elif isempty(nodetop):
                print('empty stack')

            else:
                pass

        if commands[0] == 'pop':
            if not isempty(nodetop):
                print(nodetop.data)
                nodetop = pop(nodetop)

            elif isempty(nodetop):
                print('empty stack')

            else:
                pass

        else:
            pass

        count += 1


if __name__ == '__main__':
    main()
