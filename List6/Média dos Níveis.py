def getfirstlevel(array):
    global level1
    level1 = array[0]

    print('Media do nivel 1 = {level1:.2f}'.format(level1=level1))


def geterrorlist(array):
    if (len(array) < 0) or (len(array) == 0):
        return


def getotherlevels(length, start, end, level, array, limitbetween):
    if (len(array) < 0) or (len(array) == 0):
        geterrorlist(array)
        return

    elif (len(array) == 1) and (level1 == array[0]):
        getfirstlevel(array)
        return

    else:
        while ((length > limitbetween) and (length > start)) or (array[0] != level1):

            if array[0] != level1:
                return

            else:
                sum, cont = 0, 0

                origin = (2 * start) + 1
                destiny = (2 * end) + 2

                start = origin

                limitbetween = (2 * end) + 2

                end = destiny

                if length <= end:
                    end = length - 1

                else:
                    pass

                for i in range(end, start - 1, -1):
                    if (end != 0) and (start != 0):
                        num = array[i]

                        if num != -1:
                            sum += num
                            cont += 1

                        else:
                            pass
                    
                    else:
                        pass

                m = (sum / cont)

                if length > start:
                    level += 1
                
                else:
                    pass
                    
                print('Media do nivel {level} = {values:.2f}'.format(level=level, values=m))


def main():
    sequence = input()
    sequencewithoutspace = sequence.split()

    array = [int(i) for i in sequencewithoutspace]

    level, start, end, limitbetween = 0, 0, 0, 0
    length = len(array)

    level += 1

    if length > 0:
        getfirstlevel(array)
        getotherlevels(length, start, end, level, array, limitbetween)

    else:
        pass

if __name__ == '__main__':
    main()

    
