class BinarySearchTree:
    def __init__(self, name, score):
        self.father = None
        self.left = None
        self.right = None
        self.name = name
        self.score = score


def search(root, score):

    while root is not None and score != root.score:
        if score < root.score:
            root = root.left

        elif score > root.score:
            root = root.right

        else:
            pass

    return root


def getmin(root):

    while root.left is not None:
        root = root.left

    return root


def getmax(root):

    while root.right is not None:
        root = root.right

    return root


def suc(root):

    if root.right is not None:
        return getmin(root.right)

    next1 = root.father
    while next1 is not None and root == next1.right:
        root = next1
        next1 = next1.father

    return next1


def pre(root):

    if root.left is not None:
        return getmax(root.left)

    next2 = root.father
    while next2 is not None and root == next2.left:
        root = next2
        next2 = next2.father

    return next2


def insert_tree(tree, name, score):

    element = BinarySearchTree(name, score)

    var = None
    var1 = tree

    while var1 is not None:
        var = var1

        if element.score > var1.score:
            var1 = var1.right

        elif element.score < var1.score:
            var1 = var1.left

        else:
            print('{name} ja esta no sistema.'.format(name=name))
            return tree

    element.father = var

    if var is None:
        tree = element

    elif element.score < var.score:
        var.left = element

    else:
        var.right = element

    print('{name} inserido com sucesso!'.format(name=name))

    return tree


def main():

    number = int(input())
    roottree = None
    while number > 0:

        commands = input()
        command = commands.split()

        if command[0] == 'ADD':
            person = command[1]
            points = int(command[2])

            roottree = insert_tree(roottree, person, points)

        elif command[0] == 'PROX':
            points = int(command[1])

            element = search(roottree, points)

            if suc(element) is None and pre(element) is None:
                print('Apenas {name} existe no sistema...'.format(name=element.name))

            elif suc(element) is None:

                print('{name} e o maior! e logo atras vem {name1}'.format(name=element.name, name1=pre(element).name))

            elif pre(element) is None:

                print('{name} e o menor! e logo apos vem {name1}'.format(name=element.name, name1=suc(element).name))

            else:

                print('{name} vem apos {name1} e antes de {name2}'.format(name=element.name, name1=pre(element).name, name2=suc(element).name))

        else:
            pass

        number -= 1


if __name__ == '__main__':
    main()

    
