
# creta dynamic seat


def createDynamicSeats(arr, seatList):
    i = 0
    while i < len(arr)-1:
        seatList.append([[None]*(arr[i]) for j in range(arr[i+1])])
        i += 2

# fill aisle seat first


def fillAisleSeat(seatList, totalSeat, max_elem):
    aisle = 1
    for i in range(max_elem):
        first = 0
        for list3d in seatList:
            for list2d in list3d:

                if first == len(seatList)-1 and len(list3d) > i:
                    list3d[i][0] = aisle
                    aisle += 1

                elif len(list2d) >= 3 and first != 0 and len(list3d) > i:
                    list3d[i][0] = aisle
                    aisle += 1
                    list3d[i][len(list2d)-1] = aisle
                    aisle += 1

                elif len(list2d) >= 2 and first == 0 and len(list3d) > i:
                    list3d[i][len(list2d)-1] = aisle
                    aisle += 1

                elif len(list2d) == 2 and first != 0 and len(list3d) > i:
                    list3d[i][0] = aisle
                    aisle += 1
                    list3d[i][1] = aisle
                    aisle += 1

                if aisle > totalSeat:
                    break

                break
            first += 1
    return aisle

# fill window seat after aisle seat filling


def fillWindowSeat(seatList, window, totalSeat, max_elem):
    for i in range(max_elem):
        first = 0
        for list3d in seatList:
            for list2d in list3d:

                if first == 0 and len(list3d) > i:
                    list3d[i][0] = window
                    window += 1

                elif first == len(seatList)-1 and len(list3d) > i:
                    list3d[i][len(list2d)-1] = window
                    window += 1

                if window > totalSeat:
                    break

                break
            first += 1
    return window

# fill middle seat at the end after window seat allocation


def fillMiddleSeat(seatList, middle, totalSeat, max_elem):
    for i in range(max_elem):
        first = 0
        for list3d in seatList:
            for list2d in list3d:

                if len(list2d) >= 3 and len(list3d) > i:
                    for index in range(1, len(list2d)-1):

                        if middle <= totalSeat:
                            list3d[i][index] = middle
                            middle += 1
                            
                        else:
                            break

                break
            first += 1


# main or driver program


if __name__ == '__main__':
    totalSeat = int(input())
    arr = list(map(int, input().strip().split()))
    seatList = []
    createDynamicSeats(arr, seatList)
    max_elem = max(arr)

    window = fillAisleSeat(seatList, totalSeat, max_elem)
    middle = fillWindowSeat(seatList, window, totalSeat, max_elem)
    fillMiddleSeat(seatList, middle, totalSeat, max_elem)

    for i in seatList:
        print(i)
